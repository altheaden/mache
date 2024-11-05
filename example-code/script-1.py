#!/usr/bin/env python3
from urllib.request import urlretrieve


def main():
    # get the general script
    # make call and send arguments to general script
    filename = 'deploy/shared.py'
    # TODO: We probably want a better way of doing this, such as to make sure
    # TODO: we are getting this from the correct branch and not just from main
    branch = 'develop'  # (low priority) add cmd line arg to change maybe
    url = f'https://raw.githubusercontent.com/altheaden/mache/{branch}/{filename}'
    print(url)
    urlretrieve(url, filename)
    # execute the configure script. Send the software name (e.g., polaris)
    name = 'test'
    # option: make directory and download other support files (such as shared)


if __name__ == '__main__':
    main()
