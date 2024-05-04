class HuffmanEncoder:
    @staticmethod
    def build_codes(node, prefix="", codes=None):
        if codes is None:
            codes = {}
        if node is not None:
            if node.left is None and node.right is None:
                codes[node.char] = prefix if prefix else '0'
            else:
                HuffmanEncoder.build_codes(node.left, prefix + "0", codes)
                HuffmanEncoder.build_codes(node.right, prefix + "1", codes)
        return codes

    @staticmethod
    def encode(text, codes):
        return ''.join(codes[char] for char in text)