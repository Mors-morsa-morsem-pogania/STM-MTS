#tu będzie zbieranie mowy i wszystko co z tym związane 

from micro_input import record_sound_on_key
from run_dictation import DictationArgs, DictationSettings, StreamingRecognizer, create_audio_stream, print_results
from Mors import alfabetmorsa, TTM

#path to recorded words
SOUND_PATH = "D:\Python\PROJEKT-MORS\\tm-clients-master\waves\output.wav"

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
           #print_results(results)

    return results[0]['transcript']


def translate_to_morse(speech):
    """
    Translates and prints given string to Morse code.
    
    :param speech: word to translate
    :return: 
    """
    mors = speech
    slowo = ""
    if str(mors).isalnum() == True:
        print(mors)
        for i in range(0, len(mors)):
            slowo = slowo + str(alfabetmorsa[mors[i]]) + str("|")
        print(slowo)
        slowo = slowo.replace("1", '.')
        slowo = slowo.replace("0", '_ ')
        print(slowo)
    else:
        slowo = "ERROR"
        print(slowo)
        
    # TTM(plikztekstem=speech, slownik=alfabetmorsa)


# word = get_word()
# translate_to_morse(word)
