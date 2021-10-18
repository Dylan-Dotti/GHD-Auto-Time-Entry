# this would keep track of the json file paths
# for use by json_file_factory
from pathlib import Path

def get_option_prefs_path_cwd() -> str:
    return Path(r"{input_path}".format(input_path=f"{str(Path.cwd())}\option_prefs.json"))

def get_option_prefs_path() -> str:
    return Path(__file__).parent / "json_files" / "option_prefs.json"