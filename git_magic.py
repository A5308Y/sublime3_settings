import sublime, sublime_plugin

class GitMagicCommand(sublime_plugin.WindowCommand):
  def run(self):
    print(self.window.get_layout())
    # run git_command: open modified files in second window
    # run git list modified in first window
