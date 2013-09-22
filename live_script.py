import os
import subprocess

import sublime
import sublime_plugin


class LiveScript(sublime_plugin.TextCommand):

    SETTINGS = sublime.load_settings('LiveScript.sublime-settings')
    WINDOW_NAME = 'livescript_output'

    def run(self, edit):
        text = self.text_to_compile()
        text = text.encode('utf8')
        window = self.view.window()
        js, error = self.compile(text)
        self.write_to_window(window, edit, js, error)

    def args(self):
        settings_lsc = self.SETTINGS.get('livescript_bin')
        lsc = self.parse_lsc(settings_lsc)
        return lsc, '--stdin', '--compile', '--bare'

    def compile(self, text):
        path = self.path()
        args = self.args()

        try:
            return self.execute_command(path, args, text)
        except OSError as e:
            sublime.status_message(str(e))
            return '', str(e)

    def parse_lsc(self, raw_lsc):
        if raw_lsc == '':
            if sublime.platform() == 'windows':
                return 'lsc.cmd'
            else:
                return 'lsc'
        else:
            return raw_lsc

    def execute_command(self, path, args, text):
        if sublime.platform() == 'windows':
            env = None
        else:
            env = {'PATH': path}
        proc = subprocess.Popen(args, stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                env=env)

        return proc.communicate(text)

    def path(self):
        lsc = self.SETTINGS.get('livescript_path')
        path = os.getenv('PATH')

        return os.pathsep.join(filter(None, (path, lsc)))

    def text_selected(self):
        return any(not selected.empty() for selected in self.view.sel())

    def text_to_compile(self):
        if self.text_selected():
            region = self.view.sel()[0]
        else:
            region = sublime.Region(0, self.view.size())

        return self.view.substr(region)

    def write_to_panel(self, panel, edit, text):
        panel.set_read_only(False)
        panel.insert(edit, 0, text)
        panel.sel().clear()
        panel.set_read_only(True)

    def write_to_window(self, window, edit, js, error):
        panel = window.get_output_panel(self.WINDOW_NAME)
        panel.set_syntax_file('Packages/JavaScript/JavaScript.tmLanguage')

        text = js or error
        text = text.decode('utf8')

        self.write_to_panel(panel, edit, text)

        window.run_command('show_panel',
                           {'panel': 'output.{0}'.format(self.WINDOW_NAME)})
