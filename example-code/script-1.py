#!/usr/bin/env python3
import subprocess
import sys
from urllib.request import urlretrieve


def main():
    args = sys.argv[1:]
    # FIXME: issue when running python3 <script> vs ./<script>
    print(f'args: {args}')
    remote_filepath = 'mache/deploy/script-2.py'  # path to file on GitHub
    branch = 'develop'  # TODO: (low priority) add cmd line arg to change?
    url = \
        f'https://raw.githubusercontent.com/altheaden/mache/' \
        f'{branch}/{remote_filepath}'
    local_filename = 'downloaded-script.py'
    print(f"Retrieving file from {url} and saving into {local_filename}")
    urlretrieve(url, local_filename)
    # execute the downloaded script
    commands = ['python3', local_filename] + args
    subprocess.run(commands, check=True, universal_newlines=True, shell=False)
    # TODO: Look into logging (redirecting) within subprocess.run call ???
    #       find example where stdout/stderr are files
    #       want to be able to redirect to either terminal or file depending
    #       on flags (like in mpas-tools) -> could be in script 2


if __name__ == '__main__':
    main()
