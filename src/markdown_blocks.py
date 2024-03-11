md = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item
"""

def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n")
    temp = []
    for line in lines:
        if line.strip() == "":
            if temp:
                blocks.append("\n".join(temp).strip())
                temp = []
        else:
            temp.append(line)
    if temp:
        blocks.append("\n".join(temp).strip())

    return blocks
        


print(markdown_to_blocks(md))