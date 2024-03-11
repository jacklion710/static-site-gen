import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == "text":
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Unmatched delimiter found.") 
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part: 
                        new_node_list.append(TextNode(part, "text"))
                else:
                    new_node_list.append(TextNode(part, text_type))
        else:
            new_node_list.append(node)
    return new_node_list

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == text_type_text:
            images = extract_markdown_images(node.text)
            if not images:
                new_nodes.append(node)
                continue
            remaining_text = node.text
            for alt_text, url in images:
                parts = remaining_text.split(f"![{alt_text}]({url})", 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], text_type_text))
                new_nodes.append(TextNode(alt_text, text_type_image, url))
                remaining_text = parts[1] if len(parts) > 1 else ""
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == text_type_text:
            links = extract_markdown_links(node.text)
            if not links:
                new_nodes.append(node)
                continue
            remaining_text = node.text
            for link_text, url in links:
                parts = remaining_text.split(f"[{link_text}]({url})", 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], text_type_text))
                new_nodes.append(TextNode(link_text, text_type_link, url))
                remaining_text = parts[1] if len(parts) > 1 else ""
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes

text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
result = [
    TextNode("This is ", text_type_text),
    TextNode("text", text_type_bold),
    TextNode(" with an ", text_type_text),
    TextNode("italic", text_type_italic),
    TextNode(" word and a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" and an ", text_type_text),
    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
    TextNode(" and a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),
]

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]

    nodes = split_node_delimiter(nodes, "**", text_type_bold)  # Bold
    nodes = split_node_delimiter(nodes, "*", text_type_italic)  # Italic
    nodes = split_node_delimiter(nodes, "`", text_type_code)  # Code

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    # Filter out any empty TextNodes if necessary
    nodes = [node for node in nodes if node.text.strip()]
    
    return nodes

text_to_textnodes(text)
