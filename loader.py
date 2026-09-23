def load_markdown(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    return text

result = load_markdown("sample.md")
print(result)