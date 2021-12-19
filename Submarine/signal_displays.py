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
    
    #Unique Length Matching
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

    #Matching with ULM Patterns
    @classmethod
    def is_2(cls, binary_int:int, signal4_int:int) -> bool :
        if Signal_Match.get_ons(binary_int)==Signal_Match.LEN_2 :
            not_4 = signal4_int ^ Signal_Match.BITMASK
            if binary_int == binary_int | not_4 :
                return True
        return False

    @classmethod
    def is_5(cls, binary_int:int, signal1_int:int, signal4_int:int) -> bool :
        if Signal_Match.get_ons(binary_int)==Signal_Match.LEN_5 :
            if binary_int == (binary_int | (signal4_int - signal1_int)) :
                return True
        return False

    @classmethod
    def is_6(cls, binary_int:int, signal7_int:int) -> bool :
        if Signal_Match.get_ons(binary_int)==Signal_Match.LEN_6 :
            not_7 = signal7_int ^ Signal_Match.BITMASK
            if binary_int == binary_int | not_7 :
                return True
        return False
    
    @classmethod
    def is_9(cls, binary_int:int, signal4_int:int) -> bool :
        if Signal_Match.get_ons(binary_int)==Signal_Match.LEN_9 :
            if binary_int == binary_int | signal4_int :
                return True
        return False
    
    @classmethod
    def is_0(cls, binary_int:int, signal1_int:int, signal4_int:int, signal8_int:int) -> bool :
        if Signal_Match.get_ons(binary_int)==Signal_Match.LEN_0 :
            if binary_int == (binary_int | (signal8_int - signal4_int + signal1_int)) :
                return True
        return False


    @classmethod
    def is_3(cls, binary_int:int, signal1_int:int, signal2_int:int, signal5_int:int) -> bool :
        if Signal_Match.get_ons(binary_int)==Signal_Match.LEN_3 :
            if binary_int == (binary_int | (signal1_int + (signal2_int & signal5_int))) :
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
        self.output = self.match_output_signals()
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
            if (Signal_Match.is_2(i, self.ordered_unique_signal_patterns[4])) :   
                self.ordered_unique_signal_patterns[2] = i
            elif (Signal_Match.is_5(i, self.ordered_unique_signal_patterns[1], self.ordered_unique_signal_patterns[4])) :   
                self.ordered_unique_signal_patterns[5] = i
            elif (Signal_Match.is_6(i, self.ordered_unique_signal_patterns[7])) :   
                self.ordered_unique_signal_patterns[6] = i
            elif (Signal_Match.is_9(i, self.ordered_unique_signal_patterns[4])) :   
                self.ordered_unique_signal_patterns[9] = i
            elif (Signal_Match.is_0(i, self.ordered_unique_signal_patterns[1], self.ordered_unique_signal_patterns[4], self.ordered_unique_signal_patterns[8])) : 
                self.ordered_unique_signal_patterns[0] = i  
        for i in filter(lambda x : Signal_Match.get_ons(x) == Signal_Match.LEN_3, self.unique_signal_patterns_binary) :
            if (Signal_Match.is_3(i, self.ordered_unique_signal_patterns[1], self.ordered_unique_signal_patterns[2], self.ordered_unique_signal_patterns[5])) :   
                self.ordered_unique_signal_patterns[3] = i

    def match_output_signal(self, signal:int) -> int :
        for i in range(10) :
            if signal == self.ordered_unique_signal_patterns[i] : return i
        return 0


    def match_output_signals(self) -> int :
        output_answers = list()
        for i in self.output_signal_patterns_binary :
            output_answers.append(self.match_output_signal(i))
        return int(fn.reduce(lambda string, signal: f"{string}{signal}", output_answers, "")) 

def find_signal_digits(list_of_strings:list) -> int :
    list_of_signals = list(map(lambda x : SignalPatterns(x), list_of_strings))
    
    return int(fn.reduce(lambda sum, signal: sum + signal.count_1_4_7_8_in_output(), list_of_signals, 0))

def sum_signal_output(list_of_strings:list) -> int :
    list_of_signals = list(map(lambda x : SignalPatterns(x), list_of_strings))
    return int(fn.reduce(lambda sum, signal: sum + signal.output, list_of_signals, 0))

def test_find_signal_digits() -> None :
    print(f"There are {find_signal_digits(test_list_of_strings)} in 1, 4, 7, 8")

def test_sum_signal_output() -> None :
    print(f"Sum of {sum_signal_output(test_list_of_strings)}")

#test_sum_signal_output()