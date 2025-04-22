class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict_freq=Counter(s)
        sorted_items = sorted(dict_freq.items(), key=lambda item: item[1])
        resul=sorted_items[0][0]

        if(sorted_items[0][1] == 1):
            return s.index(resul)
        else: 
            return -1
