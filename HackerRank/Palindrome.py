import sys
from collections import deque

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque()
    
    
    def pushCharacter(self, charIncomming):
        self.stack.append(charIncomming)
    
    
    def enqueueCharacter(self, charIncomming):
        self.queue.append(charIncomming)
    

    def popCharacter(self, charIncomming):
        return self.stack.pop()

    
    def dequeueCharacter(self):
        return self.queue.popleft()

# read the string s
s="121"
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter(i)!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    