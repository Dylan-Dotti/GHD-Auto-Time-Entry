from typing import Dict

# Logical representation of a Json file
# that provides reading and writing functionality
class JsonFile:

    def __init__(self, file_path: str) -> None:
        pass

    # returns the json data in file_path as a dictionary
    def read_data(self) -> Dict[str, any]:
        return None
    
    # overwrites the data in file_path with the given data
    def write_data(self, data: Dict[str, any]):
        pass