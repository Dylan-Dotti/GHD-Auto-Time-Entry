import app.option_preferences.column_layout.default_column_layout as col_layout
from app.json.json_file import JsonFile
from app.json.json_file_paths_manager import get_option_prefs_path
from app.option_preferences.column_layout.sap_column_layout import SapColumnLayout

class JsonFileFactory:

    # returns a JsonFile that represents option_prefs.json
    def get_option_prefs_file(self) -> JsonFile:
        p = get_option_prefs_path()
        p_str = str(p)
        print('option prefs path:', p_str)
        if p.is_file():
            print('found option prefs file')
            return JsonFile(p_str)
        
        print("Option prefs file not found. Generating default...")
        d_data = {
            "data_directory": None,
            "name": None,
            "num_sap_rows": None,
            "use_fn_button": None,
            "column_layout": SapColumnLayout(col_layout.DEFAULT_COLUMN_LAYOUT).to_json_data()
        }

        f = JsonFile(p_str)
        f.write_data(d_data)
        return f
