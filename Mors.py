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
