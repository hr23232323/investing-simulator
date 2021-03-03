import pandas as pd
import os

DATA_DIR = os.getcwd() + "/data/"

class Processor:
    def __init__(self):
        pass

    def process_data(self, file_name):
        file_path = self.generate_filepath(file_name)
        raw_data = pd.read_csv(file_path)
        return raw_data

    def generate_filepath(self, file_name):
        return DATA_DIR  + file_name


    def generate_monthly_returns(self):
        pass