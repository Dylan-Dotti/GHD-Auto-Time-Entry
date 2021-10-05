from app.json.json_file_factory import JsonFileFactory
from app.option_preferences.option_prefs import OptionPrefs

# interface that can retrieve the option prefs json data
# or save it to a file
class OptionPrefsJsonInterface:

    def __init__(self) -> None:
        self._json_file_factory = JsonFileFactory()
    
    def load_option_prefs(self) -> OptionPrefs:
        print('Loading option preferences...')
        option_prefs_file = self._json_file_factory.get_option_prefs_file()
        option_prefs_dict = option_prefs_file.read_data()
        return OptionPrefs.from_dict(option_prefs_dict)
    
    def save_option_prefs(self, prefs: OptionPrefs) -> None:
        print('Saving option preferences...')
        option_prefs_file = self._json_file_factory.get_option_prefs_file()
        option_prefs_dict = prefs.to_dict()
        option_prefs_file.write_data(option_prefs_dict)
