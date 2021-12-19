import functools as fn

test_list_of_strings = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\n",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\n",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\n",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\n",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\n",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\n"]

class Signal_Match :
    LEN_0, LEN_1, LEN_2, LEN_3, LEN_4 = 6, 2, 5, 5, 4
    LEN_5, LEN_6, LEN_7, LEN_8, LEN_9 = 5, 6, 3, 7, 6
    
    BITMASK = 127

    @classmethod
    def get_ons(cls, binary_int:int) -> int :
        return bin(binary_int).count('1')
    
    @classmethod
    def is_1(cls, binary_int:int) -> bool :
        return (Signal_Match.get_ons(binary_int)==Signal_Match.LEN_1)
    @classmethod
    def is_4(cls, binary_int:int) -> bool :
        return (Signal_Match.get_ons(binary_int)==Signal_Match.LEN_4)
    @classmethod
    def is_7(cls, binary_int:int) -> bool :
        return (Signal_Match.get_ons(binary_int)==Signal_Match.LEN_7)
    @classmethod
    def is_8(cls, binary_int:int) -> bool :
        return (Signal_Match.get_ons(binary_int)==Signal_Match.LEN_8)

    @classmethod
    def is_2(cls, binary_int:int, signal4_int:int) -> bool :
        if Signal_Match.get_ons(binary_int)==Signal_Match.LEN_2 :
            not_4 = signal4_int ^ Signal_Match.BITMASK
            if binary_int == binary_int | not_4 :
                return True
        return False


    @classmethod
    def convert_string_to_bit_position(self, string_signal:str) -> int :
        binary_rep = int('00000000', 2)
        for char in list(string_signal):
            if char == 'a' :   binary_rep = binary_rep | int('00000001',2)
            elif char == 'b' : binary_rep = binary_rep | int('00000010',2)
            elif char == 'c' : binary_rep = binary_rep | int('00000100',2)
            elif char == 'd' : binary_rep = binary_rep | int('00001000',2)
            elif char == 'e' : binary_rep = binary_rep | int('00010000',2)
            elif char == 'f' : binary_rep = binary_rep | int('00100000',2)
            elif char == 'g' : binary_rep = binary_rep | int('01000000',2)
        return binary_rep
    

class SignalPatterns :

    
    def __init__(self, string:str) -> None:
        self.unique_signal_patterns = list(map(lambda x : x.strip(), string.split(" | ")[0].split(" ")))
        self.output_signal_patterns = list(map(lambda x : x.strip(), string.split(" | ")[1].split(" ")))
        self.unique_signal_patterns_binary = list(map(lambda string : Signal_Match.convert_string_to_bit_position(string), self.unique_signal_patterns))
        self.output_signal_patterns_binary = list(map(lambda string : Signal_Match.convert_string_to_bit_position(string), self.output_signal_patterns))
        self.ordered_unique_signal_patterns = [0]*10
        self.match_unique_signals()
        
        pass

    def count_1_4_7_8_in_output(self) -> int :
        return int(fn.reduce(lambda count, string: count + (1 if (len(string) in \
            (Signal_Match.LEN_1,Signal_Match.LEN_4,Signal_Match.LEN_7,Signal_Match.LEN_8)) \
                else 0), self.output_signal_patterns, 0))
    
    def match_unique_signals(self) -> None :
        for i in self.unique_signal_patterns_binary :
            if (Signal_Match.is_1(i)) :   self.ordered_unique_signal_patterns[1] = i
            elif (Signal_Match.is_4(i)) : self.ordered_unique_signal_patterns[4] = i
            elif (Signal_Match.is_7(i)) : self.ordered_unique_signal_patterns[7] = i
            elif (Signal_Match.is_8(i)) : self.ordered_unique_signal_patterns[8] = i        
        for i in self.unique_signal_patterns_binary :
            if (Signal_Match.is_2(i, self.ordered_unique_signal_patterns[4])) :   self.ordered_unique_signal_patterns[2] = i
        count = 0

            




def find_signal_digits(list_of_strings:list) -> int :
    list_of_signals = list(map(lambda x : SignalPatterns(x), list_of_strings))
    return int(fn.reduce(lambda sum, signal: sum + signal.count_1_4_7_8_in_output(), list_of_signals, 0))


def test_find_signal_digits() -> None :
    print(f"There are {find_signal_digits(test_list_of_strings)} in 1, 4, 7, 8")

test_find_signal_digits()