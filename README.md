# LiveScript Sublime Text 2 package.

## Inspiration

This is greatly inspired by [@surjikal][surjikal]'s [Coffee Compile][coffee-compile]
and [my own][joneshf] [Roy Compile][roy-compile]

## Features

* Syntax highlighting
* Transpilation to js
* Snippets

## Usage

Compile the entire file by not selecting any text (or all the text).
Compile a section by selecting just that section.
Keyboard shortcut `Alt-Shift-L`

Command Palette integration `Live Script`

Context menu `right click`

## Install

### Package Control

This is not the livescript package currently in package control.

To install this package

1. Add this repository using the command `Package Control: Add Repository`
1. Paste this url into sublime: `https://github.com/joneshf/sublime-livescript`
1. Install the package like normal (`Package Control: Install Package` -> `sublime-livescript`)

### Manual

Clone this repository from your Sublime packages directory:

#### Linux

```
$ cd ~/.config/sublime-text-2/Packages
$ git clone https://github.com/joneshf/sublime-livescript
```

#### Macosx (untested)

```
$ cd "~/Library/Application Support/Sublime Text 2/Packages"
$ git clone https://github.com/joneshf/sublime-livescript
```

#### Windows (untested)

```
$ cd "%APPDATA%\Sublime Text 2\Packages"
$ git clone https://github.com/joneshf/sublime-livescript
```

## Contributing

Pretty much anything goes with a few exceptions.

* Additions must be directly related to the LiveScript language.
* Snippet files __MUST__ use tabs.  This is to ensure uniform snippet insertion.

[surjikal]: https://github.com/surjikal
[coffee-compile]: https://github.com/surjikal/sublime-coffee-compile
[joneshf]: https://github.com/joneshf
[roy-compile]: https://github.com/joneshf/RoyCompile
