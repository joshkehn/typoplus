# -*- coding: utf-8 -*- #
import markdown
from . import typos

typeit = typos.TypoPlusExtension()
md = markdown.Markdown(extensions=[typeit, "extra"])

text = md.convert("""\
This is some text.

This is some text with 100x100px dimensions.

100x100 or 10x10 or 99x10 or 100dpi x 320dpi.

Multiple different types of comparisons can be used such as 10 altoids x 20 phones.

There are, of course, limitations here where a number (10) x (1) doesn't match. The system assumes numeric-typed suffixes.
""")

if __name__ == "__main__":
    print text