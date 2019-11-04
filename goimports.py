import sublime
import sublime_plugin
import subprocess


class GoImportsListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        filename = view.file_name()
        if not filename.endswith(".go"):
            return
        view.run_command("go_imports")


class GoImportsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        goimports_cmd(self.view, edit)


def goimports_cmd(view, edit):
    filename = view.file_name()
    if filename == "":
        print("Empty filename")
        return
    try:
        region = sublime.Region(0, view.size())
        content = view.substr(region)
        p = subprocess.Popen(["goimports", "-srcdir", filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # p.stdin.write(content)
        out, _ = p.communicate(input=content.encode())
        out = out.decode("utf-8")
        # out, _ = subprocess.Popen(["goimports", "-srcdir", filename], stdout=subprocess.PIPE).communicate()
        # print("saved:", out)
        view.replace(edit, region, out)
    except Exception as e:
        print("Exception: ", e)
        return
