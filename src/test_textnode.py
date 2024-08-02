import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a first text node", "italic", "https://duckduckgo.com")
        node2 = TextNode("This is a second text node", "bold", "https://duckduckgo.com")
        self.assertNotEqual(node, node2)

    def test_url_and_no_url(self):
        node = TextNode("This is a text node", "bold", "https://duckduckgo.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_text_type_different(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "code")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
