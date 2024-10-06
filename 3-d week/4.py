"""
https://leetcode.com/problems/sentence-similarity-iii/description/
?envType=daily-question&envId=2024-10-06
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        arr1 = sentence1.split(" ")
        arr2 = sentence2.split(" ")
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        start = 0
        finish1 = len(arr1) - 1
        finish2 = len(arr2) - 1
        while start < finish1 + 1 and arr1[start] == arr2[start]:
            start += 1
        while finish1 >= 0 and arr1[finish1] == arr2[finish2]:
            finish1 -= 1
            finish2 -= 1
        return finish1 < start
