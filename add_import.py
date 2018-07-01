import sublime
import sublime_plugin

from .cmd import run_cmd


class GoLimeAddImportCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if not filename.endswith(".go"):
            print("Allowed only '.go' file: ", filename)
            return

        (imports, err) = run_cmd("imports", {})
        if err is not None:
            print("error on run 'import' cmd: ", err)
            return

        imports = imports["imports"]

        def on_done(i):
            if i >= 0:
                # needs for autoreload view
                self.window.active_view().run_command("save", {})

                (res, err) = run_cmd(
                    "add_import",
                    {
                        "import": imports[i],
                        "file": filename,
                    },
                )
                if err is not None:
                    print("Error on add import: ", err)
                    return
                print("Add import result: ", res)

        self.window.show_quick_panel(
            imports,
            on_done,
            sublime.MONOSPACE_FONT
        )

        # sublime.message_dialog("Error of you genetic code")
        # sublime.run_command("go_lime_show_log", {"name": "application"})
        # self.view.insert(edit, 0, "Hello, World!")
