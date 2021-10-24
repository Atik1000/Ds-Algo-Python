def avarage(L):
    if not L:
        return None
    return sum(L)/len(L)

def avarage(L):
    if not L:
        return None
    return sum(L)/len(L)


# if __name__=="__main__":
#     L=[1,2,3,4,5,6,7,8,9,10]
#     print(avarage(L))


# if __name__=='__main__':
#     L=[1,2,3,4,5,6,7,8,9,10]
#     expected=5.5
#     assert expected==avarage(L), "The avarage should be %s" % expected
#     print("The avarage is %s" % avarage(L))

def test_avarage():
    test_case=[
        {
            "name": "sample test 1",
            "input": [1,2,3,4,5,6,7,8,9,10],
            "expected":5.5
            
        },
        {
            "name": "sample test 2",
            "input": [1,2,3,4,5],
            "expected":3.0
        },
        {
            "name": "sample test 3",
            "input": [],
            "expected":None
        }, {
            "name":"sample test 4",
            "input": [100],
            "expected":100
        }
    ]
    for test_case in test_case:
        assert test_case["expected"]==avarage(test_case["input"]),test_case["name"]