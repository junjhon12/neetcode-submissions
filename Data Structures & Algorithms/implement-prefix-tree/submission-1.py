class TrieNode:
    __slots__ = ("children", "is_end")          # small memory win
    def __init__(self):
        self.children = {}                       # char -> TrieNode
        self.is_end = False                      # marks end of an inserted word


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    # ---- insert ----
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()   # create node on demand
            node = node.children[ch]
        node.is_end = True                       # mark the word's end

    # ---- shared walk ----
    def _walk(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None                      # path breaks -> not found
            node = node.children[ch]
        return node                              # node at end of path

    # ---- queries ----
    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end  # path exists AND word ends here

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None    # path exists -> prefix exists