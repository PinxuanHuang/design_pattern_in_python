from dataminer import BaseDataMiner

class DataSource2(BaseDataMiner):
    def collect_data(self) -> None:
        print("collect data from source2...")
    
    def extract_data(self) -> None:
        print("parse the data which was collected from source2...")
    
    def parse_data(self) -> None:
        print("parse the data which was collected from source2...")