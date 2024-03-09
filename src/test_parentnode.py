import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_init(self):
        # Test 1: Initializing with valid arguments
        child = LeafNode(tag="p", value="Child node")
        node = ParentNode(children=[child], tag="div", props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [child])
        self.assertEqual(node.props, {"class": "container"})

        # Test 2: Initializing with no props
        node = ParentNode(children=[child], tag="div")
        self.assertEqual(node.props, {})

    def test_to_html_with_tag_and_children(self):
        # Test 3: Rendering with a tag and children
        child1 = LeafNode(tag="p", value="Paragraph 1")
        child2 = LeafNode(tag="p", value="Paragraph 2")
        node = ParentNode(children=[child1, child2], tag="div", props={"id": "content"})
        expected_html = '<div id="content"><p>Paragraph 1</p><p>Paragraph 2</p></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_tag(self):
        # Test 4: Rendering without a tag
        child = LeafNode(tag="p", value="Child node")
        node = ParentNode(children=[child], tag=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_children(self):
        # Test 5: Rendering without children
        node = ParentNode(children=[], tag="div")
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()