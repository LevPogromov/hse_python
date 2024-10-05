"""
https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
?envType=daily-question&envId=2024-10-02
"""


class CustomStack:
    def __init__(self, maxSize: int):
        self.st = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.st) < self.max_size:
            self.st.append(x)

    def pop(self) -> int:
        if len(self.st) == 0:
            return -1
        else:
            needed = self.st[-1]
            self.st.pop()
            return needed

    def increment(self, k: int, val: int) -> None:
        if k > len(self.st):
            for i in range(0, len(self.st)):
                self.st[i] += val
        else:
            for i in range(0, k):
                self.st[i] += val
