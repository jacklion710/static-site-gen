from textnode import TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        # Create a LeafNode with no tag and the text_node.text as the value
        html_node = LeafNode(tag=None, value=text_node.text)
        return html_node
    if text_node.text_type == "bold":
        # Create a LeafNode with a "b" tag and the text
        html_node = LeafNode(tag="b", value=text_node.text)
        return html_node
    if text_node.text_type == "italic":
        # Create a LeafNode with an "i" tag and the text
        html_node = LeafNode(tag="i", value=text_node.text)
        return html_node
    if text_node.text_type == "code":
        # "code" tag, text
        html_node = LeafNode(tag="code", value=text_node.text)
        return html_node
    if text_node.text_type == "link":
        # "a" tag, anchor text, and "href" prop
        html_node = LeafNode(tag="a", value=text_node.text, prop="href")
        return html_node
    if text_node.text_type == "image":
        # "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        html_node = LeafNode(tag="img", value="", props=props)
        return html_node
    raise Exception("Node type is invalid")

def main():
    node = TextNode("This is a text node", "bold", "https//www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
