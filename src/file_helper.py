import os
import csv


def get_newest_csv(path):
    """Get latest CSV from given path"""
    files = os.listdir(path)
    paths = [
        os.path.join(path, basename) for basename in files if basename.endswith(".csv")
    ]
    if not paths:
        return None
    return max(paths, key=os.path.getctime)


def get_home_dir():
    """Returns OS user home directory"""
    return os.path.expanduser("~")


def get_aws_credentials():
    """Returns aws credentials file"""
    return os.path.join(get_home_dir(), ".aws", "credentials")


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == "nt":
        import winreg
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(get_home_dir(), "Downloads")


def csv_to_ordered_dict(_csv):
    """Returns an OrderedDict from CSV"""
    return csv.DictReader(open(_csv))


def replace_profile_keys(profile):
    """Replace CSV keys with aws iam config formatted keys"""
    profile = profile.replace("Access key ID", "aws_access_key_id")
    profile = profile.replace("Secret access key", "aws_secret_access_key")
    return profile
