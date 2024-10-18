#!/usr/bin/env python3
import argparse
import subprocess
import sys

from deploy.shared import check_call


def main():
    # install conda
    #    need to parse arguments to get conda path
    # install mache
    #    need to parse arguments to install local vs conda mache ?
    # begin deployment
    #    send the rest of the arguments to the next script (bootstrap)
    # could url retrieve files needed (such as shared)
    args = parse_args()
    print(args)
    options = vars(args)
    print(options)
    build_env(options)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Deploy a mache conda environment')
    parser.add_argument("--conda", dest="conda_base",
                        help="Path to the conda base")
    parser.add_argument("--spec-file", dest="spec_file",
                        help="Spec file with list of packages to install")

    args = parser.parse_args(sys.argv[1:])
    return args


def build_env(options):
    commands = \
        f'conda config --add channels conda-forge && ' \
        f'conda config --set channel_priority strict && ' \
        f'conda create -y -n begin_mache_deploy --file {options["spec_file"]}'
    check_call(commands)


if __name__ == '__main__':
    main()
