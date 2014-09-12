# coding=utf-8

from __future__ import unicode_literals
import re
import markdown
from markdown.preprocessors import Preprocessor

EXTENSIONS = (
    ("multi", r'(?P<dim1>\b\d+\s*[\w.]*\s*)(x)((?P<dim2>\s*\d+\s*[\w.]*\b))', '&times;'),
)

REPLACEMENTS = (
    ("emdash", r"—", "&#x200A;&mdash;&#x200A;"),
    ("endash", r"–", "&ndash;"),
    ("times", r"×", "&times;"),
    ("ldquo", r"“", "&ldquo;"),
    ("rdquo", r"”", "&rdquo;"),
    ("lsquo", r"‘", "&lsquo;"),
    ("rsquo", r"’", "&rsquo;"),
)

class SubProcess (Preprocessor):

    def process_line (self, text):
        return self.pattern.sub(self.repl, text)

    def run (self, lines):
        return [ self.process_line(line) for line in lines ]

class TypoSubPost (SubProcess):

    def __init__ (self, *args, **kwargs):
        self.pattern = re.compile(kwargs.pop("pattern", None))
        self.repl = "\g<dim1>{}\g<dim2>".format(kwargs.pop("repl", None))
        return super(TypoSubPost, self).__init__(*args, **kwargs)

class StraightSubPost (SubProcess):

    def __init__ (self, *args, **kwargs):
        self.pattern = re.compile(kwargs.pop("pattern", None))
        self.repl = kwargs.pop("repl")
        return super(StraightSubPost, self).__init__(*args, **kwargs)

class TypoPlusExtension (markdown.extensions.Extension):
    """Adds a variety of typographic enhancements to Markdown."""

    def extendMarkdown (self, md, glob):
        for name, pattern, repl in EXTENSIONS:
            md.preprocessors.add(name, TypoSubPost(pattern=pattern, repl=repl), "_end")
        for name, pattern, repl in REPLACEMENTS:
            md.preprocessors.add(name, StraightSubPost(pattern=pattern, repl=repl), "_end")


def makeExtension(configs={}):
    return TypoPlusExtension(configs=dict(configs))
