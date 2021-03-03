from sim.util.processor import Processor
from sim.util.sampler import Sampler

class Simulator:
    def __init__(self):
        # Create utils
        self.processor = Processor()
        self.sampler = Sampler()
        pass

    def simulate(self):

        symbol_list = ["SPY"]
        symbol = symbol_list[0]
        # Load useful data into application memory
        spy_raw_data = self.processor.load_data(symbol)
        spy_processed_data = self.processor.process_data(symbol)


        # Generate simulation data


        # Process data


        # Share findings

        # TEST
        print("Hello World")
