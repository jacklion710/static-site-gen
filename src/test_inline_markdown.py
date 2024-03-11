import unittest
from inline_markdown import split_node_delimiter, TextNode, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

class TestDelimiter(unittest.TestCase):
    def test_split_with_delimiter(self):
        """Test splitting a string with a defined delimiter."""
        node = TextNode("This is **bold** text", "text")
        expected = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text"),
        ]
        result = split_node_delimiter([node], "**", "bold")
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        """Test input text without the delimiter."""
        node = TextNode("This is plain text", "text")
        expected = [node]  # Should remain unchanged
        result = split_node_delimiter([node], "**", "bold")
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """Test an empty TextNode."""
        node = TextNode("", "text")
        expected = []  # Expecting an empty list for an empty TextNode
        result = split_node_delimiter([node], "**", "bold")
        self.assertEqual(result, expected)

    def test_unmatched_delimiter_raises_error(self):
        """Test that an unmatched delimiter raises an error."""
        node = TextNode("This is **bold text", "text")
        with self.assertRaises(ValueError):
            split_node_delimiter([node], "**", "bold")

    def test_extract_markdown_images(self):
        """Test the extract markdown images function"""
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        expected = [('image', 'https://i.imgur.com/zjjcJKZ.png'), ('another', 'https://i.imgur.com/dfsdkjfd.png')]
        result = extract_markdown_images(text)
        self.assertListEqual(result, expected)

    def test_extract_markdown_links(self):
        """Test the extract markdown links function"""
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')]
        result = extract_markdown_links(text)
        self.assertListEqual(result, expected)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
            ),
        ]
        result = split_nodes_image([node])
        self.assertListEqual(result, expected)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_link, "https://i.imgur.com/3elNhQu.png"
            ),
        ]
        result = split_nodes_link([node])
        self.assertListEqual(result, expected)

    def test_text_to_textnodes(self):
        """Test the text_to_textnodes function for accurate node splitting."""
        input_text = "This is **bold** text with an *italic* word, a `code block`, an ![image](https://i.imgur.com/zjjcJKZ.png), and a [link](https://boot.dev)."
        expected_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word, a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(", an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(", and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
            TextNode(".", text_type_text),
        ]
        result_nodes = text_to_textnodes(input_text)
        self.assertEqual(len(result_nodes), len(expected_nodes))
        for result_node, expected_node in zip(result_nodes, expected_nodes):
            self.assertEqual(result_node, expected_node)

if __name__ == "__main__":
    unittest.main()
