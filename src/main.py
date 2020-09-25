import toml
import file_helper as fh

## OS aware downloads folder
DOWNLOADS_FOLDER = fh.get_download_path()

## assume latest downloaded file is the aws profile csv
profile_csv = fh.get_newest_csv(DOWNLOADS_FOLDER)

profile_dict = {}
reader = csv.DictReader(open(profile_csv))

for v in reader:
    mydict = dict(v)

print(toml.dumps(mydict))
