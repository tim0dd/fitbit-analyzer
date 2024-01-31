
import os


def get_fitbit_analyzer_path() -> str:
    """Returns the path to the fitbit_analyzer directory. Assumes that this file is located in a direct
    subdirectory of the medseg directory. """
    current_file_path = os.path.abspath(__file__)
    current_dir_path = os.path.dirname(current_file_path)
    project_path = os.path.abspath(os.path.join(current_dir_path, ".."))
    return project_path

def get_src_path() -> str:
    """Returns the path to the python src directory. """
    src_path = os.path.abspath(os.path.join(get_fitbit_analyzer_path(), ".."))
    return src_path

def get_root_path() -> str:
    """Returns the path to the project root directory. """
    root_path = os.path.abspath(os.path.join(get_src_path(), ".."))
    return root_path

def get_out_path() -> str:
    """Returns the path to the project root directory. """
    out_path = os.path.abspath(os.path.join(get_root_path(), "out"))
    return out_path