#!/usr/bin/env python3
import argparse
import os
import platform
import subprocess
import sys
from urllib.request import Request, urlopen


def main():
    # install conda
    #    need to parse arguments to get conda path
    # install mache
    #    need to parse arguments to install local vs conda mache ?
    # begin deployment
    #    send the rest of the arguments to the next script (bootstrap)
    args = parse_args()
    print(f"DEBUG original args: {args}")
    options = vars(args)
    print(f"DEBUG var args: {options}")
    build_env(options)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Deploy a mache conda environment')
    parser.add_argument("--conda", dest="conda_base",
                        help="Path to the conda base")
    parser.add_argument("--spec-file", dest="spec_file",
                        help="Spec file with list of packages to install")
    parser.add_argument("--software-name", dest="software_name",
                        help="Name of the software to be deployed")

    args = parser.parse_args(sys.argv[1:])
    return args


def build_env(options):
    conda_base = get_conda_base(options['conda_base'])
    print(f"DEBUG conda base for installing miniforge: {conda_base}")
    activate_base = \
        f'source {conda_base}/etc/profile.d/conda.sh && conda activate'
    install_miniforge(conda_base, activate_base, None)
    print('DEBUG: running coda commands to build env')
    commands = \
        f'{activate_base} && ' \
        f'conda config --add channels conda-forge && ' \
        f'conda config --set channel_priority strict && ' \
        f'conda create -y -n begin_mache_deploy --file {options["spec_file"]}'
    subprocess.run(commands, check=True, universal_newlines=True, shell=True)


def get_conda_base(conda_base, shared=False, warn=False):
    # TODO: add config back
    """
    Get the absolute path to the files for the conda base environment

    Parameters
    ----------
    conda_base : str
        The relative or absolute path to the conda base files

    config : ConfigParser
        Config object

    shared : bool, optional
        Whether we are working in a shared conda environment

    warn : bool, optional
        Whether to print a warning that the conda path was not supplied

    Returns
    -------
    conda_base : str
        Path to the conda base environment
    """

    # if shared:
    #     conda_base = config.get('paths', 'polaris_envs')
    if conda_base is None:
        if 'CONDA_EXE' in os.environ:
            # if this is a test, assume we're the same base as the
            # environment currently active
            conda_exe = os.environ['CONDA_EXE']
            conda_base = os.path.abspath(
                os.path.join(conda_exe, '..', '..'))
            if warn:
                print(f'\nWarning: --conda path not supplied.  Using conda '
                      f'installed at:\n'
                      f'   {conda_base}\n')
        else:
            raise ValueError('No conda base provided with --conda and '
                             'none could be inferred.')
    # handle "~" in the path
    conda_base = os.path.abspath(os.path.expanduser(conda_base))
    return conda_base


def install_miniforge(conda_base, activate_base, logger):
    """
    Install Miniforge if it isn't installed already

    Parameters
    ----------
    conda_base : str
        Absolute path to the conda base environment files

    activate_base : str
        Command to activate the conda base environment

    logger : logging.Logger
        The logger for output
    """

    if not os.path.exists(conda_base):
        print('Installing Miniforge3')
        if platform.system() == 'Darwin':
            system = 'MacOSX'
        else:
            system = 'Linux'
        miniforge = f'Miniforge3-{system}-x86_64.sh'
        url = f'https://github.com/conda-forge/miniforge/releases/latest/download/{miniforge}'  # noqa: E501
        print(url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        f = urlopen(req)
        html = f.read()
        with open(miniforge, 'wb') as outfile:
            outfile.write(html)
        f.close()

        command = f'/bin/bash {miniforge} -b -p {conda_base}'
        subprocess.run(
            command, check=True, universal_newlines=True, shell=True)
        os.remove(miniforge)

    print('Doing initial setup\n')
    commands = f'{activate_base} && ' \
               f'conda config --add channels conda-forge && ' \
               f'conda config --set channel_priority strict && ' \
               f'conda update -y --all && ' \
               f'conda init --no-user'
    print(f"DEBUG Running commands: {commands}")
    subprocess.run(commands, check=True, universal_newlines=True, shell=True)
    print('DEBUG: completed miniforge setup')


if __name__ == '__main__':
    main()
