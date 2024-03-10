from textnode import TextNode

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
