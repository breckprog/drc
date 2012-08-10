import sys

from drc.pipeline import Pipeline
from drc.processors import AveragePower
from drc.sinks import PyAudioSink
from drc.sources import WaveFileSource

from drc.interfaces import AudioProcessor
from drc.interfaces import AudioSink
import array

class MuteRightChannel(AudioProcessor):

    def __call__(self, block, statistics):
        assert len(block) == 8192 * 2
        assert self.format.nchannels == 2
        mutable = array.array('c', block)
        for i in xrange(2, 8192 * 2, 4):
            mutable[i] = mutable[i+1] = chr(0) #chr(0xff/2)
        block = mutable.tostring()
        return block


class PrintPower(AudioSink):

    def __call__(self, block, statistics):
        print 'RMS Power', statistics['rms_power']


source = WaveFileSource(sys.argv[1])
pipeline = Pipeline(source)
#pipeline.add_processor(MuteRightChannel())
pipeline.add_processor(AveragePower())
pipeline.add_sink(PyAudioSink())
pipeline.add_sink(PrintPower())
pipeline.run()

