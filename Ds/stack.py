# # check complexity of the code
# n=int(input())
# count=0
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#                 count+=1
# print('n=',n,'count=',count)
# # complexity is O(n^3)


n=int(input())
count=0
for i in range(n):
    count+=1

for i in range(n):
    for j in range(n):
        count+=1

print('n=',n,'count=',count)
# complexity is O(n^2)