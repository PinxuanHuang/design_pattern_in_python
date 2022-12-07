from dataminer import BaseDataMiner

class DataSource1(BaseDataMiner):
    def collect_data(self) -> None:
        print("collect data from source1...")
    
    def extract_data(self) -> None:
        print("parse the data which was collected from source1...")
    
    def parse_data(self) -> None:
        print("parse the data which was collected from source1...")