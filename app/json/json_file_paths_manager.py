# this would keep track of the json file paths
# for use by json_file_factory
# have some concerns about relative pathing when accessing the json_files directory
# this would ideally return absolute paths

class JsonFilePathsManager:

    def get_option_prefs_path(self):
        return ''