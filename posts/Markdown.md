Since there is a need for formatting one's text, markdown usage is a no-brainer.

In addition to markdown itself, highlighting code blocks is also desired.

Luckily, setting up both of those is pretty straightforward:

```dockerfile hl_lines="3 4"
...
RUN pip install \
	markdown \
	pygments \
	pytz
...

```


```python
from markdown import markdown
# Official extensions - https://pythonhosted.org/Markdown/extensions/
from markdown.extensions.abbr import AbbrExtension
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.meta import MetaExtension
from markdown.extensions.smarty import SmartyExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.wikilinks import WikiLinkExtension

markdown_extensions = [
	AbbrExtension(),
	FootnoteExtension(),
	TableExtension(),
	CodeHiliteExtension(),
	FencedCodeExtension(),
	MetaExtension(),
	SmartyExtension(),
	TocExtension(),
	WikiLinkExtension()
]

...

buf += '	<div>' + markdown(post['body'], extensions=markdown_extensions) + '</div>'
```

Markdown without extensions lacks lots of cool features. Some useful extentions are shipped with official package so we'll take some of those too. Also check out [list](https://github.com/waylan/Python-Markdown/wiki/Third-Party-Extensions) of third-party extensions --- there must be something useful there too.

Note that naming of classes there is somewhat random. Correct class names can be easily looked up like

```python
import markdown.extensions.abbr as extension_to_inspect
print(dir(extension_to_inspect))
```

Although passing string `'markdown.extensions.abbr'` instead of an actual instance would work too, it is [not](https://pythonhosted.org/Markdown/reference.html#extensions) the recommended way. Preferred way is to use instances. They can also be configured more easily.

Also, pygments only format code by providing HTML[^1] classes, some stylesheet to make use of those classes is to be provided separately.
```html
<link rel="stylesheet" href="https://rawgit.com/richleland/pygments-css/master/autumn.css">
```

*[HTML]: Hyper Text Markup Language

[^1]: Yeah, totally showing off them cool features[^2]
[^2]: This is not an alternative to actual tests. This *is* an alternative to their absence.
