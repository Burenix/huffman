class HuffmanDecoder:
    @staticmethod
    def decode(encoded_text, codes):
        reverse_codes = {v: k for k, v in codes.items()}
        decoded_text = ""
        current_code = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_codes:
                decoded_text += reverse_codes[current_code]
                current_code = ""
        return decoded_text