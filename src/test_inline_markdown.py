import unittest
from inline_markdown import split_node_delimiter, TextNode, extract_markdown_images, extract_markdown_links

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


if __name__ == "__main__":
    unittest.main()
