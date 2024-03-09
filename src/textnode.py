class TextNode:
    """TextNode class"""
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'