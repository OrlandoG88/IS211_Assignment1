def listDivide(numbers, divide=2):
    Count = 0
    for x in numbers:
      if x % divide == 0:
        Count += 1
    return Count



class ListDivideException(Exception):
    pass


def testListDivide():
    try:
        if not listDivide([1, 2, 3, 4, 5]) == 2:
            raise ListDivideException
        elif not listDivide([2, 4, 6, 8, 10]) == 5:
            raise ListDivideException
        elif not listDivide([30, 54, 63, 98, 100], divide=10) == 2:
            raise ListDivideException
        elif not listDivide([]) == 0:
            raise ListDivideException
        elif not listDivide([1, 2, 3, 4, 5], 1) == 5:
            raise ListDivideException
        print("No errors")
    except ListDivideException:
        print("Error")

testListDivide()