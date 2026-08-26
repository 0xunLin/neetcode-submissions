import collections

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # Check rows 
#         for r in range(9):
#             seen = set()
#             for c in range(9):
#                 val = board[r][c]
#                 if val != ".":
#                     if val in seen: return False
#                     seen.add(val)
#         # Check columns
#         for c in range(9):
#             seen = set()
#             for r in range(9):
#                 val = board[r][c]
#                 if val != ".":
#                     if val in seen: return False
#                     seen.add(val)
#         # Check 3x3 boxes
#         for box_r in range(0, 9, 3):
#             for box_c in range(0, 9, 3):
#                 seen = set()
#                 for r in range(3):
#                     for c in range(3):
#                         val = board[box_r + r][box_c + c]
#                         if val != ".":
#                             if val in seen: return False
#                             seen.add(val)
#         return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = collections.defaultdict(set)
#         columns = collections.defaultdict(set)
#         boxes = collections.defaultdict(set)
#         for r in range(9):
#             for c in range(9):
#                 val = board[r][c]
#                 if val == ".":
#                     continue
#                 box_key = (r // 3, c // 3)
#                 if (val in rows[r] or
#                     val in columns[c] or
#                     val in boxes[box_key]
#                     ):
#                     return False
#                 rows[r].add(val)
#                 columns[c].add(val)
#                 boxes[box_key].add(val)
#         return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                pos = 1 << int(val)
                box_index = (r // 3) * 3 + (c // 3)
                if (
                    rows[r] & pos or
                    columns[c] & pos or
                    boxes[box_index] & pos
                ):
                    return False
                rows[r] |= pos
                columns[c] |= pos
                boxes[box_index] |= pos
        return True