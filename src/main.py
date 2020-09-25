import toml
import ntpath

import file_helper as fh

## OS aware downloads folder
DOWNLOADS_FOLDER = fh.get_download_path()

## assume latest downloaded file is the aws profile csv
profile_csv = fh.get_newest_csv(DOWNLOADS_FOLDER)

profile_dict = {}
profile_name = ntpath.basename(profile_csv)
reader = fh.csv_to_ordered_dict(profile_csv)

for profile in reader:
    profile_dict = dict(profile)

profile_dict = {profile_name: profile_dict}
print(toml.dumps(profile_dict).replace('"', ""))
