# markdown_blocks.py

import re
from htmlnode import HTMLNode
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode

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

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

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
    hash_count = block.count("#", 0, block.find(" "))
    title_text = re.sub(r"^#+\s*", "", block)  # Remove hash symbols and leading spaces
    print(f"Converting heading: '{title_text}' with level {hash_count}")
    html_content = ''.join([text_node_to_html_node(node).to_html() for node in text_to_textnodes(title_text)])
    print(f"Generated HTML content for heading: '{html_content}'")
    return LeafNode(tag=f"h{hash_count}", value=html_content, props={})

def convert_code(block):
    trimmed_block = block.strip("`")
    code_content = trimmed_block.strip() 
    code_node = LeafNode(tag="code", value=code_content)
    pre_node = ParentNode(children=[code_node], tag="pre")
    return pre_node

def convert_quote(block):
    quote_lines = block.split("\n")
    quote_contents = [re.sub(r"^>\s*", "", line) for line in quote_lines]  # Remove '>' from each line
    quote_html_nodes = [LeafNode(tag="p", value=line) for line in quote_contents if line.strip()]
    return ParentNode(children=quote_html_nodes, tag="blockquote")

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
    text_nodes = text_to_textnodes(block)
    new_block = ParentNode(children=[text_node_to_html_node(node) for node in text_nodes], tag="p")
    return new_block

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return convert_paragraph(block)
    if block_type == block_type_heading:
        return convert_heading(block)
    if block_type == block_type_code:
        return convert_code(block)
    if block_type == block_type_ordered_list:
        return convert_ordered_list(block)
    if block_type == block_type_unordered_list:
        return convert_unordered_list(block)
    if block_type == block_type_quote:
        return convert_quote(block)
    raise ValueError("Invalid block type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    parent_node = ParentNode(children=children, tag="div", props=None)
    return parent_node