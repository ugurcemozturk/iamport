import toml
import ntpath

import file_helper as fh

# Get OS-aware downloads folder
DOWNLOADS_FOLDER = fh.get_download_path()

# assumed that the latest downloaded file is the aws profile as csv
profile_csv = fh.get_newest_csv(DOWNLOADS_FOLDER)

# Get filename that'll be used as IAM profile name
profile_name = ntpath.basename(profile_csv).replace(".csv", "")

# Init reader for csv file as OrderedDict
reader = fh.csv_to_ordered_dict(profile_csv)

for line in reader:
    profile_dict = dict(line)

profile_dict = {profile_name: profile_dict}

profile = toml.dumps(profile_dict).replace('"', "")
profile = fh.replace_profile_keys(profile)

with (open("./out", "a+")) as o:
    o.write("\n" + profile)
    o.close()