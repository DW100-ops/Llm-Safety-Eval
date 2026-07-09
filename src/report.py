import os
import json
from datetime import datetime

def generate_markdown_report():
    red_team_path = os.path.join("reports", "red_team_report.json")
    auditor_path = os.path.join("reports", "hallucination_report.json")
    output_path = os.path.join("reports", "safety_summary.md")
    
    print("] Generating Final Human-Readable Safety Report...")
    
    # 1. Load data from the Red Teaming Engine
    red_team_results = []
    if os.path.exists(red_team_path):
        with open(red_team_path, "r") as f:
            red_team_results = json.load(f)
            
    # 2. Load data from the Hallucination Auditor
    audit_results = []
    if os.path.exists(auditor_path):
        with open(auditor_path, "r") as f:
            audit_results = json.load(f)
            
    # 3. Calculate high-level statistics
    total_rt = len(red_team_results)
    failed_rt = sum(1 for x in red_team_results if x["assessment"] == "FAILED")
    
    total_aud = len(audit_results)
    failed_aud = sum(1 for x in audit_results if x["hallucination_detected"])
    
    # 4. Build the Markdown Document
    markdown = f"""# LLM Safety & Evaluation Report
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## 📊 Executive Summary
This report aggregates automated evaluations measuring safety vulnerabilities (red teaming) and factual consistency (hallucination auditing).

* **Adversarial Safety Defenses:** {total_rt - failed_rt}/{total_rt} Passed
* **Factual Consistency Grounding:** {total_aud - failed_aud}/{total_aud} Passed

---

## 🛡️ Red Teaming & Jailbreak Vulnerability Scan
This section details how the target model handled deliberate, adversarial prompt injections designed to bypass guardrails.

| Test ID | Category | Risk Level | Assessment |
| :--- | :--- | :--- | :--- |
"""
    
    for res in red_team_results:
        status_symbol = "❌ FAILED" if res["assessment"] == "FAILED" else "✅ PASSED"
        markdown += f"| {res['test_id']} | {res['category']} | {res['risk_level']} | {status_symbol} |\n"
        
    markdown += """
### Detailed Vulnerability Breakthroughs
"""
    for res in red_team_results:
        if res["assessment"] == "FAILED":
            markdown += f"""
#### 🚨 {res['test_id']} - {res['category']} ({res['risk_level']} Risk)
* **Adversarial Prompt:** `{res['prompt']}`
* **Model Escape Response:** *"{res['llm_response']}"*
"""

    markdown += """
---

## 🔍 Hallucination & Factual Consistency Audit
This section measures semantic drift and grounding by validating model responses against trusted source contexts.

| Audit ID | Overlap Score | Hallucination Detected | Reasoning |
| :--- | :--- | :--- | :--- |
"""

    for aud in audit_results:
        h_symbol = "🚨 YES" if aud["hallucination_detected"] else "🍏 NO"
        markdown += f"| {aud['audit_id']} | {aud['overlap_score']} | {h_symbol} | {aud['reasoning']} |\n"

    # 5. Save the generated Markdown file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)
        
    print(f"\n Success! Markdown safety report generated at: {output_path}")

if __name__ == "__main__":
    generate_markdown_report();