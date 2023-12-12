class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candy = list(sorted(candies))[-1]

        for candy in candies:
            if candy + extraCandies >= max_candy:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        