import sublime, sublime_plugin

class DeleteMatchingBracketsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        character = "p"
        self.view.add_regions("bookmark_" + character, [s for s in self.view.sel()], "", "", sublime.PERSISTENT | sublime.HIDDEN)
        self.view.run_command('set_motion', {"inclusive": True, "motion": "vi_move_to_brackets", "motion_args": {"repeat": 1}})
        self.view.run_command('set_action_motion', {"action": "vi_right_delete", "motion": None})
        self.view.run_command('select_all_bookmarks', {'name': "bookmark_" + character})
        self.view.run_command('set_action_motion', {"action": "vi_right_delete", "motion": None})
