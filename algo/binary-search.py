

# empty list error

# def locate_card(cards, query):
#     position = 0
#     while True:
#         if cards[position] == query:
#             return position
#         position += 1
#         if position == len(cards):
#             return -1


# solve empty array 

def locate_card(cards, query):
    low=0 
    high=len(cards)-1
    while low<=high:
        mid=(low+high)//2
        mid_card=cards[mid]
        print(low,high,mid,mid_card)
        if cards[mid]==query:
            return mid
        elif cards[mid]<query:
            low=mid+1
        else:
            high=mid-1
    return -1
print(locate_card([1,2,3,4,5,6,7,8,9,10,
                   11,12,13,14,15,
                   16,17,18,
                   19,20],19))


import unittest
def binary_search(L,x):
    left, right = 0, len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            left = mid + 1
        else:
            return mid-1
    return -1

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self): 
        # self.assertEqual(locate_card([], 3), -1)
        self.assertEqual(locate_card([1, 2], 3), -1)
        self.assertEqual(locate_card([1, 2, 3, 4], 3), 2)
        self.assertEqual(locate_card([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(locate_card([1, 2, 3, 4], 3), 2)
        self.assertEqual(locate_card([1, 2, 3, 4], 1), 0)
        self.assertEqual(locate_card([1, 2, 3, 4], 4), 3)
    
if __name__=='__main__':
    unittest.main()

