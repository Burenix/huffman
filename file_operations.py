import bitarray
import pickle
import chardet

from tree import HuffmanTreeBuilder
from encoder import HuffmanEncoder
from decoder import HuffmanDecoder

class FileEncoder:
    @staticmethod
    def encode(input_filename, output_filename):
        with open(input_filename, 'rb') as file:
            byte_content = file.read()
            encoding = chardet.detect(byte_content)['encoding']
            text = byte_content.decode(encoding)
        root = HuffmanTreeBuilder.build_tree(text)
        codes = HuffmanEncoder.build_codes(root)
        encoded_text = HuffmanEncoder.encode(text, codes)
        with open(output_filename, 'wb') as file:
            byte_array = bitarray.bitarray(encoded_text)
            byte_array.tofile(file)
        with open(output_filename + ".dict", 'wb') as dict_file:
            pickle.dump(codes, dict_file)

class FileDecoder:
    @staticmethod
    def decode(input_filename, output_filename):
        with open(input_filename, 'rb') as file:
            encoded_bytes = file.read()
        with open(input_filename + ".dict", 'rb') as dict_file:
            codes = pickle.load(dict_file)
        encoded_text = bitarray.bitarray()
        encoded_text.frombytes(encoded_bytes)
        encoded_text = encoded_text.to01()
        decoded_text = HuffmanDecoder.decode(encoded_text, codes)
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(decoded_text)