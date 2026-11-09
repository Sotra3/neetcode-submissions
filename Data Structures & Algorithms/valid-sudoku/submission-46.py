class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashMapRows = [{i: 0 for i in range(1, 10)} for _ in range(9)]    
        hashMapCollumns = [{i: 0 for i in range(1, 10)} for _ in range(9)]
        hashMapSquares = [{i: 0 for i in range(1, 10)} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    numberInRow=int(board[i][j])
                    hashMapRows[i][numberInRow]=hashMapRows[i].get(numberInRow,0)+1
                    hashMapSquares[((i//3)*3)+(j//3)][numberInRow]=hashMapSquares[((i//3)*3)+(j//3)].get(numberInRow,0)+1
                    if hashMapRows[i].get(numberInRow,0)>1 or hashMapSquares[((i//3)*3)+(j//3)].get(numberInRow,0)>1:
                        return False;

                if board[j][i]!='.':
                    numberInCollumn=int(board[j][i])
                    hashMapCollumns[i]               [numberInCollumn]=hashMapCollumns[i].get(numberInCollumn,0)+1   
                    if hashMapCollumns[i].get(numberInCollumn,0)>1:
                        return False;                
        
        print(hashMapRows)
        print("\n\n")
        print(hashMapCollumns)
        return True    