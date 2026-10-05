from pathlib import Path

# ("/") directory
root = Path(".")

# Software Architecture
folders = ["app/api", "app/core", "app/rag", "app/services", "data", "data/sample_kb", "templates", "static", "uploads", "tests", "notebook"]
files = ["app/main.py", "requirements.txt", "ingest_sample_kb.py", "run.py", ".env", "app/services/ingestion.py"]


for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)
for file in files:
    (root / file).touch()
    
    
if __name__ == "__main__":
    print("⚠️  Project Structure Changed.")
