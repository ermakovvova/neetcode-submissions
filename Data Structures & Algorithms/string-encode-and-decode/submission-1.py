class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        num = str(len(strs))
        lengths = [str(len(s)) for s in strs]
        arr = [num] + lengths
        res = '_'.join(arr)
        res = '_'.join([res] + strs)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        num = ''
        while s[i] != '_':
            num += s[i]
            i += 1
        num = int(num)

        lengths = []
        curr_length = ''
        i += 1
        while i < len(s) and len(lengths) < num:
            if s[i] != '_':
                curr_length += s[i]
            else:
                lengths.append(int(curr_length))
                curr_length = ''
            i += 1

        res = []
        for j in range(num):
            res.append(s[i : i + lengths[j]])
            i += lengths[j] + 1

        return res

            


        

            



        
            
