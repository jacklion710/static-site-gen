import unittest
from inline_markdown import split_node_delimiter, TextNode

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

if __name__ == "__main__":
    unittest.main()
