from typing import Dict
import json
# Logical representation of a Json file
# that provides reading and writing functionality

class JsonFile:

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        pass

    # returns the json data in file_path as a dictionary
    def read_data(self) -> Dict[str, any]:
        try:
            with open (self.file_path, 'r') as json_path:
                return json.load(json_path)
        except Exception as err:
            # place hold just kill
            print("Error reading pref file: " + str(err))
            exit(0)    

    # overwrites the data in file_path with the given data
    def write_data(self, data: Dict[str, any]):
        try:
            with open (self.file_path, 'w') as json_path:
                json.dump(data, json_path, indent=4)

        except Exception as err:
           # place hold just kill
            print("Error reading pref file: " + str(err))
            exit(0)   