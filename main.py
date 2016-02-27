#!/usr/bin/env python3

from blog import Blog
from server import run_server, HtmlEncoder

blog = Blog()
page_encoder = HtmlEncoder()
page_encoder.set_head(blog.get_head())
run_server(blog, port = 9000, encoder = page_encoder)
