from cStringIO import StringIO
import math
import struct

from drc.interfaces import AudioProcessor

class AveragePower(AudioProcessor):
    """
    Finds average power of audio in block and adds value to
    statistics['rms_power'].  All channels are averaged together.  The audio is
    not mutated in any way.
    """
    def __call__(self, block, statistics):
        format = self.format
        assert format.samplewidth == 2, format.samplewidth
        sum_of_squares = 0
        num_samples = 0
        stream = StringIO(block)
        chunk = stream.read(2)
        while chunk:
            num_samples += 1
            sample = struct.unpack('<h', chunk)[0]
            sum_of_squares += sample*sample
            chunk = stream.read(2)
        statistics['rms_power'] = math.sqrt(sum_of_squares)
        return block
