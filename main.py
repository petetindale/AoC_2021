from Common import file_importer
from Day3 import Day3_Part1
from os import path

CurrentDay = "Day3"

list_of_strings = file_importer.get_list_of_strings(path.dirname(__file__) + ("/"+ CurrentDay +"/"), "list.txt")


print(Day3_Part1.get_binary_diagnostic(list_of_strings))

