# Tu będzie syntezator lub wszystko co związane z odczytaniem morsa i pusczeniem go w świat
import signal
import wave
import numpy as np
import matplotlib.pyplot as plt
from Mors import alfabetmorsa
import pyaudio

SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\Morseshort.wav"
filename = "val2.wav"

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
def Audio_to_text(audio, prob=200):
    audio = abs(audio)
    detektor = []
    avg_audio = []
    # plt.plot(audio)
    # plt.show()
    for i in range(0, len(audio), prob):
        avg_audio.append(np.mean(abs(audio[i:i + prob * 5])))
        # avg_audio.append(audio[i])
    # print("1")
    # plt.plot(avg_audio)
    # plt.show()
    for i in range(0, len(avg_audio)):
        # print(avg_audio[i])
        # print(max(avg_audio)/3)
        if avg_audio[i] > max(audio) / 3:
            detektor.append(1)
        else:
            detektor.append(-1)
    detektor.append(0)
    impulsy = []
    impulsy.append(0)
    # print("2")
    el = 0
    for i in range(1, len(detektor)):
        if detektor[i] == detektor[i - 1]:
            impulsy[el] = impulsy[el] + detektor[i]
        else:
            impulsy.append(0)
            el = el + 1
    # print(detektor)
    # print(impulsy)
    # print("3")
    slowa = []
    wyraz = ""
    bezwgl = []
    for ele in impulsy:
        if ele != 0: bezwgl.append(abs(ele))
    print(bezwgl)

    maximal = max(impulsy)
    minimal = min(bezwgl)
    print(minimal)
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

        #
        #
        # if impulsy[i]<minimal or impulsy[i]==0:
        #     slowa.append(wyraz)
        #     wyraz=""
        #     slowa.append(" ")
        # if impulsy[i]>maximal/10:
        #     if impulsy[i]>0 and impulsy[i]<=maximal/3:
        #         wyraz=wyraz+("1")
        #     if impulsy[i]>=maximal/3:
        #         wyraz = wyraz +("0")
        # if impulsy[i]<0 and impulsy[i]>minIMP/3:
        #     wyraz = wyraz + (" ")
    return slowa


# slowa=Audio_to_text(s,200)
slowa=Audio_to_text(s,200)
print(slowa)

def MTT(slowa, alfabet):
    slowo = ""
    for dl in range(0, len(slowa)):
        # print(tekst[dl])
        for key in alfabetmorsa.keys():
            if alfabetmorsa[key] == slowa[dl]:
                slowo = slowo + str(key)
    return slowo


# slowa=MTT(slowa,alfabetmorsa)

# print(slowa)
# slowa = ['1', '000', '111','110110']

output=[]
def Morse_to_Audio(slowa, playsound=None):
    kropka = wave.open("kropka.wav", 'rb')
    kreska = wave.open("kreska.wav", 'rb')
    # p_kropka = kropka.getparams()
    # p_kreska = kreska.getparams()
    #
    # nch_kropka = kropka.getnchannels()
    # sampwidth_kropka = kropka.getsampwidth()
    rate_kropka = kropka.getframerate()
    # nframe_kropka = kropka.getnframes()
    #
    # nch_kreska = kreska.getnchannels()
    # sampwidth_kreska = kreska.getsampwidth()
    rate_kreska = kreska.getframerate()
    # nframe_kreska = kreska.getnframes()
    #
    # p = pyaudio.PyAudio()
    # play_kropka = p.open(format=p.get_format_from_width(sampwidth_kropka),
    #                      channels=nch_kropka,
    #                      rate=rate_kropka,
    #                      output=True)
    #
    # p = pyaudio.PyAudio()
    # play_kreska = p.open(format=p.get_format_from_width(sampwidth_kreska),
    #                      channels=nch_kreska,
    #                      rate=rate_kreska,
    #                      output=True)
    # chunk = 1024
    data_kropka = kropka.readframes(-1)
    data_kreska = kreska.readframes(-1)
    data_kropka = np.fromstring(data_kropka, 'Int16')
    data_kreska = np.fromstring(data_kreska, 'Int16')
    # play.write(data)
    # play.stop_stream()
    # play stream
    dl_kropka = len(data_kropka) / rate_kropka
    dl_kreska = len(data_kreska) / rate_kreska
    print(dl_kreska)
    print(dl_kropka)
    import time
    import playsound
    output=[]
    from playsound import playsound
    for element in slowa:
        # print(element)
        for i in range(0, len(element)):
            # print(element[i])
            if element[i] == '1':
                playsound("kropka.wav")
                output.extend(data_kropka)
                # data_kropka = kropka.readframes(1024)
                # while data_kropka:
                #     play_kropka.write(data_kropka)
                #     data_kropka = kropka.readframes(1024)

            if element[i] == '0':
                playsound("kreska.wav")
                output.extend(data_kreska)
                # data_kreska = kreska.readframes(1024)
                # while data_kreska:
                #     play_kreska.write(data_kreska)
                #     data_kreska = kreska.readframes(1024)

            if i != len(element) - 1:
                time.sleep(dl_kropka)

                output.extend(np.zeros(int(len(data_kropka))))
        time.sleep(dl_kreska)

        output.extend(np.zeros(int(len(data_kreska))))
    # print(output)
    import scipy.io.wavfile
    wynik=np.asarray(output)
    maksymum=max(abs(wynik))
    srednia=np.mean(wynik)
    for i in range(0,len(wynik)):
        wynik[i]=wynik[i]/maksymum

    scipy.io.wavfile.write("OutPutMORSEM.wav", rate_kreska, wynik)
    #plik sie nie odtwarza w windowsie ale w audacity jest już wyraźnym szumem XD

    # stop stream
    # play_kropka.stop_stream()
    # play_kropka.close()
    # play_kreska.stop_stream()
    # play_kreska.close()
    # p.terminate()


Morse_to_Audio(slowa)
