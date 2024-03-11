import unittest
from htmlnode import HTMLNode

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    convert_heading,
    convert_code,
    convert_quote,
    convert_unordered_list,
    convert_ordered_list,
    convert_paragraph,
    markdown_to_html_node,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)

class TestMarkdownBlocks(unittest.TestCase):
    def test_single_block(self):
        """Test a single block with no line breaks."""
        md = "This is a single block of text."
        expected = ["This is a single block of text."]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_multiple_blocks(self):
        """Test multiple blocks separated by blank lines."""
        md = """# This is a heading

This is a paragraph of text.

* This is a list item
* This is another list item"""
        expected = [
            "# This is a heading",
            "This is a paragraph of text.",
            "* This is a list item\n* This is another list item"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_excessive_whitespace(self):
        """Test input with excessive whitespace between blocks."""
        md = """# Heading

        
        
This is text.


* List item 1
* List item 2"""
        expected = [
            "# Heading",
            "This is text.",
            "* List item 1\n* List item 2"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_trailing_and_leading_whitespace(self):
        """Test blocks with leading and trailing whitespace."""
        md = """
        
        This is a block with leading and trailing spaces.  
        
        
        """
        expected = ["This is a block with leading and trailing spaces."]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_empty_string(self):
        """Test empty string input."""
        md = ""
        expected = []
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_no_separation(self):
        """Test input where blocks are not separated by blank lines."""
        md = "Block 1\nBlock 2\nBlock 3"
        expected = ["Block 1\nBlock 2\nBlock 3"]  # Treated as a single block
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_block_is_heading(self):
        """Test if markdown block is a heading."""
        block = "## This is a heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result, expected)

    def test_block_is_code(self):
        """Test if markdown block is code."""
        block = "```py some python code```"
        result = block_to_block_type(block)
        expected = block_type_code
        self.assertEqual(result, expected)

    def test_block_is_quote(self):
        """Test if markdown block is a quote."""
        block = "> to be or not to be..."
        result = block_to_block_type(block)
        expected = block_type_quote
        self.assertEqual(result, expected)

    def test_block_is_unordered_list(self):
        """Test if markdown block is an unordered list."""
        block = "* item 1"
        result = block_to_block_type(block)
        expected = block_type_unordered_list
        self.assertEqual(result, expected)

    def test_block_is_ordered_list(self):
        """Test if markdown block is an ordered list."""
        block = "1. first point"
        result = block_to_block_type(block)
        expected = block_type_ordered_list
        self.assertEqual(result, expected)

    def test_block_is_paragraph(self):
        """Test if markdown block is a paragraph."""
        block = "This is a short paragraph"
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result, expected)

    def test_multi_line_code_block(self):
        """Test if multi-line markdown block is identified as code."""
        block = "```\ndef some_function():\n    pass\n```"
        result = block_to_block_type(block)
        expected = block_type_code
        self.assertEqual(result, expected)

    def test_invalid_heading(self):
        """Test if improperly formatted heading defaults to paragraph."""
        block = "##This is not a valid heading because it lacks space"
        result = block_to_block_type(block)
        expected = block_type_paragraph  # Assuming default behavior is to fallback to paragraph
        self.assertEqual(result, expected)

    def test_convert_heading(self):
        block = "## This is a heading"
        expected = HTMLNode(tag="h2", value="This is a heading")
        result = convert_heading(block)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(len(result.children), len(expected.children))

    def test_convert_code(self):
        block = "```\nprint('Hello, world!')\n```"
        expected_code_value = "print('Hello, world!')"
        result = convert_code(block)
        self.assertEqual(result.tag, "pre")
        self.assertTrue(any(child.tag == "code" and child.value == expected_code_value for child in result.children))

    def test_convert_quote(self):
        block = "> This is a quote"
        expected = HTMLNode(tag="blockquote", value="This is a quote")
        result = convert_quote(block)
        self.assertEqual(result, expected)

    def test_convert_unordered_list(self):
        block = "* Item 1\n* Item 2"
        expected = HTMLNode(tag="ul", children=[HTMLNode(tag="li", value="Item 1"), HTMLNode(tag="li", value="Item 2")])
        result = convert_unordered_list(block)
        self.assertEqual(result, expected)

    def test_convert_ordered_list(self):
        block = "1. Item 1\n2. Item 2"
        expected = HTMLNode(tag="ol", children=[HTMLNode(tag="li", value="Item 1"), HTMLNode(tag="li", value="Item 2")])
        result = convert_ordered_list(block)
        self.assertEqual(result, expected)

    def test_convert_paragraph(self):
        block = "This is a paragraph."
        expected = HTMLNode(tag="p", value=block)
        result = convert_paragraph(block)
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(len(result.children), len(expected.children))

if __name__ == "__main__":
    unittest.main()
