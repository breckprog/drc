import pyaudio
import wave

from drc.interfaces import AudioFormat
from drc.interfaces import AudioSource


class WaveFileSource(AudioSource):

    def __init__(self, path, block_size=4096):
        self.source = source = wave.open(path)
        self.format = AudioFormat(
            source.getnchannels(),
            source.getsampwidth(),
            source.getframerate(),
            block_size)
        self.block_size = block_size

    def __iter__(self):
        source = self.source
        block_size = self.block_size
        block = source.readframes(block_size)
        while block:
            yield block
            block = source.readframes(block_size)

    def get_format(self):
        return self.format


class PyAudioSource(AudioSource):

    def __init__(self, nchannels=1, samplewidth=2, framerate=44100,
                 block_size=4096):
        self.format = AudioFormat(nchannels, samplewidth, framerate, block_size)
        self.block_size = block_size
        self.pa = pa = pyaudio.PyAudio()
        self.source = pa.open(
            format=pa.get_format_from_width(samplewidth),
            channels=nchannels,
            rate=framerate,
            frames_per_buffer=block_size,
            input=True)

    def __iter__(self):
        source = self.source
        block_size = self.block_size
        while True:
            yield source.read(block_size)

    def get_format(self):
        return self.format
