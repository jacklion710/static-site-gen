import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

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

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if all(line.startswith(">") for line in block.split("\n")):
        return block_type_quote
    if all(line.startswith(("*", "-")) for line in block.split("\n")):
        return  block_type_unordered_list
    if all(re.match(r"^\d+\.", line) for line in block.split("\n")):
        return block_type_ordered_list
    return block_type_paragraph