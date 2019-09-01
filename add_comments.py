import sublime
import sublime_plugin

from . import cmd

class GoLimeAddCommentsCommand(sublime_plugin.TextCommand):
    filename = None

    def run(self, edit):
        self.filename = self.view.window().active_view().file_name()
        if not self.filename.endswith(".go"):
            print("Allowed only '.go' file: ", self.filename)
            return
        res = cmd.run_cmd("add_comments", {
            "file": self.filename,
            "isRuneCount": True,
        })
        if res["status"] != "ok":
            print("Wrong result status:", res)
            return
        print("ok", res)
        if res["result"] is not None:
            for l in res["result"]:
                self.view.insert(edit, l["pos"], l["text"])
