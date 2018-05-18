#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi, unicodedata, html


form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "did not set")
text2 = form.getfirst("TEXT_2", "did not set")
text1 = html.escape(text1)
text2 = html.escape(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Form data</title>
        </head>
        <body>""")

print("<h1>Form data!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")
