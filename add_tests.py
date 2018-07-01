import sublime
import sublime_plugin

from .cmd import run_cmd


class GoLimeAddTestsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()

        if not filename.endswith(".go"):
            print("Available only for *.go files")
            return

        res, err = run_cmd("gotest", {
            "file": filename,
            "function": "Run",
        })
        if err is None:
            testpaths = res["test_files"]
            if testpaths is not None and len(testpaths) > 0:
                self.view.window().open_file(testpaths[0])
        print(res, err)
