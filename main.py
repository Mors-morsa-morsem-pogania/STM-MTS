# import STM
# import MTS

def call_STM():

    print("Tu będzie STM")


def call_MTS():

    print("Tu będzie MTS")

def call_exit():

    print("Dziękujemy za skorzystanie z programu. Miłego dnia!")

def call_error():

    print("Proszę wybrać prawidłową opcję. \n")


def menu(option):

if option == 0:
        call_exit()
    elif option == 1:
        call_STM()
    elif option == 2:
        call_MTS()
    else:
        call_error()

def main():
    """
    Main no. Bez tego jak bez ręki.
    Baza menu zrobiona z pomocą https://www.geeksforgeeks.org/switch-case-in-python-replacement/

    :return:
    """
    welcome_message = """MORSEM-GO. Wersja testowa. \n"""
    print(welcome_message)
    choice = int(input("Wybierz moduł: \n\t[1] Speech-To-Morse \n\t[2] Morse-To-Speech \n\n\t[0] Wyjście \n\n"))
    menu(option=choice)

    # na razie nie będzie idiotoodporne do końca
    # while choice != 0 | choice != 1 | choice != 2:
    #     menu(option=choice)


main()
