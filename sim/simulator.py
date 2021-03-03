from sim.util.processor import Processor
from sim.util.sampler import Sampler
from sim.constants import (
    SPY_DATA_FILE,
    TLT_DATA_FILE,
    QQQ_DATA_FILE,
    SPY,
    TLT,
    QQQ
)

class Simulator:
    def __init__(self):
        # Create utils
        self.processor = Processor()
        self.sampler = Sampler()

    def simulate(self):
        # Load processed data
        spy_processed_data = self.processor.process_data(SPY_DATA_FILE)
        qqq_processed_data = self.processor.process_data(QQQ_DATA_FILE)
        tlt_processed_data = self.processor.process_data(TLT_DATA_FILE)


        # Generate simulation data


        # Process data


        # Share findings

        # TEST
        print("Hello World")
