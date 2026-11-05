class WordDictionary:
    class Node:
        def __init__(self):
            self.edges = dict()
            self.terminal = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.edges:
                node.edges[c] = self.Node()
            node = node.edges[c]
        node.terminal = True

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)

    def _search(self, word: str, l: int, node: self.Node) -> bool:
        for i in range(l, len(word)):
            c = word[i]
            if c in node.edges:
                node = node.edges[c]
                continue
            if c == '.':
                for cc in node.edges.keys():
                    if self._search(word, i+1, node.edges[cc]):
                        return True
            return False
        return node.terminal
