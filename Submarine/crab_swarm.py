import numpy as np
import statistics as sts
import functools as fn

from numpy.lib.function_base import median

test_list_of_strings = ["16,1,2,0,4,2,7,1,2,14\n"]

def calculate_fuel_consumed(list_of_crabs:list, new_pos:int) -> int :
    return int(fn.reduce(lambda sm, pos: sm + abs(new_pos-pos), list_of_crabs, 0))

def calculate_fuel_consumed_weighted(list_of_crabs:list, new_pos:int) -> int :
    return int(fn.reduce(lambda sm, pos: sm + (((abs(new_pos-pos)*abs(new_pos-pos))+abs(new_pos-pos))/2), list_of_crabs, 0))


def calculate_minimal_crab_moves(list_of_strings:list) -> int :
    list_of_crabs = list(map(lambda x : int(x), list_of_strings[0].split(",")))
    mode_position = sts.mode(list_of_crabs)
    median_postiion = int(sts.median(list_of_crabs))
    mean_position = sts.mean(list_of_crabs)

    prev_fuelconsumed = 0
    current_position = median_postiion
    current_fuelconsumed = calculate_fuel_consumed_weighted(list_of_crabs, current_position)
    prev_fuelconsumed = calculate_fuel_consumed_weighted(list_of_crabs, current_position-1)
    direction = -1 if prev_fuelconsumed < current_fuelconsumed else 1

    print(f"460 - {calculate_fuel_consumed_weighted(list_of_crabs, 460)}")
    print(f"464 - {calculate_fuel_consumed_weighted(list_of_crabs, 464)}")
    print(f"468 - {calculate_fuel_consumed_weighted(list_of_crabs, 468)}")


    while True :
        current_position += direction
        current_fuelconsumed = calculate_fuel_consumed_weighted(list_of_crabs, current_position)
        if prev_fuelconsumed < current_fuelconsumed :
            print(f"Best Position : {current_position-direction}")
            return prev_fuelconsumed
        else :
            prev_fuelconsumed = current_fuelconsumed

    return 0

def test_calculate_minimal_crab_moves() -> None :
    print(f"There are {calculate_minimal_crab_moves(test_list_of_strings)} crab moves")

#test_calculate_minimal_crab_moves()