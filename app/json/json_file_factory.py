from app.json.json_file import JsonFile
from app.json.json_file_paths_manager import get_option_prefs_path
class JsonFileFactory:

    # returns a JsonFile that represents option_prefs.json
    def get_option_prefs_file(self) -> JsonFile:
        p = get_option_prefs_path()
        p_str = str(p)
        if p.is_file():
            return JsonFile(p_str)
        
        d_data = {
            "data_directory": None,
            "name": None,
            "num_sap_rows": None,
            "use_fn_button": None
        }

        f = JsonFile(p_str)
        f.write_data(d_data)
        return f
