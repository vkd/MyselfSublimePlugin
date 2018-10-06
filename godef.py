import sublime
import sublime_plugin
import subprocess

import json

# from .cmd import run_cmd


class GoLimeGodefCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if not filename.endswith(".go"):
            print("Allowed only for go files")
            return

        x = None
        for s in self.view.sel():
            x = s.a
            break

        if x is None:
            print("Not selected")
            return

        isFinded = self.defGodef(filename, x)
        if isFinded:
            return

        self.defGogetdoc(filename, x)

    def defGogetdoc(self, filename, x):
        out, _ = subprocess.Popen(["gogetdoc", "-json", "-pos", filename + ":#" + str(x)], stdout=subprocess.PIPE).communicate()
        out = out.decode("utf-8")
        if out == "":
            print("Empty result on gogetdoc")
            # self.defGodef(filename, x)
            return
        try:
            j = json.loads(out)
        except Exception as e:
            print("Wrong output: ", out)
            print("Exception: ", e)
            return
        pos = j["pos"]
        if pos == "":
            print("declaration not found: ", j)
            return
        self.view.window().open_file(pos, sublime.ENCODED_POSITION)
        # print("godef:", j)

        # res = run_cmd("godef", {})
        # print("godef:", res)

    def defGodef(self, filename, x):
        pcmd = subprocess.Popen(["godef", "-f", filename, "-o", str(x)], stdout=subprocess.PIPE)
        out, _ = pcmd.communicate()
        out = out.decode("utf-8")
        if pcmd.returncode != 0:
            print("wrong return code", pcmd.returncode)
            return False
        if out == "":
            return False
        print("out", out)  # parseLocalPackage error: no more package files found
        self.view.window().open_file(out, sublime.ENCODED_POSITION)
        return True
