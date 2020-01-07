from STM import get_word, text_to_binary_morse
from MTS import audio_to_text, speech_to_text, load_dane, morse_to_audio, binary_Morse_to_text, morse_to_text
from micro_input import record_sound_on_key, WAVE_OUTPUT_FILENAME
import winsound
import time
from tts.call_synthesize import call_synthesize
from address_provider import AddressProvider

def call_STM():

    word = ""
    choice = 5
    while choice != 0:
        choice = int(input("Wybierz sposób wprowadzenia sygnału: \n[1] Mikrofon \n[2] Klawiatura \n\n[0] Cofnij do menu\n"))
        if choice == 1:
            print("Naciśnij i przytrzymaj LCtrl aby nagrywać. Puść LCtrl, aby zakończyć nagrywanie.\n")
            word = get_word()
            break
        elif choice == 2:
            word = input("Wprowadź słowo do przetłumaczenia: ")

            break
        elif choice == 0:
            return
        else:
            print("Wybierz prawidłową opcję.\n")

    wordlist, wordall = text_to_binary_morse(word)
    print("Tłumaczenie: ",wordall)
    morse_to_audio(wordlist)

    time.sleep(2.5)
    filepath = "output\\code_to_audio_output.wav"
    winsound.PlaySound(filepath, winsound.SND_FILENAME | winsound.SND_NOWAIT)

    return


def call_MTS():

    choice = 5
    while choice != 0:
        choice = int(input("Wybierz sposób wprowadzenia sygnału: \n[1] Mowa (jednotonowa samogłoska) \n[2] Inne (maszynowe) \n[3] Klawiatura \n\n[0] Cofnij do menu\n"))
        if choice == 1:
            print("Naciśnij i przytrzymaj LCtrl aby nagrywać. Puść LCtrl, aby zakończyć nagrywanie.\n")
            record_sound_on_key()
            audio,rate = load_dane(file_name="output\\output.wav")
            word = speech_to_text(audio=audio)
            translated = binary_Morse_to_text(word)

            choice1 = 6
            while choice1 != 0:
                choice1 = int(input("Wybierz sposób wyprowadzenia sygnału: \n[1] Wyświetl \n[2] Odtwórz\n"))
                if choice1 == 1:
                    print(translated)
                    break
                elif choice1 == 2:
                    output_wave_file = 'tts_output.wav'
                    ap = AddressProvider()
                    address = ap.get("tts")
                    sampling_rate = 44100
                    input_text = translated
                    time.sleep(1.5)
                    call_synthesize(address, input_text, output_wave_file, sampling_rate)
                    break
                else:
                    print("Wybierz prawidłową opcję.\n")
            break

        elif choice == 2:
            print("Naciśnij i przytrzymaj LCtrl aby nagrywać. Puść LCtrl, aby zakończyć nagrywanie.\n")
            record_sound_on_key()
            audio, rate = load_dane(file_name="output\\output.wav")
            word = speech_to_text(audio=audio)
            translated = binary_Morse_to_text(word)

            choice1 = 6
            while choice1 != 0:
                choice1 = int(input("Wybierz sposób wyprowadzenia sygnału: \n[1] Wyświetl \n[2] Odtwórz\n"))
                if choice1 == 1:
                    print(translated)
                    break
                elif choice1 == 2:
                    output_wave_file = 'tts_output.wav'
                    ap = AddressProvider()
                    address = ap.get("tts")
                    sampling_rate = 44100
                    input_text = translated
                    time.sleep(1.5)
                    call_synthesize(address, input_text, output_wave_file, sampling_rate)
                    break
            break
        elif choice == 3:
            print("Zasady: \n1. Słowa oddzielamy spacją \n2. Znaki w literze oddzielamy symbolem |\nPrzykład: |111|000|111| = SOS")
            word = input("Wprowadź słowo do przetłumaczenia: ")
            word_Morse=morse_to_text(word)
            print("Tłumaczenie: ", word_Morse)
            break
        elif choice == 0:
            return
        else:
            print("Proszę wybrać prawidłową opcję.\n")

    return


def call_exit():

    print("Dziękujemy za skorzystanie z programu. Miłego dnia!\n")
    return

def call_error():

    print("Proszę wybrać prawidłową opcję. \n")
