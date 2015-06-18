#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright © 2015 The SublimeLinter Community
#
# License: MIT
#

"""This module exports the HtmlTidy plugin class."""

from SublimeLinter.lint import Linter, util
import sublime


class HtmlTidy(Linter):

    """Provides an interface to tidy."""

    syntax = 'html'
    executable = 'sh'
    if sublime.platform() == 'windows':
        executable = 'cmd'

    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR

    def cmd(self):
        command = [self.executable_path, '-errors', '-quiet', '-utf8']
        if Linter.which('tidy5'):
            command[0] = Linter.which('tidy5')
        return command
