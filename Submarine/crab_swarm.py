import numpy as np
import statistics as sts
import functools as fn

from numpy.lib.function_base import median

test_list_of_strings = ["16,1,2,0,4,2,7,1,2,14\n"]

def calculate_fuel_consumed(list_of_crabs:list, new_pos:int) -> int :
    return int(fn.reduce(lambda sm, pos: sm + abs(new_pos-pos), list_of_crabs, 0))


def calculate_minimal_crab_moves(list_of_strings:list) -> int :
    list_of_crabs = list(map(lambda x : int(x), list_of_strings[0].split(",")))
    mode_position = sts.mode(list_of_crabs)
    median_postiion = sts.median(list_of_crabs)
    mean_position = sts.mean(list_of_crabs)
    print(f"Mode: {mode_position} - Fuel: {calculate_fuel_consumed(list_of_crabs, mode_position)}")
    print(f"Mean: {mean_position} - Fuel: {calculate_fuel_consumed(list_of_crabs, mean_position)}")
    
    print(f"Median-10: {median_postiion-10} - Fuel: {calculate_fuel_consumed(list_of_crabs, (median_postiion-10))}")
    print(f"Median-1: {median_postiion-1} - Fuel: {calculate_fuel_consumed(list_of_crabs, (median_postiion-1))}")
    print(f"Median: {median_postiion} - Fuel: {calculate_fuel_consumed(list_of_crabs, median_postiion)}")
    print(f"Median+1: {median_postiion+1} - Fuel: {calculate_fuel_consumed(list_of_crabs, (median_postiion+1))}")
    print(f"Median+10: {median_postiion+10} - Fuel: {calculate_fuel_consumed(list_of_crabs, (median_postiion+10))}")

    return sum(list_of_crabs)

def test_calculate_minimal_crab_moves() -> None :
    print(f"There are {calculate_minimal_crab_moves(test_list_of_strings)} crab moves")

test_calculate_minimal_crab_moves()