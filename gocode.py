# import sublime
# import sublime_plugin
# import subprocess

# import json

# # from .cmd import run_cmd


# class GoLimeGocode(sublime_plugin.EventListener):
#     def on_query_completions(self, view, prefix, locations):
#         print("competitions golime gocode", prefix, locations)
#         filename = view.file_name()
#         if not filename.endswith(".go"):
#             print("Allowed only for go files")
#             return

#         x = None
#         for s in view.sel():
#             x = s.a
#             break

#         if x is None:
#             print("Not selected")
#             return

#         self.gocode(filename, locations[0])
#         return ([["FileSet", "hello world"], ["Files", "allfiles"]], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

#         # if isFinded:
#         #     return

#         # self.defGogetdoc(filename, x)

#     def gocode(self, filename, pos):
#         commade = ["gocode", "-f=json", "autocomplete", filename, "c" + str(pos)]
#         print(' '.join(commade))
#         out, _ = subprocess.Popen(commade, stdout=subprocess.PIPE).communicate()
#         out = out.decode("utf-8")
#         if out == "":
#             print("Empty result on gocode")
#             return
#         try:
#             j = json.loads(out)
#         except Exception as e:
#             print("Wrong output: ", out)
#             print("Exception: ", e)
#             return
#         print("output:", j)
#         # pos = j["pos"]
#         # if pos == "":
#         #     print("declaration not found: ", j)
#         #     return
#         # self.view.window().open_file(pos, sublime.ENCODED_POSITION)
#         # print("godef:", j)

#         # res = run_cmd("godef", {})
#         # print("godef:", res)

