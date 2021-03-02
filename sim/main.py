from sim.util.processor import Processor
from sim.util.sampler import Sampler

def main():
    # Create utils
    processor = Processor()
    sampler = Sampler()

    symbol_list = ["SPY"]
    symbol = symbol_list[0]

    # Load useful data into application memory
    spy_raw_data = processor.load_data(symbol)


    # Generate simulation data


    # Process data


    # Share findings

    # TEST
    print("Hello World")

if __name__ == "__main__":
    main()