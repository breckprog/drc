import abc
from collections import namedtuple


AudioFormat = namedtuple('AudioFormat',
                         ('nchannels', 'samplewidth', 'framerate'))

class AudioSource(object):
    """
    An implementation of IAudioSource should be an iterable, usually implemented
    as a generator, that yields blocks of wave data.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_format(self):
        """
        Return instance of AudioFormat.
        """


class AudioProcessor(object):
    """
    An IAudioProcessor instance can be place in an audio processing pipeline
    and can either mutate the audio data and/or gather statistics about the
    audio.
    """
    __metaclass__ = abc.ABCMeta

    def set_format(self, format):
        self.format = format

    @abc.abstractmethod
    def __call__(self, block, statistics):
        """
        Process a block of audio.  The return value is the new audio data block.
        ``statistics`` is a ``dict`` instance which can be populated with
        arbitrary keys representing different aggregate information about the
        block.
        """


class AudioSink(object):
    """
    An endpoint for an audio pipeline.  Responsible for getting statistics
    and/or audio data to wherever it's supposed to go.
    """
    __metaclass__ = abc.ABCMeta

    def set_format(self, format):
        self.format = format

    @abc.abstractmethod
    def __call__(self, block, statistics):
        """
        Dispatch audio and/or statistics data wherever it is that it's
        supposed to go.  No return value.
        """
