#Tu będzie kod do kodowania i odkodywania oraz słownik (lub graf) z morsem
def load_results(filename):
    """
    Loads content of CSV file into a dictionary.
    :param filename: CSV file path
    :return: dictionary [wav_filename]->label
    """
    import csv
    results_dict = dict()
    with open(filename, 'r') as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            results_dict[str(row[0])] = str(row[1])
    return results_dict
alfabetmorsa=load_results(filename="alfabetmorsa.csv")
print(alfabetmorsa)

def TTM(plikztekstem="TTM.txt",slownik=alfabetmorsa):
    """
    Text to Mors
    :param plikzmorsem: string albo plik txt/csv
    :return: plik z tłumaczeniem na tekst
    """
    plik=open(plikztekstem,'r+')
    mors=plik.readline()
    slowo=""
    if str(mors).isalnum()==True:
        print(mors)
        for i in range(0,len(mors)):
            slowo=slowo+str(slownik[mors[i]])+str("|")
        print(slowo)
        slowo=slowo.replace("1",'.')
        slowo=slowo.replace("0",'_ ')
        print(slowo)
    else:
        slowo="ERROR"
        print(slowo)
    plik.close()

TTM("TTM.txt",alfabetmorsa)
