import pyaudio
import wave
from pynput import keyboard
import threading

# UPORZĄDKOWANE

CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output\\output.wav"

def record_sound_on_key():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []

    recordingEvent = threading.Event()    # set to activate recording
    exitEvent = threading.Event()         # set to stop recording thread


    def on_press(key):
        if key == keyboard.Key.ctrl_l:
            print('- Recording -'.format(key))
            recordingEvent.set()
        else:
            print('incorrect character {0}, press ctrl_l'.format(key))


    def on_release(key):
        print('{0} released'.format(key))
        if key == keyboard.Key.ctrl_l:
            print('{0} stop'.format(key))
            recordingEvent.clear()
            listener.stop()
            return False


    def do_recording():
        while (not exitEvent.is_set()):
            if (recordingEvent.wait(0.1)):
                try:
                    data = stream.read(CHUNK)
                    # print len(data)
                    frames.append(data)
                except IOError:
                    print('warning: dropped frame') # can replace with 'pass' if no message desired


    class myRecorder(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
        def run(self):
            do_recording()


    # start recorder thread
    recordingThread = myRecorder()
    recordingThread.start()

    # monitor keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    # stop recorder thread
    exitEvent.set()
    recordingThread.join()

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return stream