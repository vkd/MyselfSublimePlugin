# import sublime
import sublime_plugin


class GoLimePlaygroundCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        imp = self.view.find("^import", 0)
        print(imp)
