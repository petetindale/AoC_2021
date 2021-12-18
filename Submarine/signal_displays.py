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


class SignalPatterns :
    def __init__(self, string:str) -> None:
        self.unique_signal_patterns = list(map(lambda x : x.strip(), string.split(" | ")[0].split(" ")))
        self.output_signal_patterns = list(map(lambda x : x.strip(), string.split(" | ")[1].split(" ")))
        pass
    def count_1_4_7_8_in_output(self) -> int :
        return int(fn.reduce(lambda count, string: count + (1 if (len(string) in (2,3,4,7)) else 0), self.output_signal_patterns, 0))


def find_signal_digits(list_of_strings:list) -> int :
    list_of_signals = list(map(lambda x : SignalPatterns(x), list_of_strings))
    return int(fn.reduce(lambda sum, signal: sum + signal.count_1_4_7_8_in_output(), list_of_signals, 0))


def test_find_signal_digits() -> None :
    print(f"There are {find_signal_digits(test_list_of_strings)} 1, 4, 7, 8")

#test_find_signal_digits()