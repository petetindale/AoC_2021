test_list_of_strings = [
    "[1,2]\n"
    ,"[[1,2],3]\n"
    ,"[9,[8,7]]\n"
    ,"[[1,9],[8,5]]\n"
    ,"[[[[1,2],[3,4]],[[5,6],[7,8]]],9]\n"
    ,"[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]\n"
    ,"[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]\n"
]

def final_sum_magnitude(list_of_strings:list)->int:
    return 0

def test_final_sum_magnitude()->None:
    print(f'TEST - Final Sum Magnitude = {final_sum_magnitude(test_list_of_strings)}')
    print('ASSERT - FSM = 4140')

test_final_sum_magnitude()