# this would keep track of the json file paths
# for use by json_file_factory
from pathlib import Path

def get_option_prefs_path():
    return Path(__file__).parent / "json_files" / "option_prefs.json"