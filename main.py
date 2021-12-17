from Common import file_importer
import Submarine as sb
from os import path

CurrentDay = "Day 6"

if CurrentDay == "Day 1" or CurrentDay == "All" : 
    #Day 1
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "depths_day1.txt")

    #Day 1 Part 1
    print(sb.measure_depth(list_of_strings))
    #Day 1 Part 2
    print(sb.measure_threes_depth(list_of_strings))

if CurrentDay == "Day 2" or CurrentDay == "All" : 
    #Day 2
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "instructions_day2.txt")

    #Day 2 Part 1
    print(sb.move_with_instructions(list_of_strings))
    #Day 2 Part 2
    print(sb.move_with_aim_and_depth(list_of_strings))

if CurrentDay == "Day 3" or CurrentDay == "All" : 
    #Day 3
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "binaries_day3.txt")

    #Day 3 Part 1
    print(f"binary diagnostics {sb.get_binary_diagnostic(list_of_strings)}")
    #Day 3 Part 2
    print(f"oxy * co2 = {sb.get_oxy_co2_diagnostic(list_of_strings)}")

if CurrentDay == "Day 4" or CurrentDay == "All" : 
    #Day 4
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "bingo_boards_day4.txt")

    #Day 4 Part 1
    print(f"Winning Squid Board {sb.play_squid_bingo(list_of_strings, True)}")
    #Day 4 Part 2
    print(f"Losing Squid Board {sb.play_squid_bingo(list_of_strings, False)}")

if CurrentDay == "Day 5" or CurrentDay == "All" : 
    #Day 5
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "hydrothermal_vents_day5.txt")

    #Day 5 Part 1
    print(f"Overlapping Vents {sb.find_overlapping_vents(list_of_strings, False, 1000)}")

if CurrentDay == "Day 6" or CurrentDay == "All" : 
    #Day 6
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "lanterfish_observations_day6.txt")

    #Day 6 Part 1
    print(f"Population of lanterfish {sb.lanternfish_population_counter(list_of_strings, 256)}")

