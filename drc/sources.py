import wave

from drc.interfaces import AudioFormat
from drc.interfaces import AudioSource


class WaveFileSource(AudioSource):

    def __init__(self, path, block_size=4096):
        self.source = source = wave.open(path)
        self.format = AudioFormat(
            source.getnchannels(),
            source.getsampwidth(),
            source.getframerate())
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
