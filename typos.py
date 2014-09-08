# coding=utf-8

from __future__ import unicode_literals
import re
import markdown
from markdown.postprocessors import Postprocessor

EXTENSIONS = (
    ("multi", r'(?P<dim1>\b\d+\s*[\w.]*\s*)(x)((?P<dim2>\s*\d+\s*[\w.]*\b))', '&times;'),
    ("emdash", r'(?P<dim1>\w+)—(?P<dim2>\w+)', '&#x200A;&mdash;&#x200A;'),
    ("endash", r'(?P<dim1>\w+)–(?P<dim2>\w+)', '&ndash;')
)


class TypoSubPost (Postprocessor):

    def __init__ (self, *args, **kwargs):
        self.pattern = re.compile(kwargs.pop("pattern", None))
        self.repl = "\g<dim1>{}\g<dim2>".format(kwargs.pop("repl", None))
        return super(TypoSubPost, self).__init__(*args, **kwargs)

    def run (self, text):
        return self.pattern.sub(self.repl, text)


class TypoPlusExtension (markdown.extensions.Extension):
    """Adds a variety of typographic enhancements to Markdown."""

    def extendMarkdown (self, md, glob):
        for name, pattern, repl in EXTENSIONS:
            md.postprocessors.add(name, TypoSubPost(pattern=pattern, repl=repl), "_end")


def makeExtension(configs={}):
    return TypoPlusExtension(configs=dict(configs))
