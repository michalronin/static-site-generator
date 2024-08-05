def markdown_to_blocks(markdown):
    blocks = [block.strip() for block in markdown.split("\n\n")]
    return blocks
