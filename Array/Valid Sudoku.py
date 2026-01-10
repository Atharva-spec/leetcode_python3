class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create hash sets to store numbers we've seen in each row, col, and box
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set) # Key will be (row_chunk, col_chunk) e.g., (0,1)

        for c in range(9):
            for r in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue
                
                # Check if the number already exists in the current:
                # 1. Row 'r'
                # 2. Col 'c'
                # 3. 3x3 Box (identified by r//3, c//3)
                if ( board[r][c] in rows[r] or
                     board[r][c] in cols[c] or
                     board[r][c] in square[(r // 3, c // 3)]):
                    return False # Found a duplicate, so it's invalid

                # If not a duplicate, add number to sets to remember it
                cols[c].add(board[r][c])  
                rows[r].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])          
        
        return True # If no duplicates found after checking all, it's valid