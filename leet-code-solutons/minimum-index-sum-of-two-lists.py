class Solution:
    def build_dict(self, l: List[str]):
        book = {}
        
        for i, val in enumerate(l):
            book[val] = i
        
        return book
    
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list3 = [val for val in list1 if val in list2]
        book1, book2 = self.build_dict(list1), self.build_dict(list2)
        ans = {}
        
        for val in list3:
            i = book1[val] + book2[val]
            if i not in ans:
                ans[i] = [val]
            else:
                ans[i].append(val)
        
        return ans[sorted(ans.keys())[0]]