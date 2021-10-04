from app.json.json_file import JsonFile
from app.json.json_file_paths_manager import get_option_prefs_path
class JsonFileFactory:

    # returns a JsonFile that represents option_prefs.json
    def get_option_prefs_file(self) -> JsonFile:
        p = get_option_prefs_path()
        return JsonFile(p)