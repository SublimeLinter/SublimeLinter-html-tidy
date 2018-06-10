SublimeLinter-html-tidy
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-html-tidy.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-html-tidy)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to tidy (either the [html4](http://tidy.sourceforge.net) or [html5](http://w3c.github.io/tidy-html5/) version). It will be used with files that have the “HTML” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please install via [Package Control](https://sublime.wbond.net/installation).

Before installing this plugin, you must ensure that `tidy` or `tidy5` are installed on your system. `tidy5` will be used over `tidy` if available.

- **Mac OS X** – `tidy` comes preinstalled on recent versions of Mac OS X. You can install the [html5](https://github.com/w3c/tidy-html5) version by using [Homebrew](http://brew.sh) and `brew install tidy-html5`.

- **Linux** – You should be able to install tidy using the system’s package manager.

- **Windows** – Windows binaries are available for the [html5](http://tidybatchfiles.info/) version.

In order for `tidy` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter.
