#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2015-2017 The SublimeLinter Community
# Copyright (c) 2013-2014 Aparajita Fishman
#
# License: MIT
#

"""This module exports the HtmlTidy plugin class."""

from SublimeLinter.lint import Linter, util


class HtmlTidy(Linter):
    """Provides an interface to tidy."""

    syntax = 'html'
    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR

    def cmd(self):
        """Return a tuple with the command line to execute."""
        # Must return either a full path to a binary or an informal name
        # of an executable.
        executable = self.which('tidy5') or 'tidy'
        return [executable, '-errors', '-quiet', '-utf8']
