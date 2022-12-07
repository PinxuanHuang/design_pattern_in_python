from dataminer import BaseDataMiner
from datasource1 import DataSource1
from datasource2 import DataSource2

def collect_data_from(abstract_class: BaseDataMiner):
    print("# ", "="*25, " #")
    print(f"start collect data from {abstract_class.__class__.__name__}")
    abstract_class.start_procedure()
    print("procedure complete")
    print("# ", "="*25, " #")
    
if __name__ == "__main__":
    collect_data_from(DataSource1())
    collect_data_from(DataSource2())