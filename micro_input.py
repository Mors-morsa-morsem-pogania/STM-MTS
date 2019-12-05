"""
zbiera przez 5 sekund z mikrofonu

UWAGI:
na razie u mnie działa tylko z mikro wewnętrznym laptopa //Paula

"""

import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as signal



CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])

def main():
    stream = p.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=True,
                    stream_callback=callback
                    )

    stream.start_stream()

    while stream.is_active():
        time.sleep(5)
        stream.stop_stream()
    stream.close()

    numpydata = np.hstack(fulldata)
    plt.plot(numpydata)
    plt.show()


    p.terminate()

def callback(in_data, frame_count, time_info, flag):
    global b,a,fulldata,dry_data,frames
    audio_data = np.fromstring(in_data, dtype=np.float32)

    fulldata = np.append(fulldata,audio_data)
    return (audio_data, pyaudio.paContinue)

main()
