
def get_list_of_strings(input_path, input_filename):
    #Load file information
    f = open(input_path + input_filename, "r")
    list_of_strings = f.readlines()
    f.close()
    return list_of_strings