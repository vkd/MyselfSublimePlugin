# import sublime
import sublime_plugin

from . import cmd


class GoLimeAddTestsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()

        if not filename.endswith(".go"):
            print("Available only for *.go files")
            return

        funcname = None
        for s in self.view.sel():
            funcname = self.view.substr(self.view.word(s))
            break

        if funcname is None:
            print("Funcname not found")
            return

        # print("funcname", funcname)
        # return

        res = cmd.run_cmd("gotest", {
            "file": filename,
            "function": funcname,
        })
        testpaths = res["test_files"]
        if testpaths is not None and len(testpaths) > 0:
            self.view.window().open_file(testpaths[0])
        print(res)
