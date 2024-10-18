#!/usr/bin/env python3
import subprocess


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
