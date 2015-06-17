# command: vi_set_bookmark
# command: set_motion {"inclusive": true, "motion": "vi_move_to_brackets", "motion_args": {"repeat": 1}}
# command: set_action_motion {"action": "vi_right_delete", "motion": null}
# command: vi_select_bookmark
# command: set_action_motion {"action": "vi_right_delete", "motion": null}

# class ViSetBookmark(sublime_plugin.TextCommand):
#     def run(self, edit, character):
#         sublime.status_message("Set bookmark " + character)
#         self.view.add_regions("bookmark_" + character, [s for s in self.view.sel()],
#             "", "", sublime.PERSISTENT | sublime.HIDDEN)

# class ViSelectBookmark(sublime_plugin.TextCommand):
#     def run(self, edit, character, select_bol=False):
#         self.view.run_command('select_all_bookmarks', {'name': "bookmark_" + character})
#         if select_bol:
#             sels = list(self.view.sel())
#             self.view.sel().clear()
#             for r in sels:
#                 start = self.view.line(r.a).begin()
#                 self.view.sel().add(sublime.Region(start, start))
import sublime, sublime_plugin

class DeleteMatchingBracketsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        character = "p"
        self.view.add_regions("bookmark_" + character, [s for s in self.view.sel()], "", "", sublime.PERSISTENT | sublime.HIDDEN)
        self.view.run_command('set_motion', {"inclusive": True, "motion": "vi_move_to_brackets", "motion_args": {"repeat": 1}})
        self.view.run_command('set_action_motion', {"action": "vi_right_delete", "motion": None})
        self.view.run_command('select_all_bookmarks', {'name': "bookmark_" + character})
        self.view.run_command('set_action_motion', {"action": "vi_right_delete", "motion": None})
