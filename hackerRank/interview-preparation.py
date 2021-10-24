# 1 Socket Merchant

# def sockMerchant(n, arr):
#         count=0
#         d={}
#         for i in arr:
#                 if i in d:
#                         d[i]+=1
#                 else:
#                         d[i]=1
#         for i in d:
#                 count+=d[i]//2
#         return count
# n=int(input())
# arr= list(map(int, input().split()))
# print(sockMerchant(n, arr))


# import math
# import os
# import random
# import re 
# import sys

# from collections import Counter
# def sockMerchant(n, ar):
#     s=0
#     for val in Counter(ar).values():
#         s+=val//2
#     return s


# if __name__ == '__main__':
#   fptr=open(os.environ['OUTPUT_PATH'], 'w')
  
#   n=int(input())
#   ar= list(map(int, input().rstrip().split()))
#   result= sockMerchant(n, ar)
#   fptr.write(str(result) + '\n')
#   fptr.close()
