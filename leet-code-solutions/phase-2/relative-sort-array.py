class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        present_elements = {}
        len_arr1 = len(arr1)

        for i in range(len(arr2)):
            present_elements[arr2[i]] = i

        def relativeSort(x):
            if x in present_elements:
                return present_elements[x]
            return x + len_arr1

        arr1.sort(key = relativeSort)
        return arr1
