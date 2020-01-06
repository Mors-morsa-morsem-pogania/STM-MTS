# Tu będzie kod do kodowania i odkodywania oraz słownik (lub graf) z morsem

def load_csv(filename):
    """
    Loads content of CSV file into a dictionary.
    :param filename: CSV file path
    :return: dictionary [wav_filename]->label
    """
    import csv
    results_dict = dict()
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            results_dict[str(row[0])] = str(row[1])
    return results_dict


AlfabetMorsa = load_csv(filename="alfabetmorsa.csv")


def TTM(textfile, morse_dictionary=AlfabetMorsa):
    """
    Text to Morse
    :param textfile: string containing text to translate
    :param morse_dictionary: Dictionary variable containing Morse's signs written in binary system
    :return: 
    """
    # plik = open(plikztekstem, 'r+')
    # mors = plik.readline()
    mors = textfile
    word = ""
    if str(mors).isalnum() == True:
        print(mors)
        for i in range(0, len(mors)):
            word = word + str(morse_dictionary[mors[i]]) + str("|")
        print(word)
        word = word.replace("1", '.')
        word = word.replace("0", '_ ')
        print(word)
    else:
        word = "ERROR"
        print(word)
    #plik.close()


# TTM("TTM.txt", alfabetmorsa)


def morse_to_text(textfile_name="output_from_MTT.txt", morse_dict=AlfabetMorsa):
    """
    Morse to Text
    :param textfile_name: Name of txt file in which the output will appear
    :param morse_dict: Dictionary variable containing Morse's signs written in binary system
    :return:
    """
    file = open(textfile_name, 'r+')
    text = file.readline()
    print(text)
    text = text.replace(".", '1')
    text = text.replace("_ ", '0')
    text = text.split("|")
    print(text)
    word = ""
    for dl in range(0, len(text)):
        # print(tekst[dl])
        for key in morse_dict.keys():
            if morse_dict[key] == text[dl]:
                word = word + str(key)

    print(word)
    # slowo=slowo.replace("1",'.')
    # slowo=slowo.replace("0",'_ ')
    # print(slowo)
    file.close()


# MTT("MTT.txt", alfabetmorsa)