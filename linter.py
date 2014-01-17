#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the HtmlTidy plugin class."""

from SublimeLinter.lint import Linter, util


class HtmlTidy(Linter):

    """Provides an interface to tidy."""

    syntax = ('html', 'html 5')
    cmd = 'tidy -errors -quiet -utf8'
    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR

    def communicate(self, cmd, code=''):
        """
        If the code that is linted is an HTML fragment, 
        we wrap it into a valid HTML document.
        """
        if code.find('<html') == -1 and code.find('<body') == -1:
            code = \
                ("<!DOCTYPE html><html><head><title>Fragment</title></head><body>" + \
                "%s" + \
                "</body></html>") \
                % code

        return util.communicate(
            cmd,
            code,
            output_stream=self.error_stream,
            env=self.env)
