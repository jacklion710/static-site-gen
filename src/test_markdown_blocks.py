import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
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

if __name__ == "__main__":
    unittest.main()
