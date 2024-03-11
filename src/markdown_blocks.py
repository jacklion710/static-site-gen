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
