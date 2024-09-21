"""
https://leetcode.com/problems/complex-number-multiplication/submissions/1397255466/
?envType=problem-list-v2&envId=string
"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        ind1 = 0
        ind2 = 0
        for i in range (0, len(num1)) :
            if num1[i] == "+" :
                ind1 = i
        for i in range (0, len(num2)) :
            if num2[i] == "+" :
                ind2 = i
        real1 = num1[:ind1]
        real2 = num2[:ind2]
        im1 = num1[ind1+1: len(num1) - 1]
        im2 = num2[ind2+1: len(num2) - 1]
        return str(int(real1)*int(real2)-int(im1)*int(im2)) + "+" + str(int(real1)*int(im2) + int(real2)*int(im1)) + "i"
        
