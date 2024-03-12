# test_textnode.py

import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test 1
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        # Test 2
        node = TextNode("This is another text node", "bold", "www.newtest.com")
        node2 = TextNode("This is a new text node", "bold", "www.testnew.com")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        # Test 3
        node = TextNode("Yet another text node", "italic")
        self.assertIsNone(node.url)

    def test_different_text(self):
        # Test 4
        node = TextNode("Different text", "bold")
        node2 = TextNode("Another different text", "bold")
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        # Test 5
        node = TextNode("Same text", "bold")
        node2 = TextNode("Same text", "italic")
        self.assertNotEqual(node, node2)

    def test_url_is_not_none(self):
        # Test 6
        node = TextNode("Text with URL", "link", "https://www.example.com")
        self.assertIsNotNone(node.url)
    
    def test_eq_with_url(self):
        # Test 7
        node = TextNode("Text with URL", "link", "https://www.example.com")
        node2 = TextNode("Text with URL", "link", "https://www.example.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()