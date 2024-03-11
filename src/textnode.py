from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    """TextNode class"""
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
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
