import os

def get_app_path() -> str:
    """Returns the path to the app directory. Assumes that this file is located in a direct
    subdirectory of the app directory. """
    current_file_path = os.path.abspath(__file__)
    current_dir_path = os.path.dirname(current_file_path)
    project_path = os.path.abspath(os.path.join(current_dir_path, ".."))
    return project_path

def get_src_path() -> str:
    """Returns the path to the python src directory. """
    src_path = os.path.abspath(os.path.join(get_app_path(), ".."))
    return src_path

def get_backend_path() -> str:
    """Returns the path to the backend directory. """
    root_path = os.path.abspath(os.path.join(get_src_path(), ".."))
    return root_path

def get_root_path() -> str:
    """Returns the path to the project root directory. """
    out_path = os.path.abspath(os.path.join(get_backend_path(), ".."))
    return out_path

def get_data_path() -> str:
    """Returns the path to the data directory. """
    data_path = os.path.abspath(os.path.join(get_root_path(), "data"))
    return data_path