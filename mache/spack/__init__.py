import os as os
import subprocess as subprocess

import yaml as yaml
from jinja2 import Template as Template

from mache.machine_info import (
    MachineInfo as MachineInfo,
)
from mache.machine_info import (
    discover_machine as discover_machine,
)
from mache.spack.config_machines import (
    config_to_shell_script as config_to_shell_script,
)
from mache.spack.env import (
    get_modules_env_vars_and_mpi_compilers as get_modules_env_vars_and_mpi_compilers,  # noqa: E501
)
from mache.spack.env import (
    make_spack_env as make_spack_env,
)
from mache.spack.script import get_spack_script as get_spack_script
