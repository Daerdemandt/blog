#!/usr/bin/env python3

from pathlib import Path

from datetime import datetime
from pytz import timezone
tz = timezone('Europe/Moscow')

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
	buf += '	<div><pre>' + post['body'] + '</pre></div>'
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
		#page += '<h1>SAMPLE BLOG</h1>\n'
		#page += '<h2>Posts</h2>\n'
		page += '\n'.join(posts_pretty)
		return page

