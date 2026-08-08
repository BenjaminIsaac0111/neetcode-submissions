class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(f'{len(s)}#{s}')
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            lenght = int(s[i:j])
            
            i = j + 1

            end_index = i + lenght
            extract = s[i:end_index]
            decoded_string.append(extract)
            i = end_index
        return decoded_string