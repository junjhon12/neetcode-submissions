class PrefixTree:
    def __init__(self):
        self.words = set()
        self.prefixes = {}

    def insert(self, word: str) -> None:
        self.words.add(word)

        # tmp_prefix = ""
        for i in range(len(word), 0, -1):
            tmp_prefix = word[:i]
            # print(tmp_prefix)
            if i not in self.prefixes:
                self.prefixes[i] = set()

            if tmp_prefix in self.prefixes[i]:
                break

            self.prefixes[i].add(tmp_prefix)

            # print(self.prefixes)

        

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) in self.prefixes:
            if prefix in self.prefixes[len(prefix)]:
                return True

        return False
