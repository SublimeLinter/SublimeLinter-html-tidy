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
    if Linter.which('tidy5'):
        cmd = 'tidy5 -errors -quiet -utf8'
    else:
        cmd = 'tidy -errors -quiet -utf8'
    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR
