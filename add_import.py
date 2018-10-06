import sublime
import sublime_plugin

from . import cmd


class GoLimeAddImportEditCommand(sublime_plugin.TextCommand):
    def run(self, edit, **res):
        print("result text=", res)
        self.view.replace(edit, sublime.Region(res["l_pos"], res["r_pos"]), res["text"])


class GoLimeAddImportCommand(sublime_plugin.TextCommand):
    filename = None

    def run(self, edit):
        self.filename = self.view.window().active_view().file_name()
        if not self.filename.endswith(".go"):
            print("Allowed only '.go' file: ", self.filename)
            return
        sublime.set_timeout_async(self._import, 0)

    def _import(self):
        imports = cmd.run_cmd("imports", {})
        imports = imports["imports"]

        def on_done(i):
            if i >= 0:
                # needs for autoreload view
                # self.view.window().active_view().run_command("save", {})

                res = cmd.run_cmd(
                    "add_import",
                    {
                        "import": imports[i],
                        "file": self.filename,
                    },
                )
                if res["status"] != "ok":
                    print("Wrong result status:", res)
                    return

                res = res["result"]
                self.view.run_command("go_lime_add_import_edit", res)

        self.view.window().show_quick_panel(
            imports,
            on_done,
            sublime.MONOSPACE_FONT
        )
