# Experiment 06: Collaborative Multi-Agent System

## 1. Project Title
Collaborative Multi-Agent System using Local LLM (Ollama)

## 2. Objective
To design and implement a collaborative multi-agent system in which multiple AI agents perform specialized tasks and coordinate to solve a common problem.

## 3. Architecture
The system uses a Supervisor-Worker sequential pipeline:
User -> Coordinator -> Research -> Analysis -> Writer -> Review -> Final Output

## 4. Agent Descriptions
- **Coordinator Agent**: Breaks down the user task into a research directive.
- **Research Agent**: Gathers facts, concepts, and data.
- **Analysis Agent**: Processes and structures the research data.
- **Writer Agent**: Drafts a structured Markdown report.
- **Review Agent**: Critiques and improves the final report.

## 5. Requirements
- Python 3.10+
- Ollama installed and running
- Model: `qwen3.5:9b`

## 6-12. Setup & Execution
1. Install Ollama from [ollama.com](https://ollama.com).
2. Download model: `ollama pull qwen3.5:9b`
3. Start Ollama: `ollama serve`
4. Create venv: `python -m venv venv` and activate it.
5. Install deps: `pip install -r requirements.txt`
6. Run: `python main.py`

## 13. Example Input
Prepare a report on the applications of Artificial Intelligence in Healthcare.

## 14. Example Output
The system will output the step-by-step thinking of each agent, followed by a polished Markdown report in the "FINAL OUTPUT" section.

## 15. Troubleshooting
- If `ollama` is not recognized, ensure it's added to your system PATH.
- If connection fails, run `ollama serve` in a separate terminal.
- If model not found, run `ollama pull qwen3.5:9b`.
