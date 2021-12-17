test_list_of_strings = ["16,1,2,0,4,2,7,1,2,14\n"]

def calculate_minimal_crab_moves(list_of_strings:list) -> int :
    list_of_crabs = list(map(lambda x : int(x), list_of_strings[0].split(",")))
    
    
    return sum(list_of_crabs)

def test_calculate_minimal_crab_moves() -> None :
    print(f"There are {calculate_minimal_crab_moves(test_list_of_strings)} crab moves")

test_calculate_minimal_crab_moves()