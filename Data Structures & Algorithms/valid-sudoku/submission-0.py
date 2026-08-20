class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            dict1 = {}
            for j in range(9):

                value = board[i][j]
                if value != ".":
                    dict1[value] = dict1.get(value,0)+1
            for key,value in dict1.items():
                if value == 2:
                    return False


        for i in range(9):
            dict2 = {}
            for j in range(len(board)):

                value = board[j][i]
                if value != ".":
                    dict2[value] = dict2.get(value,0)+1
            for key,value in dict2.items():
                    if value == 2:
                        return False

        for i in range(9):
            dict3 = {}
            for j in range(9):

                r = (i//3)*3 + (j//3)
                c = (i%3)*3 + (j%3)
                value = board[r][c]
                if value != ".":
                    dict3[value] = dict3.get(value,0)+1
            for key,value in dict3.items():
                    if value == 2:
                        return False

        return True
                


            

        


        