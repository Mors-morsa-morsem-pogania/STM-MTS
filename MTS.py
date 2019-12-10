#Tu będzie syntezator lub wszystko co związane z odczytaniem morsa i pusczeniem go w świat
import signal
import wave
import numpy as np
import matplotlib.pyplot as plt
from Mors import alfabetmorsa

SOUND_PATH = "E:\Studia\Semestr V\Technologia Mowy\ProjektII\Wszystko\\Morseshort.wav"
filename="MorseCode_mid.wav"
#wave z alfabetem
for i in alfabetmorsa.keys():
    print("[",i,"] = ",alfabetmorsa[i],"   ")
audio=wave.open(filename, 'rb')
s = audio.readframes(-1)
s = np.fromstring(s, 'Int16')
rate=audio.getframerate()
_20ms=int(0.02*rate)

plt.plot(s)
plt.show()
def sprawdzamcos(audio):
    audio=abs(audio)
    detektor=[]
    avg_audio=[]
    plt.plot(audio)
    plt.show()
    for i in range(0, len(audio),200):
        avg_audio.append(np.mean(abs(audio[i:i+1000])))
        # avg_audio.append(audio[i])
    print("1")
    plt.plot(avg_audio)
    plt.show()
    for i in range(0, len(avg_audio)):
        # print(avg_audio[i])
        # print(max(avg_audio)/3)
        if avg_audio[i]>max(audio)/3:
            detektor.append(1)
        else:
            detektor.append(-1)
    detektor.append(0)
    impulsy=[]
    impulsy.append(0)
    print("2")
    el=0
    for i in range(1,len(detektor)):
        if detektor[i]==detektor[i-1]:
            impulsy[el]=impulsy[el]+detektor[i]
        else:
            impulsy.append(0)
            el=el+1
    # print(detektor)
    # print(impulsy)
    print("3")
    slowa=[]
    wyraz = ""
    for i in range(0,len(impulsy)):
        if impulsy[i]<min(impulsy)/3 or impulsy[i]==0:
            slowa.append(wyraz)
            wyraz=""
            slowa.append(" ")
        if impulsy[i]>min(impulsy)/2:
            if impulsy[i]>0 and impulsy[i]<=max(impulsy)/3:
                wyraz=wyraz+("1")
            if impulsy[i]>=max(impulsy)/3:
                wyraz = wyraz +("0")
    return slowa

slowa=sprawdzamcos(s)
print(slowa)
slowo=""
for dl in range(0, len(slowa)):
    # print(tekst[dl])
    for key in alfabetmorsa.keys():
        if alfabetmorsa[key] == slowa[dl]:
            slowo = slowo + str(key)

print(slowo)
