#tu będzie zbieranie mowy i wszystko co z tym związane 

# from micro_input import record_sound_on_key
from run_dictation import DictationArgs, DictationSettings, StreamingRecognizer, create_audio_stream, print_results
from Mors import alfabetmorsa
from MTS import Morse_to_Audio

#path to recorded words
SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\Krokiet\WieczorowąPorą.wav"
# SOUND_PATH="E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\tm-clients-master\waves\example.wav"
# SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\annaiania.wav"
def get_word():
    """
    Records speech using micro_input.py (records on key),
    then creates transcript of spoken word or sentence by [dictation] system.
    
    :return: recognized word or sentence
    """
    #record_sound_on_key()

    args = DictationArgs(wav_filepath=SOUND_PATH)
    # args = DictationArgs(wav_filepath="output.wav")
    # args = DictationArgs()

    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)

            print('Recognizing...')
            results = recognizer.recognize(stream)
            print_results(results)

    return results[0]['transcript']


def translate_to_morse(speech):
    """
    Translates and prints given string to Morse code.
    
    :param speech: word to translate
    :return: 
    """
    mors = speech
    slowo = ""
    slowa=[]
    if str(mors.replace(" ","")).isalnum() == True:
        # print(mors)
        for i in range(0, len(mors)):
            slowo = slowo + str(alfabetmorsa[mors[i]]) + str("|")
        # print(slowo)
        # slowo = slowo.replace("1", '.')
        # slowo = slowo.replace("0", '_')
        # print(slowo)
        slowa=slowo.split("|")
    else:
        slowo = "ERROR"
        # print(slowo)
    # print(slowa)
    return slowa,slowo
    # TTM(plikztekstem=speech, slownik=alfabetmorsa)


word = get_word()

# print(word)
slowaa,slowo=translate_to_morse(word)

# Morse_to_Audio(slowaa,alfabetmorsa,filename="OUTPUT_STM.wav")

def utf8len(s):
    return len(s.encode('utf-8'))

print(word)
print("Dlugosc sekwencji w znakach: ",len(word), " Typ: ", type(word) )
print("Dlugosc sekwencji w bitach: ",len(str.encode(word)), " Typ: ", type(str.encode(slowo)) )
print("_____________________________")
print(slowo)
print("Dlugosc sekwencji w znakach: ",len(slowo), " Typ: ", type(slowo) )
print("Dlugosc sekwencji w bitach: ",len(str.encode(slowo)), " Typ: ", type(str.encode(slowo)) )
#
# my_str = "hello world"
# my_str_as_bytes = str.encode(my_str)
# print(len(my_str_as_bytes))
# print(type(my_str_as_bytes)) # ensure it is byte representation
# my_decoded_str = my_str_as_bytes.decode()
# print(type(my_decoded_str)) # ensure it is string representation

