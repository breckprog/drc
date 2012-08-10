from drc.pipeline import Pipeline
from drc.processors import AveragePower
from drc.sources import PyAudioSource

from drc.interfaces import AudioSink

class PrintPower(AudioSink):

    def __call__(self, block, statistics):
        print 'RMS Power', statistics['rms_power']


source = PyAudioSource()
pipeline = Pipeline(source)
pipeline.add_processor(AveragePower())
pipeline.add_sink(PrintPower())
pipeline.run()
