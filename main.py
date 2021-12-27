from Common import file_importer
import Submarine as sb
from os import path

CurrentDay = "Day 11"

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

if CurrentDay == "Day 7" or CurrentDay == "All" : 
    #Day 7
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "crab_position_day7.txt")

    #Day 6 Part 1
    print(f"Crab fuel used {sb.calculate_minimal_crab_moves(list_of_strings)}")

if CurrentDay == "Day 8" or CurrentDay == "All" : 
    #Day 8
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "signals_day8.txt")

    #Day 8 Part 1
    #print(f"Found unique patterns in output {sb.find_signal_digits(list_of_strings)}")

    #Day 8 Part 2
    print(f"Sum of output {sb.sum_signal_output(list_of_strings)}")

if CurrentDay == "Day 9" or CurrentDay == "All" : 
    #Day 9
    list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "smoke_basin_day9.txt")

    #Day 9 Part 1
    print(f"Sum of Risk Level = {sb.find_low_points(list_of_strings)}")

    #Day 9 Part 2
    print(f"Product of 3 largest basins = {sb.find_largest_basins(list_of_strings)}")
    #print(f"Sum of output {sb.sum_signal_output(list_of_strings)}")
    

if CurrentDay == "Day 10" or CurrentDay == "All" : 
		#Day 10
		list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "syntax_day10.txt")

		#Day 9 Part 1
		print(f"Corrupted line score = {sb.find_corrupted_lines(list_of_strings)}")

    #Day 9 Part 2
		print(f"Complete lines score = {sb.complete_lines(list_of_strings)}")
    #print(f"Sum of output {sb.sum_signal_output(list_of_strings)}")
    
if CurrentDay == "Day 11" or CurrentDay == "All" : 
		#Day 10
		list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/Inputs/"), "dumbo_octo_day11.txt")

		#Day 9 Part 1
		print(f"Octopus flashes = {sb.count_flashes(list_of_strings, 500)}")

    #Day 9 Part 2
		#print(f"Complete lines score = {sb.complete_lines(list_of_strings)}")
    
