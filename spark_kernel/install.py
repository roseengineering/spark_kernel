
import json
import os
import sys
import getopt

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

language = "spark"

kernel_spec = {
    "argv": [sys.executable, "-m", __package__, "-f", "{connection_file}"],
    "language": language,
    "display_name": language.title()
}

def is_root():
    return os.geteuid() == 0


def install_my_kernel_spec(user, prefix):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_spec, f)
        KernelSpecManager().install_kernel_spec(
            td, language, user=user, replace=True, prefix=prefix)


def main(argv=[]):
    prefix = None
    user = not is_root()

    opts, _ = getopt.getopt(argv[1:], '', ['user', 'prefix='])
    for k, v in opts:
        if k == '--user':
            user = True
        elif k == '--prefix':
            prefix = v
            user = False

    install_my_kernel_spec(user=user, prefix=prefix)


if __name__ == '__main__':
    main(argv=sys.argv)

