import sublime
import sublime_plugin
import subprocess
import os

from .cmd import run_cmd


_playground = None
GOLIME_CMD = "golime"
GOLIME_DAEMON_URL = "http://localhost:8601/cmd"


def plugin_loaded():
    start_golime()


def start_golime():
    def _start():
        global _playground
        _playground = subprocess.Popen(GOLIME_CMD)

        try:
            _playground.wait(timeout=1)
        except subprocess.TimeoutExpired:
            pass

        out, err = run_cmd("version", {})
        print("golime subprocess started:", out["version"])

    sublime.set_timeout_async(_start, 0)


def stop_golime():
    if _playground is not None:
        try:
            _playground.kill()
            print("golime stopped")
        # except subprocess.TimeoutExpired as e:
        #     print("golime process not found", e)
        except Exception as e:
            print("unknown error", e)


def plugin_unloaded():
    stop_golime()


class GoLimeGodefCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        print(view.show_popup('''<body id="my-plugin-feature">
    <style>
        div.error {
            background-color: red;
            padding: 5px;
        }
    </style>
    <div class="error"></div>
</body>''', 0))
        # ------------------------
        # filename = self.window.active_view().file_name()
        # if not filename.endswith(".go"):
        #     print("Allowed only '.go' file: ", filename)
        #     return

        # (imports, err) = run_cmd("imports", {})
        # if err is not None:
        #     print("error on run 'import' cmd: ", err)
        #     return`

        # imports = imports["imports"]

        # def on_done(i):
        #     if i >= 0:
        #         # needs for autoreload view
        #         self.window.active_view().run_command("save", {})

        #         (res, err) = run_cmd(
        #             "add_import",
        #             {
        #                 "import": imports[i],
        #                 "file": filename,
        #             },
        #         )
        #         if err is not None:
        #             print("Error on add import: ", err)
        #             return
        #         print("Add import result: ", res)

        # self.window.show_quick_panel(
        #     imports,
        #     on_done,
        #     sublime.MONOSPACE_FONT
        # )

        # ------------------------
        # sublime.message_dialog("Error of you genetic code")
        # sublime.run_command("go_lime_show_log", {"name": "application"})
        # self.view.insert(edit, 0, "Hello, World!")


class GoLimeReloadCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        stop_golime()
        start_golime()


class GoLimeDeleteFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if sublime.ok_cancel_dialog("delete " + filename + "?"):
            os.remove(filename)
            self.view.set_scratch(True)
            self.view.window().run_command("close")
            print("Deleted", filename)
