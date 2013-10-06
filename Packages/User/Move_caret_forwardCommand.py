import sublime, sublime_plugin

class Move_multiCommand(sublime_plugin.TextCommand):
    def run(self, edit, by="characters", amount=1):

        (row,col) = self.view.rowcol(self.view.sel()[0].begin())

        if by == "lines":
        	row += amount
        else:
        	col += amount

        target = self.view.text_point(row, col)

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(target))
        self.view.show(target)