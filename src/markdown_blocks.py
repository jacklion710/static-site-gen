import re
from htmlnode import HTMLNode
from htmlnode import LeafNode, LeafNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

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

def convert_heading(block):
    hash_count = block.count("#", 0, block.find(" "))  # Count '#' up to the first space
    heading_text = block[hash_count:].strip()
    tag = f"h{hash_count}"
    new_block = HTMLNode(tag=tag, value=heading_text)
    return new_block

def convert_code(block):
    code_lines = block.split("\n")[1:-1]
    code_text = "\n".join(code_lines)
    new_block = HTMLNode(tag="pre", value=None, children=[
        HTMLNode(tag="code", value=code_text)
    ])
    return new_block

def convert_quote(block):
    quote_lines = [line.lstrip('> ').rstrip() for line in block.split("\n")]
    quote_text = "\n".join(quote_lines)
    new_block = HTMLNode(tag="blockquote", value=quote_text)
    return new_block

def convert_unordered_list(block):
    items = block.split("\n")
    list_items = [HTMLNode(tag="li", value=item.lstrip('* ').lstrip('- ')) for item in items]
    new_block = HTMLNode(tag="ul", children=list_items)
    return new_block

def convert_ordered_list(block):
    items = block.split("\n")
    list_items = [HTMLNode(tag="li", value=re.sub(r"^\d+\.\s", "", item)) for item in items]
    new_block = HTMLNode(tag="ol", children=list_items)
    return new_block

def convert_paragraph(block):
    return HTMLNode(tag="p", value=block)

def markdown_to_html_node(text_node):
    # Determine the HTML representation based on the text_node's type
    if text_node.text_type == text_type_text:
        html_node = LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == text_type_bold:
        html_node = LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == text_type_italic:
        html_node = LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == text_type_code:
        html_node = LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == text_type_link:
        # Assuming 'prop' was meant to be 'props', and it should be a dictionary
        html_node = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == text_type_image:
        props = {"src": text_node.url, "alt": text_node.text}
        html_node = LeafNode(tag="img", value="", props=props)
    else:
        raise Exception(f"Unsupported text node type: {text_node.text_type}")
    
    return html_node