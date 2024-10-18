#!/usr/bin/env python3
import argparse
import subprocess
import sys


def main():
    # install conda
    #    need to parse arguments to get conda path
    # install mache
    #    need to parse arguments to install local vs conda mache ?
    # begin deployment
    #    send the rest of the arguments to the next script (bootstrap)
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


def check_call(commands, env=None, logger=None):
    command_list = commands.replace(' && ', '; ').split('; ')
    print_command = '\n   '.join(command_list)
    if logger is None:
        print(f'\n Running:\n   {print_command}\n')
    else:
        logger.info(f'\nrunning:\n   {print_command}\n')

    if logger is None:
        process = subprocess.Popen(commands, env=env, executable='/bin/bash',
                                   shell=True)
        process.wait()
    else:
        process = subprocess.Popen(commands, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, env=env,
                                   executable='/bin/bash', shell=True)
        stdout, stderr = process.communicate()

        if stdout:
            stdout_decoded = stdout.decode('utf-8')
            for line in stdout_decoded.split('\n'):
                logger.info(line)
        if stderr:
            stderr_decoded = stderr.decode('utf-8')
            for line in stderr_decoded.split('\n'):
                logger.error(line)

    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, commands)


if __name__ == '__main__':
    main()
