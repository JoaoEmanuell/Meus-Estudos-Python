from typing import Dict

from .algorithm_template import AlgorithmTemplate

class CSVProcessor(AlgorithmTemplate) :

    def insert_value_in_doc(self, formatted_data_with_id : Dict[str, str]) -> None :
        print("CSV Processor")
        print(formatted_data_with_id)