class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "[" + ", ".join(repr(char) for char in strs) + "]"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = eval(s)
        return decoded_strs