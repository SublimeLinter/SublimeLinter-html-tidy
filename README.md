SublimeLinter-html-tidy
=========================

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to tidy (either the [html4](http://tidy.sourceforge.net) or [html5](http://w3c.github.io/tidy-html5/) version). It will be used with files that have the “HTML” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `tidy` is installed on your system.

- **Mac OS X** – `tidy` comes preinstalled on recent versions of Mac OS X. You can install a more recent version by using [Homebrew](http://brew.sh) and `brew install homebrew/dupes/tidy`.

- **Linux** – You should be able to install tidy using the system’s package manager. For example, on Debian-based systems (including Ubuntu), you can install with `sudo apt-get install tidy`.

- **Windows** – A Windows binary is available [here](http://www.paehl.com/open_source/?HTML_Tidy_for_Windows).

On Mac OS X and Linux, you can also try building the experimental [html5 tidy](https://github.com/w3c/tidy-html5). A Windows binary with HTML5 support is available [here](http://tidybatchfiles.info/).

Once tidy is installed, if the SublimeLinter-html-tidy plugin is not yet installed, you can proceed to install it.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `html-tidy`. Among the entries you should see `SublimeLinter-html-tidy`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

`tidy` must be configured via command line arguments. You can use the `"args"` linter setting to pass arguments to tidy.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
