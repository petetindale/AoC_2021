import functools as fn
import statistics as sts

# Day 3 Part 1
def get_binary_diagnostic(list_of_strings):
    list_of_binaries = list(map(lambda x : list(map(int, x.strip())), list_of_strings))
    number_of_binary_words = len(list_of_binaries)
    length_of_binary_word = len(list_of_binaries[0])

    sum_binary_words = fn.reduce(lambda binary_word, binary_sum : list(map(lambda x,y : x + y, binary_word, binary_sum)), list_of_binaries, [0] * length_of_binary_word)

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


def get_recurse_diagnostic(list_of_binaries, position, word, least):
    if position < len(word) :
        list_of_bits = list(map(lambda x : x[position], list_of_binaries))
        count_ons = sum(list_of_bits, 0)
        
        if count_ons == len(list_of_bits) :
            word[position] = 1
        elif count_ons != 0 :
            word[position] = (1 if not least else 0) if count_ons >= len(list_of_bits)/2 else (0 if not least else 1)
        else :
            word[position] = 0
        
        filtered_list_of_binaries = list(filter(lambda x: (x[position]==word[position]), list_of_binaries))
        return get_recurse_diagnostic(filtered_list_of_binaries, (position+1), word, least)
    return word

    

# Day 3 Part 2
def get_oxy_co2_diagnostic(list_of_strings):
    list_of_binaries = list(map(lambda x : list(map(int, x.strip())), list_of_strings))
    number_of_binary_words = len(list_of_binaries)
    length_of_binary_word = len(list_of_binaries[0])

    oxygen_binary_list = get_recurse_diagnostic(list_of_binaries,0, [0] * length_of_binary_word, False)
    co2_binary_list = get_recurse_diagnostic(list_of_binaries,0, [0] * length_of_binary_word, True)

    oxygen = int(''.join(map(str, oxygen_binary_list)),2)
    co2 = int(''.join(map(str, co2_binary_list)),2)

    return oxygen * co2



def test_binary_diags() :
    #test
    test_list = ["00100\n",
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
        "01010\n"]

    print(get_binary_diagnostic(test_list))
    print(get_oxy_co2_diagnostic(test_list))


#test_binary_diags()