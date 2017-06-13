
import os
import tempfile
import pexpect
from pexpect.replwrap import REPLWrapper
from ipykernel.kernelbase import Kernel

from .install import language

class Main(Kernel):
    implementation = language
    implementation_version = "1"
    banner = language.title()
    language_info = { 
        "name": language,
        "codemirror_mode": "clike",
    }

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        child = pexpect.spawn("spark-shell", echo=False, encoding='utf-8')
        child.timeout = 100000
        self.wrapper = REPLWrapper(child, "scala> ", None)

    def do_execute(self, code, silent, *args):
        code = code.rstrip()
        status = 'ok'
        if not silent and code:
            try:
                filename = tempfile.mktemp(suffix=language)
                with open(filename, "w") as f:
                    f.write(code)
                output = self.wrapper.run_command(":paste " + filename)
                os.remove(filename)
                output = output[output.find('\n') + 1:]
                output = output[output.find('\n') + 1:]
            except Exception as e:
                status = 'error'
                output = str(e)

            output = output.rstrip()
            stream_content = { 'name': 'stdout', 'text': output }
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': status, 'execution_count': self.execution_count,
                'payload': [], 'user_expressions': {}}


from ipykernel.kernelapp import IPKernelApp
IPKernelApp.launch_instance(kernel_class=Main)


