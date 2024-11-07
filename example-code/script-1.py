#!/usr/bin/env python3
from urllib.request import urlretrieve


def main():
    remote_filepath = 'mache/deploy/script-2.py'  # path to file on GitHub
    branch = 'develop'  # TODO: (low priority) add cmd line arg to change?
    url = \
        (f'https://raw.githubusercontent.com/altheaden/mache/'
         f'{branch}/{remote_filepath}')
    local_filename = 'downloaded-script.py'
    print(f"Retrieving file from {url} and saving into {local_filename}")
    # NOTE: this will not overwrite an existing file. A file with the same
    #       filename will not be updated, the original will be preserved.
    urlretrieve(url, local_filename)
    # execute the downloaded script. Send the software name (e.g., polaris)
    # name = 'my-cool-software'


if __name__ == '__main__':
    main()
