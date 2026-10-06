from loader import load_markdown, extract_title

text = load_markdown("docs/cats.md")
print(extract_title(text))