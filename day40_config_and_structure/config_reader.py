import configparser
def load_config(path: str="config.ini")->configparser.ConfigParser:
    config=configparser.ConfigParser()
    read_files=config.read(path)

    if not read_files:
        raise FileNotFoundError(f"Config file not found: {path}")
    return config
