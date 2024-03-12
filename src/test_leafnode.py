# test_leafnode.py

import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        # Test 1: Initializing with valid arguments
        node = LeafNode(tag="p", value="Hello, World!", props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, {"class": "text"})

        # Test 2: Initializing with no props
        node = LeafNode(tag="a", value="Click me")
        self.assertEqual(node.props, {})

    def test_to_html_with_tag(self):
        # Test 3: Rendering with a tag
        node = LeafNode(tag="h1", value="Heading", props={"id": "title"})
        expected_html = '<h1 id="title">Heading</h1>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_tag(self):
        # Test 4: Rendering without a tag
        node = LeafNode(tag=None, value="Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_to_html_without_value(self):
        # Test 5: Rendering without a value
        node = LeafNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()