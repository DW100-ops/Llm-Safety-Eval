import os

structure = {
    "config": ["payloads.json"],
    "src": ["__init__.py", "red_team.py", "auditor.py", "report.py"],
    "tests": ["__init__.py", "test_red_team.py", "test_auditor.py"],
    "reports": [".gitkeep"]
}

root_files = ["requirements.txt", "README.md", ".gitignore", ".env"]

for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")
            print(f"Created: {file_path}")

for file in root_files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            if file == ".gitignore":
                f.write(".env\n__pycache__/\n*.pyc\nreports/*.md\nreports/*.pdf\n")
            elif file == "requirements.txt":
                f.write("openai>=1.0.0\npydantic>=2.0.0\npytest>=8.0.0\npython-dotenv>=1.0.0\n")
        print(f"Created root file: {file}")

print("\nStructure created successfully! You can delete setup_repo.py now.")