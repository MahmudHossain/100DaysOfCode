import math
import os
import random
import re
import sys
def repeatedString(s, n):
    str_len=len(s)
    t=n//str_len*s.count('a')
    rr=sum([1 for x in range(n%len(s)) if s[x]=="a"])
    print(rr)
    return rr+t
if __name__ == '__main__':
    

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)
