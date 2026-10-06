from pathlib import Path

def load_markdown(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    return text

def extract_title(text):
    lines = text.splitlines()
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            cleaned = cleaned.lstrip("#")
            cleaned = cleaned.strip()
            return cleaned
    return None

if __name__ == "__main__":
    for path in sorted(Path("docs").glob("*.md")):
        text = load_markdown(path)
        title = extract_title(text)
        print(title)