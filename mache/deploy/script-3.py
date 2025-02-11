#!/usr/bin/env python3
import argparse
import sys

from shared import check_call


def main():
    args = parse_args()
    # show --help options, etc
    print(args)  # TODO: debug
    options = vars(args)
    print(options)  # TODO: debug
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
