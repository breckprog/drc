

class Pipeline(object):

    def __init__(self, source):
        self.source = source
        self.processors = []
        self.sinks = []

    def add_processor(self, processor):
        processor.set_format(self.source.format)
        self.processors.append(processor)

    def add_sink(self, sink):
        sink.set_format(self.source.format)
        self.sinks.append(sink)

    def run(self):
        source = self.source
        for block in source:
            statistics = {}
            for processor in self.processors:
                block = processor(block, statistics)
            for sink in self.sinks:
                sink(block, statistics)
