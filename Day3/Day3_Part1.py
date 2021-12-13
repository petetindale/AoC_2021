def get_binary_diagnostic(list_of_strings):
    list_of_binaries = list(map(lambda x : list(map(int, x.strip())), list_of_strings))
    number_of_binary_words = len(list_of_binaries)
    length_of_binary_word = len(list_of_binaries[0])

    print(list_of_binaries)
    return 0


#test
get_binary_diagnostic(
    ["00100\n",
    "11110\n",
    "10110\n",
    "10111\n",
    "10101\n",
    "01111\n",
    "00111\n",
    "11100\n",
    "10000\n",
    "11001\n",
    "00010\n",
    "01010\n"])