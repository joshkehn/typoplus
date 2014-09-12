# coding=utf-8

from __future__ import unicode_literals
import markdown
from . import typos

typeit = typos.TypoPlusExtension()
md = markdown.Markdown(extensions=[typeit, "extra"])

text = md.convert("""\
This is some text.

“This is some text with 100x100px dimensions.”

This—I mean this—is an em-dash.

100x100 or 10x10 or 99x10 or 100dpi x 320dpi.

Multiple different types of comparisons can be used such as 10 altoids x 20 phones.

That’s ‘all’!

There are, of course, limitations here where a number (10) x (1) doesn't match.
""")

if __name__ == "__main__":
    print text