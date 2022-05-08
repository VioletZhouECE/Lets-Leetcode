"""
Good question!

https://leetcode.com/problems/flatten-nested-list-iterator/

Can we flatten it the list in the pre-processing step?
Yes we can...and it's not bad tbh...

Any better/fancier/one-pass solution?
We flatten the array until we see a number, and we store numbers in the flattened array into a stack so that they can be used in future iterations.
stack -> recursion: we kinda wanna dfs into a nested list till we find a number.

Can we just use recursion? No! It's kinda difficult to write a recursive function that dfs into a nested list, if the nested list does not return a number, go to the next index, and do this until we find a number (I tried that :((. Also, pushing and popping numbers is more natural with a stack (with recursion, you probably need to do list.pop(0))
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        self.prepareStack(nestedList)
        
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while len(self.stack)>0 and not NestedInteger.isInteger(self.stack[-1]):
            self.prepareStack(self.stack.pop().getList())
        if len(self.stack)==0:
            return False
        return True
    
    def prepareStack(self, l):
        #this guarantees that we process numbers in order even though we are working with stack
        for x in l[::-1]:
            self.stack.append(x)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())