import unittest


from block_markdown import (
    markdown_to_blocks,
)


test_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        blocks = markdown_to_blocks(test_text)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            ],
            blocks,
        )
