from day2.part2 import safe
import pytest

@pytest.mark.parametrize("test_input,assert_true", 
                          [([63, 65, 66, 67, 68, 71, 74, 76], True),
                          ([85, 88, 90, 92, 95, 98], True),
                          ([75, 73, 70, 67, 66], True),
                          ([91, 89, 87, 85, 82, 79, 77, 74], True),
                          ([33, 32, 30, 27, 26, 24, 21, 20], True),
                          ([88, 85, 82, 79, 76, 74, 73, 71], True),
                          ([31, 33, 34, 35, 38, 41, 42, 43], True),
                          ([10, 11, 12, 15, 17, 20, 21], True),
                          ([8 ,10 ,13 ,14 ,17, 18], True),
                          ([78, 77, 74, 73, 70], True),
                          ([8 ,10 ,12 ,13 ,15], True),
                          ([47, 46, 43, 42, 40], True),
                          ([94, 91, 90, 89, 88, 85, 84, 83], True),
                          ([41, 43, 45, 46, 48], True),
                          ([65, 66, 67, 68, 69, 72, 75], True),
                          ([97, 95, 94, 92, 91, 89], True),
                          ([68, 71, 73, 75, 78], True),
                          ([35, 37, 40, 42, 44], True)])
def test_input(test_input, assert_true):
    assert safe(test_input) == assert_true
