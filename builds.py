import sublime_plugin
import subprocess
import os


class GolimeBuildCommand(sublime_plugin.WindowCommand):

    """
    Command to run "go build", "go install", "go test" and "go clean"
    """

    def run(self, task='install', flags=None):
        cwd = self.window.active_view().file_name()
        cwd = os.path.dirname(cwd)
        print("cwd", cwd)

        try:
            _build = subprocess.Popen(
                ["go", task],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=cwd,
            )
            out, err = _build.communicate()
            print("code", _build.returncode, task)
            print("out", out)
            stderr = err.decode()
            if len(stderr) > 0:
                print("============== ERROR ==============")
                print(stderr)
                print("===================================")
        except Exception as exc:
            print("exc", exc, type(exc))
