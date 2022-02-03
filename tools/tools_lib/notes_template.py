"""
These are the templates used for the notes files.
"""

TMPL_HEADER = """---
release:
  release_date: XXXX-XX-XX
  text: |
    TEXT_TO_REPLACE

  import_system_requirements: XX.X

notes:
"""

REQUIREMENTS_IMPORT = {"release": "91.0",
                       "beta": "86.0beta",
                       }

TMPL_RELEASE_TEXT = """**For more on all the new features in Thunderbird 91, see
[New in Thunderbird 91.0](https://support.mozilla.org/en-US/kb/new-thunderbird-91/).**

**System Requirements:** [Details](/en-US/thunderbird/91.0/system-requirements/)

- Windows: Windows 7 or later
- Mac: macOS 10.12 or later
- Linux: GTK+ 3.14 or higher
"""

TMPL_BETA_TEXT = """Coming soon!"""


