from typing import List

class TrieNode:
    __slots__ = ("children", "word")
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.word = None        # the full word if a word ends here


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # ---- 1. build trie ----
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w            # store the word at its terminal node

        R, C = len(board), len(board[0])
        res = []

        # ---- 2. DFS from every cell ----
        def dfs(r, c, node):
            ch = board[r][c]
            nxt = node.children.get(ch)
            if nxt is None:          # no word continues with this char -> prune
                return

            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word = None      # de-duplicate: don't report same word twice

            board[r][c] = '#'        # mark visited (in place)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '#':
                    dfs(nr, nc, nxt)
            board[r][c] = ch         # backtrack: restore

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)

        return res