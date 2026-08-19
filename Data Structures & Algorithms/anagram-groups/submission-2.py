class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        count = []
        ans = []
        group_indices = {}
        list1 = []

        for index,value in enumerate(strs):
            temp = "".join(sorted(value))
            result[index] = temp
            count.append(temp)

        for index,value in result.items():
            if value not in group_indices:
                group_indices[value] = []
            group_indices[value].append(strs[index])
        for key,value in group_indices.items():
            list1.append(value)
        return list1




        


            


        
            


        