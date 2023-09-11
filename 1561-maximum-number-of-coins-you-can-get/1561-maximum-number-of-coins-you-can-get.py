class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bobs_index = 0
        alice_index = len(piles) - 1
        my_index = alice_index - 1
        
        res = 0
        
        while bobs_index < my_index:
            res += piles[my_index]
            bobs_index += 1
            alice_index -= 1
            my_index -= 2
            
        return res