#!/usr/bin/env python3
import http.server
import socketserver
from urllib.parse import parse_qsl as parse_query, urlparse as parse_url
from abc import abstractmethod, ABC as abstractclass
import json

class ContentEncoder(abstractclass):
	@abstractmethod
	def get_type():
		pass
	@abstractmethod
	def encode(self, content):
		pass

class JsonEncoder(ContentEncoder):
	def get_type(self):
		return 'application/json'
	def encode(self, content):
		return bytes(json.dumps(content), 'UTF-8')

class TextEncoder(ContentEncoder):
	def __init__(self, text_type='plain'):
		self.text_type = text_type
	def get_type(self):
		return 'text/' + self.text_type
	def encode(self, content):
		return bytes(str(content), 'UTF-8')

class HtmlEncoder(TextEncoder):
	def __init__(self):
		super().__init__('html')
	def set_head(self, head):
		self.head = head
	def encode(self, content):
		return super().encode('<!DOCTYPE html><html><head>' + self.head + '</head><body>' + str(content) + '</body></html>')

def run_server(info, port, encoder = JsonEncoder(), response_cache = {}):
	class MyHandler(http.server.SimpleHTTPRequestHandler):
		def respond(self, content, code=200):
			self.send_response(code)
			self.send_header("Content-type", encoder.get_type())
			self.end_headers()
			self.wfile.write(encoder.encode(content))
	
		def not_implemented(self):
			self.respond({'error':'{} not implemented'.format(self.path)}, code=404)
	
		def not_found(self, key = False):
			key = key or self.path
			self.respond({'error': key + ' not found'}, code=404)
	
		def do_GET(self):
			request = parse_url(self.path).path.split('/')[1]
			query_vars = dict(parse_query(parse_url(self.path).query))

			try:
				if self.path not in response_cache:
					info_getter = getattr(info, 'get_' + request)
					response_cache[self.path] = info_getter(**query_vars)
				self.respond(response_cache[self.path])
			except AttributeError:
				self.not_found()
			except NotImplementedError:
				self.not_implemented()
			# todo: KeyError -> 404(key)

	httpd = socketserver.TCPServer(("", port), MyHandler)
	print("serving at port", port)
	httpd.serve_forever()
