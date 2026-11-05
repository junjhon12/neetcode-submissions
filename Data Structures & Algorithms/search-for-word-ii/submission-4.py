class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.complete_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_end = True
        curr_node.complete_word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_trie = Trie()

        for word in words:
            word_trie.addWord(word)

        present_words = []

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, parent):
            if row < 0 or row >= rows or cols <= col or col < 0 or board[row][col] == ".":
                return
            curr_char = board[row][col]

            if curr_char in parent.children:
                if parent.children[curr_char].is_end == True:
                    present_words.append(parent.children[curr_char].complete_word)
                    parent.children[curr_char].is_end = False                
                child = parent.children[curr_char]
                
                original = board[row][col]
                board[row][col] = "."
            else:
                return
            
            dfs(row + 1, col, child)
            dfs(row - 1, col, child)
            dfs(row, col + 1, child)
            dfs(row, col - 1, child)
            
            board[row][col] = original

            if child and child.is_end == False and not child.children:
                del parent.children[curr_char]     

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, word_trie.root)     
        return present_words
    

        
       
        