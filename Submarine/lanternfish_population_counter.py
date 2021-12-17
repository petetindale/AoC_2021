test_list_of_strings = ["3,4,3,1,2\n"]

def lanterfish_age_population_by_one_day(list_of_laternfish:list) -> list :
    #decrement age
    next_day_population = list(map(lambda x : x-1, list_of_laternfish))
    
    #add children
    for laternfish in list(filter(lambda x: x < 0, next_day_population)) :
        next_day_population.append(8)
    
    #decrement age
    next_day_population = list(map(lambda x : x if x > -1 else 6, next_day_population))

    return next_day_population


def lanternfish_population_counter(list_of_strings:list, days:int) -> int :
    list_of_lanternfish = list(map(lambda x : int(x), list_of_strings[0].split(",")))
    i = 0
    while i < days :
        list_of_lanternfish = lanterfish_age_population_by_one_day(list_of_lanternfish)
        i += 1
    return len(list_of_lanternfish)

def test_lanternfish_population_counter() -> None :
    print(f"There are {lanternfish_population_counter(test_list_of_strings, 80)} lanternfish")

test_lanternfish_population_counter()