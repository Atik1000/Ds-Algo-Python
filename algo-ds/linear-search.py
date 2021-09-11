def locate_card(card, query):
    i = 0
    while i < len(card):    # while True when used have an  error when empty card list
        print(i, '===i')
        if card[i] == query:
            return i
        i += 1
    return -1
print(locate_card([1,2,8,10],10))



#     for i in range(len(card)):
#         if card[i] == query:
#             return i
#     return -1
# print(locate_card([1,2,3,4,5,6,7,8,9,10],11))