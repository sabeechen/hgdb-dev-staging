import json
import sys
import os
from os.path import join


def main():
    print(os.getcwd())
    files = os.listdir(os.getcwd())
    for f in files:
        print(f)
    print("Listing Complete")

    source_repo = sys.argv[0]
    staging_repo = sys.argv[1]
    run_number = os.environ.get('GITHUB_RUN_NUMBER', -1)
    with open(join(source_repo, "hassio-google-drive-backup", "config.json")) as f:
        source_config = json.load(f)
        print("Source verison is '{0}'".format(source_config['version']))

    with open(join(staging_repo, "hassio-google-drive-backup", "config.json")) as f:
        staging_config = json.load(f)
        print("Current staging version is '{0}'".format(staging_config['version']))

    new_version = source_config['version'] + ".staging." + run_number

    print("New staging version will be '{0}'".format(new_version))
    source_config['version'] = new_version
    source_config['name'] = source_config['name'] + " (staging)"
    source_config['slug'] = source_config['slug'] + "_staging"
    source_config['image'] = source_config['image'] + "_staging"
    source_config['panel_title'] = source_config['panel_title'] + "(staging)"
    with open(join(source_repo, "hassio-google-drive-backup", "config.json"), "w") as f:
        json.dump(source_config, f)
    with open(join(staging_repo, "hassio-google-drive-backup", "config.json"), "w") as f:
        json.dump(source_config, f)


if __name__ == '__main__':
    print("Starting")
    main()