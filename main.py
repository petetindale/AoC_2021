from Common import file_importer
import Submarine as sb
from os import path

CurrentDay = "Day 3"

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
    print(sb.get_binary_diagnostic(list_of_strings))
    #Day 3 Part 2

