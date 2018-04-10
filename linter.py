from SublimeLinter.lint import Linter, util


class HtmlTidy(Linter):
    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'text.html.basic'
    }

    def cmd(self):
        """Return a tuple with the command line to execute."""
        # Must return either a full path to a binary or an informal name
        # of an executable.
        executable = self.which('tidy5') or 'tidy'
        return [executable, '-errors', '-quiet', '-utf8']
