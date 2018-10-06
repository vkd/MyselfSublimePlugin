import sublime
import sublime_plugin
import os


class GoLimeDeleteFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if filename is not None:
            self._delete_dialog(filename)
        else:
            self._close_dialog(self.view.name())

    def _delete_dialog(self, filename):
        if sublime.ok_cancel_dialog("You want to delete %s file?" % (filename)):
            os.remove(filename)
            self._close()
            print("Deleted", filename)

    def _close_dialog(self, filename):
        if sublime.ok_cancel_dialog("You want to close %s file?" % (filename)):
            self._close()
            print("Closed", filename)

    def _close(self):
        self.view.set_scratch(True)
        self.view.window().run_command("close")
