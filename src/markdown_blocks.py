# markdown_blocks.py

import re
from htmlnode import HTMLNode
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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
    list_items = []
    for item in items:
        item_text = item.lstrip('* ').lstrip('- ')
        text_nodes = text_to_textnodes(item_text)
        list_items.append(ParentNode(children=[text_node_to_html_node(node) for node in text_nodes], tag="li"))
    new_block = HTMLNode(tag="ul", children=list_items)
    return new_block

def convert_ordered_list(block):
    items = block.split("\n")
    list_items = []
    for item in items:
        item_text = re.sub(r"^\d+\.\s", "", item)
        text_nodes = text_to_textnodes(item_text)
        list_items.append(ParentNode(children=[text_node_to_html_node(node) for node in text_nodes], tag="li"))
    new_block = HTMLNode(tag="ol", children=list_items)
    return new_block

def convert_paragraph(block):
    return HTMLNode(tag="p", value=block)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        text_nodes = text_to_textnodes(block)
        return ParentNode(children=[text_node_to_html_node(node) for node in text_nodes], tag="p")
    if block_type == block_type_heading:
        text_nodes = text_to_textnodes(block)
        hash_count = block.count("#", 0, block.find(" "))
        tag = f"h{hash_count}"
        return ParentNode(children=[text_node_to_html_node(node) for node in text_nodes], tag=tag)
    if block_type == block_type_code:
        return convert_code(block)
    if block_type == block_type_ordered_list:
        return convert_ordered_list(block)
    if block_type == block_type_unordered_list:
        return convert_unordered_list(block)
    if block_type == block_type_quote:
        text_nodes = text_to_textnodes(block)
        return ParentNode(children=[text_node_to_html_node(node) for node in text_nodes], tag="blockquote")
    raise ValueError("Invalid block type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    parent_node = ParentNode(children=children, tag="div", props=None)
    return parent_node