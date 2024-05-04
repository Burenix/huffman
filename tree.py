import heapq
from collections import Counter

class TreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTreeBuilder:
    @staticmethod
    def build_tree(text):
        freq = Counter(text)
        priority_queue = [TreeNode(char, freq) for char, freq in freq.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            merged = TreeNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(priority_queue, merged)

        return merged