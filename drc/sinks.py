import pyaudio

from drc.interfaces import AudioSink


class PyAudioSink(AudioSink):

    def set_format(self, format):
        self.pa = pa = pyaudio.PyAudio()
        self.out = pa.open(
            format=pa.get_format_from_width(format.samplewidth),
            channels=format.nchannels,
            rate=format.framerate,
            frames_per_buffer=format.block_size*2, # for some reason this works
            output=True)

    def __call__(self, block, statistics):
        self.out.write(block)

    def __del__(self):
        self.out.close()
        self.pa.terminate()
