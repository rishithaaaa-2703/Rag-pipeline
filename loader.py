def load_markdown(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    return text

def extract_title(text):
    lines = text.splitlines()       # break the text into a list of lines
    for line in lines:              # look at each line, one at a time
        cleaned = line.strip()      # trim whitespace off both ends
        if cleaned:                 # true only if something's left — i.e. not blank
            cleaned = cleaned.lstrip("#")   # remove leading # characters
            cleaned = cleaned.strip()       # remove the space(s) left after the #
            return cleaned           # hand it back immediately — stop looking
    return None                      # only reached if every line was blank

result = load_markdown("sample.md")
print(result)
text = load_markdown("sample.md")
title = extract_title(text)
print(title)