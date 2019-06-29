import sublime
import sublime_plugin


class EvalCustomPyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            ss = self.view.substr(s)
            res = eval(ss)
            res = int(res)
            res = str(res)
            self.view.replace(edit, s, res)
        # 9/2
        # 4/2
        # 100/2
        # self.view.replace(edit, sublime.Region(res["l_pos"], res["r_pos"]), res["text"])
