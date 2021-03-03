import pandas as pd

class Processor:
    def __init__(self):
        self.data_base_path = "../data/"

    def process_data(self, file_name):
        file_path = self.generate
        raw_data = pd.read_csv(file_name)
        return raw_data

    def generate_filepath(self, file_name):
        return self.data_base_path  + file_name


    def generate_monthly_returns(self):
        pass