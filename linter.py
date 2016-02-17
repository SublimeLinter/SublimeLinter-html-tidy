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


class HtmlTidy(Linter):

    """Provides an interface to tidy."""

    syntax = 'html'
    executable = 'tidy'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 4.9'
    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR

    def cmd(self):
        """Return a tuple with the command line to execute."""
        command = [self.executable_path, '-errors', '-quiet', '-utf8']
        if Linter.which('tidy5'):
            command[0] = Linter.which('tidy5')
        else:
            command[0] = Linter.which('tidy')
        return command
