So, this is the first post of this blog, describing creation of this blog (and maybe other things), describing creation of this blog (and maybe other things), describing... You got the point.

As of now, this is merely an exercise at writing things and writing about things.

Setup us really simple for now, consisting of 2 main parts:

- HTTP server which gets an object and, when prompted with a /[stuff] request calls object's get_[stuff] method and responds with that method's output (I reused and improved this one and plan to continue doing so for use in other stuff)

- Blog class with get_posts method - which scans a certain folder for .md files and treats each of them as a separate entry. Name, contents, creation and modification times of each entry are determined in an obvious way.

There are *many* things I'd like to address from technological, aesthetic and eloquent standpoints but as of now, it works and that's enough.

