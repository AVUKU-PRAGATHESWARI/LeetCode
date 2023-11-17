class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        ext = [i for i in arr1 if i not in arr2]
        ext.sort()
        for i in arr2:
            if i in arr1:
                cou = arr1.count(i)
                new = [i]*cou
                res.extend(new)
        res.extend(ext)
        return res
        

# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         arr12 = []
#         arr = []
#         arr1 = Counter(arr1)
#         for i in arr2:
#             arr12+=[i]*arr1[i]
#         for i in arr1:
#             if i not in arr2:
#                 arr+=[i]*arr1[i]
#         return arr12+sorted(arr)