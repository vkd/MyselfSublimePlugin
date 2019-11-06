import sublime
import sublime_plugin
import subprocess

from . import cmd

GOLIME_CMD = ["golime", "-s"]

_playground = None


def start_golime():
    def _start():
        global _playground
        _playground = subprocess.Popen(GOLIME_CMD)

        try:
            _playground.wait(timeout=0.5)
        except subprocess.TimeoutExpired:
            pass

        out = cmd.run_cmd("version", {})
        print("golime subprocess started:", out["version"])

    sublime.set_timeout_async(_start, 0)


def stop_golime():
    if _playground is not None:
        try:
            res = cmd.run_cmd("exit", {})
            print("Stop golime:", res)
        except Exception as e:
            print("Exception of 'exit' cmd", e)

        try:
            _playground.kill()
            print("golime stopped!")
        except Exception as e:
            print("unknown error", e)


class GoLimeReloadCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        sublime.status_message("Restarting golime...")
        stop_golime()
        start_golime()
        sublime.status_message("Golime is restarted")
