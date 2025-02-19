class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_length_product=0        
        sets = [set(word) for word in words]
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word1 = words[i]
                word2 = words[j]

                if sets[i].isdisjoint(sets[j]):
                    max_length_product = max(max_length_product, len(word1) * len(word2))
        
        return max_length_product
        