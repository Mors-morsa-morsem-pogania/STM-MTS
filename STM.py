#tu będzie zbieranie mowy i wszystko co z tym związane 

# UPORZĄDKOWANE

from micro_input import record_sound_on_key
from run_dictation import DictationArgs, DictationSettings, StreamingRecognizer, create_audio_stream, print_results
from morse_coding import AlfabetMorsa


#path to recorded words
# SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\Krokiet\WieczorowąPorą.wav"
# SOUND_PATH="E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\tm-clients-master\waves\example.wav"
# SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\annaiania.wav"

def get_word():
    """
    Records speech using micro_input.py (records on key),
    then creates transcript of spoken word or sentence by [dictation] system.
    
    :return: recognized word or sentence (string)
    """
    record_sound_on_key()

    # args = DictationArgs(wav_filepath=SOUND_PATH)
    args = DictationArgs(wav_filepath="output\\output.wav")
    # args = DictationArgs()

    if args.wave is not None or args.mic:
        with create_audio_stream(args) as stream:
            settings = DictationSettings(args)
            recognizer = StreamingRecognizer(args.address, settings)

            print('Recognizing...')
            results = recognizer.recognize(stream)
            print_results(results)

    return results[0]['transcript']


def text_to_binary_morse(speech):
    """
    Translates and returns given string as Morse code in binary.
    
    :param speech: word to translate (string)
    :return: word_list -> list of signs, word_tmp -> string of signs with "|" as delimeter
    """
    morse = speech
    word_tmp = ""
    word_list = []
    if str(morse.replace(" ","")).isalnum() == True:
        for i in range(0, len(morse)):
            word_tmp = word_tmp + str(AlfabetMorsa[morse[i]]) + str("|")
        word_list = word_tmp.split("|")
    else:
        word_tmp = "ERROR"

    return word_list, word_tmp

