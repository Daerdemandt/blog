#!/usr/bin/env python3

from blog import Blog
from server import run_server, HtmlEncoder

blog = Blog()
run_server(blog, port = 9000, encoder = HtmlEncoder())
