from abc import ABC, abstractmethod

class BaseDataMiner(ABC):
    def start_procedure(self) -> None:
        self.hook()
        self.collect_data()
        self.extract_data()
        self.parse_data()
        self.store_data()
        self.send_report()
    
    def store_data(self) -> None:
        print("store the data to database...")

    def send_report(self) -> None:
        print("send the report to maintainer...")

    def hook(self) -> None:
        print("using a condition to decide whether execute the procedure or not")
    
    @abstractmethod
    def collect_data(self) -> None:
        pass

    @abstractmethod
    def extract_data(self) -> None:
        pass
    
    @abstractmethod
    def parse_data(self) -> None:
        pass
    