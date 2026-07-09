# LLM Safety & Evaluation Toolkit

A lightweight testing suite designed to evaluate Large Language Models (LLMs) for toxicity, jailbreaks, and adversarial safety vulnerabilities.

## 🎯 Overview
As LLMs are integrated into production environments, automated security testing is critical. This toolkit provides a foundation for continuous evaluation of LLM vulnerabilities, checking for prompt injections and factual consistency (hallucinations).

### Core Capabilities
1. **Automated Red Teaming (`src/red_team.py`):** Injects adversarial prompts (jailbreaks, developer mode bypasses) to test system guardrails.
2. **Hallucination Auditing (`src/auditor.py`):** Measures factual consistency between a trusted source document and the LLM's output to detect semantic drift.
3. **Automated Reporting (`src/report.py`):** Aggregates raw JSON findings into clean, human-readable markdown summaries.

## 📂 Architecture
* `/config` - Contains `payloads.json` with standardized adversarial testing prompts.
* `/src` - Core scanning engines and report generation logic.
* `/reports` - Output directory for test results and final markdown summaries.

## 🚀 Quick Start
To run this evaluation suite locally:

1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
