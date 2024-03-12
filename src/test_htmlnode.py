# test_htmlnode.py

import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test 1: Node with no props
        node1 = HTMLNode(tag='p', value='Hello, World!')
        self.assertEqual(node1.props_to_html(), '')

        # Test 2: Node with props
        node2 = HTMLNode(tag='a', value='Click me', props={'href': 'https://www.example.com', 'target': '_blank'})
        self.assertEqual(node2.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_repr(self):
        # Test 3: Ensure __repr__ method works correctly
        node = HTMLNode(tag='div', value='Container', props={'class': 'my-container'})
        expected_repr = "HTMLNode(tag='div', value='Container', children=[], props={'class': 'my-container'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()