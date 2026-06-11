from pathlib import Path

# Current project root
PROJECT_NAME = "NL2SQL"

folders = [
    "data",
    "metadata",
    "scripts",
    "config",
    "agents",
    "rag",
    "validation",
    "execution",
    "evaluation",
    "notebooks",
    "tests",
    "logs"
]

files = {
    ".env": "",
    ".gitignore": """venv/
.env
__pycache__/
.ipynb_checkpoints/
*.pyc
logs/
""",
    "README.md": "# Enterprise NL2SQL Assistant\n",
    "requirements.txt": "",

    "config/db_config.py": "",

    "scripts/create_tables.py": "",
    "scripts/load_data.py": "",

    "rag/embed_schema.py": "",
    "rag/pinecone_loader.py": "",
    "rag/schema_retriever.py": "",

    "agents/intent_agent.py": "",
    "agents/schema_agent.py": "",
    "agents/sql_agent.py": "",
    "agents/validation_agent.py": "",
    "agents/execution_agent.py": "",
    "agents/insight_agent.py": "",

    "validation/sql_validator.py": "",
    "execution/query_executor.py": "",

    "evaluation/evaluate.py": "",
    "evaluation/benchmark_questions.csv": ""
}

root = Path(PROJECT_NAME)

root.mkdir(exist_ok=True)

for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

for file_path, content in files.items():
    full_path = root / file_path

    full_path.parent.mkdir(parents=True, exist_ok=True)

    if not full_path.exists():
        full_path.write_text(content, encoding="utf-8")

print(f"✅ Project structure created successfully: {PROJECT_NAME}")