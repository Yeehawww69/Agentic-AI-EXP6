"""
main.py
Main entry point for the Collaborative Multi-Agent System.
Orchestrates the workflow and handles user interaction.
"""

import sys
from ollama_client import OllamaLLM, OllamaConnectionError, OllamaModelError
from agents import (
    CoordinatorAgent, 
    ResearchAgent, 
    AnalysisAgent, 
    WriterAgent, 
    ReviewAgent
)

def print_header(text: str):
    """Prints a formatted main header."""
    print("\n" + "=" * 60)
    print(f"        {text}")
    print("=" * 60 + "\n")

def print_section(title: str):
    """Prints a formatted section header for agent outputs."""
    print("\n" + "-" * 60)
    print(f"[{title}]")
    print("-" * 60 + "\n")

def main():
    # 1. Display System Header
    print_header("COLLABORATIVE MULTI-AGENT SYSTEM")
    
    # 2. Initialize LLM and verify connection
    try:
        llm = OllamaLLM()
        # Quick test to ensure Ollama is running and responsive
        llm.generate("Hello")
    except OllamaConnectionError:
        print("\nERROR: Could not connect to Ollama.")
        print("\nPlease make sure:")
        print("1. Ollama is installed.")
        print("2. Ollama is running (run: ollama serve).")
        print("3. qwen3.5:9b has been downloaded (run: ollama pull qwen3.5:9b).")
        sys.exit(1)
    except OllamaModelError:
        print(f"\nERROR: Model 'qwen3.5:9b' not found.")
        print("\nPlease download the model by running:")
        print("ollama pull qwen3.5:9b")
        sys.exit(1)
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {e}")
        sys.exit(1)

    # 3. Get User Task
    print("Enter your task (or type 'exit' to quit):")
    user_task = input("> ").strip()
    
    if not user_task or user_task.lower() == 'exit':
        print("No task provided. Exiting.")
        sys.exit(0)

    print(f"\nUser Task: {user_task}")

    # 4. Initialize Agents
    coordinator = CoordinatorAgent(llm)
    researcher = ResearchAgent(llm)
    analyst = AnalysisAgent(llm)
    writer = WriterAgent(llm)
    reviewer = ReviewAgent(llm)

    # 5. Execute Workflow Pipeline
    
    # Step 1: Coordinator
    print_section("1] COORDINATOR AGENT")
    print("Understanding task and breaking it down...")
    research_task = coordinator.run(user_task)
    print(f"Subtask assigned:\n{research_task}")

    # Step 2: Research
    print_section("2] RESEARCH AGENT")
    print("Gathering information...")
    research_output = researcher.run(research_task)
    print(f"Research output:\n{research_output}")

    # Step 3: Analysis
    print_section("3] ANALYSIS AGENT")
    print("Analyzing research data...")
    analysis_output = analyst.run(research_output)
    print(f"Analysis output:\n{analysis_output}")

    # Step 4: Writer
    print_section("4] WRITER AGENT")
    print("Drafting the report...")
    writer_output = writer.run(research_output, analysis_output)
    print(f"Generated report:\n{writer_output}")

    # Step 5: Review
    print_section("5] REVIEW AGENT")
    print("Reviewing and refining the report...")
    review_output = reviewer.run(writer_output)
    print(f"Review output:\n{review_output}")

    # 6. Final Output Extraction
    print_section("FINAL OUTPUT")
    # Extract the improved report if the Review Agent followed the format
    if "IMPROVED FINAL REPORT:" in review_output:
        final_report = review_output.split("IMPROVED FINAL REPORT:")[-1].strip()
    else:
        final_report = review_output
        
    print(final_report)
    print("\n" + "=" * 60)
    print("Process completed successfully.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()