#!/usr/bin/env python3

from pathlib import Path

from datetime import datetime
from pytz import timezone
tz = timezone('Europe/Moscow')

from markdown import markdown
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
#	WikiLinkExtension() #TODO: this needs to be configured and tested
]
# TODO: check out third party extensions like https://github.com/waylan/Python-Markdown/wiki/Third-Party-Extensions
# Especially PyEmbed, superscript, tilde, SmartSymbols, ProgressBar, magiclink
# Also, something for LaTeX

def filename_to_title(filename):
	circumcised = filename[:-len('.md')]
	return circumcised.replace('_', ' ')

def load_post(post_path):
	with post_path.open() as post_file:
		post = {
			'name' : filename_to_title(post_path.name),
			'posted' : datetime.fromtimestamp(post_path.stat().st_ctime, tz), 
			'modified' : datetime.fromtimestamp(post_path.stat().st_mtime, tz),
			'body' : ''.join(post_file.readlines()),
		}
		return post

def format_post(post):
	buf = '<div>\n'
	buf += '	<h3>' + post['name'] + '</h3>'
	buf += '	<h5>' + post['posted'].strftime('%c') + '</h5>'
	buf += '	<div>' + markdown(post['body'], extensions=markdown_extensions) + '</div>'
	buf += '</div>'
	return buf

class Blog:
	def __init__(self):
		this_file_path = Path(__file__).absolute()
		self.posts_path = this_file_path.parents[0] / 'posts'
		
	def get_posts(self):
		posts = [load_post(x) for x in self.posts_path.iterdir() if x.is_file() and x.name.endswith('.md')]
		posts_pretty = [format_post(x) for x in sorted(posts, key = lambda p:p['posted'], reverse = True)]
		page = ''
		page += '<div class="container">'
		page += '	<h1>SAMPLE BLOG</h1>\n'
		page += '	<div class="row">'
		#page += '		<div class="col-md-2 col-lg-2 hidden-lg-down">'
		#page += '			<img src="http://i.imgur.com/dMmQkJa.gif" alt="How do I CSS" width="100%" height="auto">'
		#page += '		</div>'
		page += '		<div class="col-md-10 col-lg-10 col-sm-12 col-xs-12">'
		page += '			<h2>Posts</h2>\n'
		page += 			'\n<br>\n'.join(posts_pretty)
		page += '		</div>'
		page += '	</div>'
		page += '</div>'
		return page

	def get_head(self):
		buf = ''
		buf += '<!-- Latest compiled and minified CSS -->'
		buf += '<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">'
		#buf += '<link rel="stylesheet" href="https://rawgit.com/richleland/pygments-css/master/vim.css">'
		buf += '<link rel="stylesheet" href="https://rawgit.com/richleland/pygments-css/master/autumn.css">'

		buf += '<!-- jQuery library -->'
		buf += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>'

		buf += '<!-- Latest compiled JavaScript -->'
		buf += '<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>'
		return buf
