# Tu będzie syntezator lub wszystko co związane z odczytaniem morsa i pusczeniem go w świat
import signal
import wave
import numpy as np
import matplotlib.pyplot as plt
from Mors import alfabetmorsa
import pyaudio

SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\Morseshort.wav"
filename = "mowca4.wav"

# wave z alfabetem
for i in alfabetmorsa.keys():
    print("[", i, "] = ", alfabetmorsa[i], "   ")


def load_dane(file_name):
    audio = wave.open(file_name, 'rb')
    s = audio.readframes(-1)
    s = np.fromstring(s, 'Int16')
    rate = audio.getframerate()
    return s, rate


s, rate = load_dane(filename)

# plt.plot(s)
# plt.show()
def Audio_to_text(audio, prob=20):
    audio = abs(audio)
    detektor = []
    avg_audio = []
    # plt.plot(audio)
    # plt.show()
    for i in range(0, len(audio), prob):
        avg_audio.append(np.mean(abs(audio[i:i + prob * 5])))

    # print("Punkt kontrolny 1")
    plt.plot(avg_audio)
    plt.show()
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

    for i in range(0, len(impulsy)):
        if impulsy[i] <= 0:
            if impulsy[i] <= -0.5 * minimal and impulsy[i] > -2 * minimal:
                wyraz = wyraz + ""
            if impulsy[i] <= -2 * minimal and impulsy[i] >= -3 * minimal:
                if i != 0 and i != len(impulsy) - 1: wyraz = wyraz + " "
            if impulsy[i] < -3 * minimal:
                slowa.append(wyraz)
                wyraz = ""

        else:
            if impulsy[i] <= 2 * minimal:
                wyraz = wyraz + "1"
            if impulsy[i] > 2 * minimal:
                wyraz = wyraz + "0"

    slowa.append(wyraz)
    return slowa

def Speech_to_text(audio, prob=100):
    audio = abs(audio)
    detektor = []
    avg_audio = []
    # plt.plot(audio)
    # plt.show()
    for i in range(0, len(audio), prob):
        avg_audio.append(np.mean(abs(audio[i:i + prob * 5])))

    # print("Punkt kontrolny 1")
    plt.plot(avg_audio)
    plt.show()

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


# slowa=Audio_to_text(s)
# print(slowa)

slowa=Speech_to_text(s)
print(slowa)

def MTT(slowa, alfabet):
    slowo = ""
    for dl in range(0, len(slowa)):
        # print(tekst[dl])
        for key in alfabetmorsa.keys():
            if alfabetmorsa[key] == slowa[dl]:
                slowo = slowo + str(key)
    return slowo


slowaaaa=MTT(slowa,alfabetmorsa)

print(slowaaaa)

output=[]
def Morse_to_Audio(slowa, playsound=None):
    kropka = wave.open("kropka.wav", 'rb')
    kreska = wave.open("kreska.wav", 'rb')

    rate_kropka = kropka.getframerate()

    rate_kreska = kreska.getframerate()

    data_kropka = kropka.readframes(-1)
    data_kreska = kreska.readframes(-1)
    data_kropka = np.fromstring(data_kropka, 'Int16')
    data_kreska = np.fromstring(data_kreska, 'Int16')

    dl_kropka = len(data_kropka) / rate_kropka
    dl_kreska = len(data_kreska) / rate_kreska

    import time
    import playsound
    output=[]
    from playsound import playsound
    for element in slowa:
        # print(element)
        for i in range(0, len(element)):
            # print(element[i])
            if element[i] == '1':
                # playsound("kropka.wav")
                output.extend(data_kropka)

            if element[i] == '0':
                # playsound("kreska.wav")
                output.extend(data_kreska)

            if i != len(element) - 1:
                # time.sleep(dl_kropka)
                output.extend(np.zeros(int(len(data_kropka))))
            else:
                continue
        # time.sleep(dl_kreska)
        output.extend(np.zeros(int(len(data_kreska))))

    # print(output)
    import scipy.io.wavfile
    wynik=np.asarray(output)

    wynik=np.array(wynik).astype('int16')

    scipy.io.wavfile.write("OutPutMORSEM_mowca4.wav", rate_kreska, wynik)

    #plik sie nie odtwarza w windowsie ale w audacity jest już wyraźnym szumem XD

    kropka.close()
    kreska.close()

Morse_to_Audio(slowa)
