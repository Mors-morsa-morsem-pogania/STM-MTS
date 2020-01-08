# Tu będzie syntezator lub wszystko co związane z odczytaniem morsa i pusczeniem go w świat
import signal
import wave
import numpy as np
from morse_coding import AlfabetMorsa
import scipy.io.wavfile as wav
from numpy import ones

#SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\Morseshort.wav"
SOUND_PATH = "D:\\Python\\PROJEKT-MORS\\Morseshort.wav"
filename = "output\\output.wav"

def load_dane(file_name=filename):
    audio = wave.open(file_name, 'rb')
    s = audio.readframes(-1)
    s = np.fromstring(s, 'Int16')
    rate = audio.getframerate()
    return s, rate


def audio_to_text(audio, prob=20):
    """
    Transforms knocking Morse to binary
    :param audio: Audio data to transform
    :param prob:
    :return: text
    """
    audio = abs(audio)
    detektor = []
    avg_audio = []
    for i in range(0, len(audio), prob):
        avg_audio.append(np.mean(abs(audio[i:i + prob * 5])))

    # print("Punkt kontrolny 1")

    for i in range(0, len(avg_audio)):
        if avg_audio[i] > max(avg_audio) / 3:
            detektor.append(1)
        else:
            detektor.append(-1)
    detektor.append(0)
    impulsy = []
    impulsy.append(0)
    # print("Punkt kontrolny 2")
    el = 0
    for i in range(1, len(detektor)):
        if detektor[i] == detektor[i - 1]:
            impulsy[el] = impulsy[el] + detektor[i]
        else:
            impulsy.append(0)
            el = el + 1
    # print(detektor)
    # print(impulsy)
    # print("Punkt kontrolny 3")
    slowa = []
    wyraz = ""
    bezwgl = []
    for ele in impulsy:
        if ele != 0: bezwgl.append(abs(ele))

    minimal = min(bezwgl)
    if impulsy[0]<0: del impulsy[0]
    if impulsy[len(impulsy)-1]<0: del impulsy[len(impulsy)-1]
    for i in range(0, len(impulsy)):
        if impulsy[i] <= 0:
            if impulsy[i] <= -0.5 * minimal and impulsy[i] > -2 * minimal:
                wyraz = wyraz + ""
            if impulsy[i] <= -2 * minimal and impulsy[i] >= -3 * minimal:
                if i != 0 and i != len(impulsy) - 1: wyraz = wyraz + " "
            if impulsy[i] < -3 * minimal:
                wyraz=wyraz.replace(" ", "")
                slowa.append(wyraz)
                wyraz = ""
            if impulsy[i] < -9 * minimal:
                slowa.append(" ")
        else:
            if impulsy[i] <= 2 * minimal:
                wyraz = wyraz + "1"
            if impulsy[i] > 2 * minimal:
                wyraz = wyraz + "0"
    wyraz=wyraz.replace(" ", "")
    slowa.append(wyraz)

    return slowa


def speech_to_text(audio, prob=100):
    """
    Transforms spoken Morse (on vowels) to binary
    :param audio: Audio data to transform
    :param prob:
    :return:
    """

    audio = abs(audio)
    detektor = []
    avg_audio = []

    for i in range(0, len(audio), prob):
        avg_audio.append(np.mean(abs(audio[i:i + prob * 5])))

    # print("Punkt kontrolny 1")

    for i in range(0, len(avg_audio)):
        if avg_audio[i] > max(avg_audio) / 4:
            detektor.append(1)
        else:
            detektor.append(-1)
    detektor.append(0)
    impulsy = []
    impulsy.append(0)
    # print("Punkt kontrolny 2")
    el = 0
    for i in range(1, len(detektor)):
        if detektor[i] == detektor[i - 1]:
            impulsy[el] = impulsy[el] + detektor[i]
        else:
            impulsy.append(0)
            el = el + 1
    # print(detektor)
    print(impulsy)
    # print("Punkt kontrolny 3")
    slowa = []
    wyraz = ""
    bezwgl = []
    for ele in impulsy:
        if ele != 0: bezwgl.append(abs(ele))
    if impulsy[0]<0: del impulsy[0]
    if impulsy[len(impulsy)-1]<0: del impulsy[len(impulsy)-1]
    minimal = min(bezwgl)
    maximal=max(impulsy)
    minimalne_minimum=min(impulsy)
    for i in range(0, len(impulsy)):
        if impulsy[i] <= 0:
            if impulsy[i] <= -0.5 * minimal and impulsy[i] > 0.6 * minimalne_minimum:
                wyraz = wyraz + ""
            # if impulsy[i] <= 0.1 * minimalne_minimum and impulsy[i] >= 0.5 * minimalne_minimum:
            #     if i != 0 and i != len(impulsy) - 1: wyraz = wyraz + " "
            if impulsy[i] < 0.6 * minimalne_minimum:
                slowa.append(wyraz)

                wyraz = ""

        else:
            if impulsy[i] <= 0.5 * maximal:
                wyraz = wyraz + "1"
            if impulsy[i] > 0.5 * maximal:
                wyraz = wyraz + "0"

    slowa.append(wyraz)
    return slowa


def binary_Morse_to_text(text,morse_dict=AlfabetMorsa):
    """
    Transforms given list of Morse binary signs into words using given dictionary
    :param slowa: list of Morse binary signs
    :param alfabet: dictionary with Morse binary coding
    :return: string -> translated word
    """

    word = ""
    for dl in range(0, len(text)):
        # print(tekst[dl])
        for key in morse_dict.keys():
            if morse_dict[key] == text[dl]:
                word = word + str(key)
                break
    return word


def morse_to_audio(words, playsound=None, name_file="output\\code_to_audio_output.wav"):
    """
    Transforms binary Morse code to beeping audio
    :param words: string to transform
    :param playsound: -
    :param name_file: name of wave file with the output
    :return:
    """
    dot = wave.open("kropka.wav", 'rb')
    dash = wave.open("kreska.wav", 'rb')

    rate_dot = dot.getframerate()

    rate_dash = dash.getframerate()

    data_dot = dot.readframes(-1)
    data_dash = dash.readframes(-1)
    data_dot = np.fromstring(data_dot, 'Int16')
    data_dash = np.fromstring(data_dash, 'Int16')

    l2=len(data_dot)
    l1=len(data_dash)

    output=[]

    for element in words:
        # print(element)
        for i in range(0, len(element)):
            # print(element[i])
            if element[i] == '1':
                # playsound("kropka.wav")
                output.extend(data_dot)

            if element[i] == '0':
                # playsound("kreska.wav")
                output.extend(data_dash)
            if element[i] == ' ':
                output.extend(np.zeros(int(len(data_dash)))*3)
            if i != len(element) - 1:
                # time.sleep(dl_kropka)
                output.extend(np.zeros(int(len(data_dot))))
            else:
                continue
        # time.sleep(dl_kreska)
        output.extend(np.zeros(int(len(data_dash))))

    # print(output)

    wynik=np.asarray(output)

    wynik=np.array(wynik).astype('int16')

    wav.write(name_file, rate_dash, wynik)

    #plik sie nie odtwarza w windowsie ale w audacity jest już wyraźnym szumem XD

    dot.close()
    dash.close()

def morse_to_text(text, morse_dict=AlfabetMorsa):
    """
    Morse to Text
    :param textfile_name: Name of txt file in which the output will appear
    :param morse_dict: Dictionary variable containing Morse's signs written in binary system
    :return:
    """
    text = text.replace(".", '1')
    text = text.replace("_ ", '0')
    text = text.split("|")
    word = ""
    for dl in range(0, len(text)):
        # print(tekst[dl])
        for key in morse_dict.keys():
            if morse_dict[key] == text[dl]:
                word = word + str(key)
                break
    return word