import unittest

def locate_card(card, query):
    i = 0
    while i < len(card):    # while True when used have an  error when empty card list
        print(i, '===i')
        if card[i] == query:
            return i
        i += 1
    return -1
print(locate_card([1,2,8.0,12,13,14,15,10],10))


# Test cases for binary search
class TestBinarySearch(unittest.TestCase):
    
    def test_binary_search(self): 
        self.assertEqual(locate_card([], 3), -1)
        self.assertEqual(locate_card([1, 2], 3), -1)
        self.assertEqual(locate_card([1, 2, 3, 4], 3), 2)
        self.assertEqual(locate_card([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(locate_card([1, 2, 3, 4,3,3], 3), 2)
        self.assertEqual(locate_card([1, 2, 3, 4], 1), 0)
        self.assertEqual(locate_card([1, 2, 3, 4], 4), 3)
    
if __name__=='__main__':
    unittest.main()



#     for i in range(len(card)):
#         if card[i] == query:
#             return i
#     return -1
# print(locate_card([1,2,3,4,5,6,7,8,9,10],11))



