"""
https://leetcode.com/problems/design-excel-sum-formula/

This is very interesting lol...
How to represent the excel sheet so that sum() is fast?
"Update" sum when set() OR represent sum as a list of cells can calculate sum() "on the fly"
Adjacency list
{"B3": 2}
{"B3": ["A1", "F7", ...]}

"""
class Excel:
    def __init__(self, height: int, width: str):
        self.grid = {}
        for i in range(1,height+1):
            for j in range(ord(width)-ord('A')+1):
                self.grid[chr(ord('A')+j)+str(i)] = 0

    def set(self, row: int, column: str, val: int) -> None:
        self.grid[column + str(row)] = val

    def get(self, row: int, column: str) -> int:
        if not isinstance(self.grid[column + str(row)], list):
            return self.grid[column + str(row)]
        currSum = 0
        for cell in self.grid[column + str(row)]:
            currSum += self.get(cell[1:], cell[0])
        return currSum

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.grid[column + str(row)] = self.getCells(numbers)
        return self.get(row, column)
    
    def getCells(self, numbers):
        cells = []
        for number in numbers:
            if ":" in number:
                start = number.split(":")[0]
                end = number.split(":")[1]
                for row in range(int(start[1:]), int(end[1:])+1):
                    for col in range(ord(start[0]), ord(end[0])+1):
                        cells.append(chr(col)+str(row))
            else:
                cells.append(number)
        return cells
                


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)