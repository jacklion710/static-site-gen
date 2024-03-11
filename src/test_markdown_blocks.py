import unittest
from markdown_blocks import markdown_to_blocks

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

if __name__ == "__main__":
    unittest.main()
