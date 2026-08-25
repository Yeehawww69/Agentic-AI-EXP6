"""
agents.py
Defines the 5 specialized agents for the collaborative multi-agent system.
"""

from ollama_client import OllamaLLM

class BaseAgent:
    """Base class for all agents."""
    def __init__(self, name: str, role_prompt: str, llm: OllamaLLM):
        self.name = name
        self.role_prompt = role_prompt
        self.llm = llm

    def run(self, input_data: str) -> str:
        """Default run method for agents taking a single string input."""
        prompt = f"{self.role_prompt}\n\nInput:\n{input_data}\n\nOutput:"
        return self.llm.generate(prompt)


class CoordinatorAgent(BaseAgent):
    """
    Coordinator Agent: Understands the user task and breaks it down 
    into a specific research subtask for the Research Agent.
    """
    def __init__(self, llm: OllamaLLM):
        role = """You are the Coordinator Agent in a collaborative multi-agent system.
Your job is to understand the user's task and break it down into a specific, actionable research subtask for the Research Agent.
Do NOT solve the task yourself. Do NOT write the final report.
Just output a clear, concise research directive.
Do not include any introductory or concluding conversational text."""
        super().__init__("Coordinator", role, llm)


class ResearchAgent(BaseAgent):
    """
    Research Agent: Gathers facts, concepts, and data about the assigned topic.
    """
    def __init__(self, llm: OllamaLLM):
        role = """You are the Research Agent in a collaborative multi-agent system.
Your job is ONLY to research the assigned topic.
Do not write the final report.
Provide:
- Important concepts
- Relevant facts
- Key points
- Advantages
- Limitations
- Useful examples
Return concise but useful research material for the Analysis Agent.
Do not include any introductory or concluding conversational text."""
        super().__init__("Research", role, llm)


class AnalysisAgent(BaseAgent):
    """
    Analysis Agent: Analyzes the research data, identifies patterns, 
    and structures the information logically.
    """
    def __init__(self, llm: OllamaLLM):
        role = """You are the Analysis Agent in a collaborative multi-agent system.
Your job is to analyze the research material provided.
Identify important findings, compare ideas, identify advantages and limitations, and organize the information logically.
Do not write the final report.
Return a structured analysis.
Do not include any introductory or concluding conversational text."""
        super().__init__("Analysis", role, llm)


class WriterAgent(BaseAgent):
    """
    Writer Agent: Takes research and analysis to draft a structured final report.
    """
    def __init__(self, llm: OllamaLLM):
        role = """You are the Writer Agent in a collaborative multi-agent system.
Your job is to generate a structured final report using the research and analysis provided.
Maintain logical flow, use Markdown headings, and produce clear and readable content.
Structure:
# Title
## Introduction
## Key Concepts / Applications
## Advantages
## Limitations
## Conclusion
Do not include any introductory or concluding conversational text."""
        super().__init__("Writer", role, llm)

    def run(self, research_data: str, analysis_data: str) -> str:
        """Overrides base run to accept both research and analysis data."""
        prompt = f"""{self.role_prompt}

Research Data:
{research_data}

Analysis Data:
{analysis_data}

Output:"""
        return self.llm.generate(prompt)


class ReviewAgent(BaseAgent):
    """
    Review Agent: Reviews the drafted report, checks for completeness, 
    and provides an improved final version.
    """
    def __init__(self, llm: OllamaLLM):
        role = """You are the Review Agent in a collaborative multi-agent system.
Your job is to review the generated report.
Check completeness, relevance, logical organization, clarity, and factual consistency.
First, output exactly "REVIEW FINDINGS:" followed by bullet points of your critique.
Then, output exactly "IMPROVED FINAL REPORT:" followed by the fully polished and improved report in Markdown.
Do not include any introductory or concluding conversational text."""
        super().__init__("Review", role, llm)