from functools import reduce
import statistics

# Day 3 Part 1
def get_binary_diagnostic(list_of_strings):
    list_of_binaries = list(map(lambda x : list(map(int, x.strip())), list_of_strings))
    number_of_binary_words = len(list_of_binaries)
    length_of_binary_word = len(list_of_binaries[0])

    sum_binary_words = reduce(lambda binary_word, binary_sum : list(map(lambda x,y : x + y, binary_word, binary_sum)), list_of_binaries, [0] * length_of_binary_word)

    gamma_binary_list = list(map(lambda x : 1 if x > number_of_binary_words/2 else 0, sum_binary_words))
    epsilon_binary_list = list(map(lambda x : 0 if x > number_of_binary_words/2 else 1, sum_binary_words))

    print(gamma_binary_list)
    print(epsilon_binary_list)

    gamma_binary = int(''.join(map(str, gamma_binary_list)),2)
    epsilon_binary = int(''.join(map(str, epsilon_binary_list)),2)

    print(sum_binary_words)
    print(gamma_binary)
    print(epsilon_binary)

    return gamma_binary * epsilon_binary


#test
""" get_binary_diagnostic(
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
    "01010\n"]) """