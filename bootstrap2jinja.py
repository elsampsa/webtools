#!/usr/bin/python3
"""

1. Create "static/bootstrap" into your pyramid projects directory structure

2. Copy -r the "dist" folder from bootstrap into your pyramid projects "static/bootstrap/"

3. Copy -r the "docs/assets" folder from bootstrap into your pyramid projects "static/bootstrap/"

4. Copy the template specific css file (say, "jumbotron.css") into "static/bootstrap/"

5. Run ```python3 bootstrap2jinja.py namespace index.html > template.jinja2```

where ```namespace``` is the namespace of your pyramid project (say, ```my.awesome.project```), i.e. links will look like this:
```
<link href="{{request.static_url('NAMESPACE:static/bootstrap/dist/css/bootstrap.min.css')}}" rel="stylesheet">
```

Bonus sector:

If you define (any) extra parameter, say ```python3 bootstrap2jinja.py namespace index.html 1 > template.jinja2```, the scripts will turn any js downloaded from cdn's into local files.

After that, you have to run the script ```__download__.bash``` in your "static/js/" directory: it will download automagically the .js files


A sample directory tree:
```
static
    bootstrap
        jumbotron.css
        assets
            brand
            css
            ...
        dist
            css
            fonts
            ...
    js
        jquery-1.12.4.min.js
        ...
```


"""
import sys
import re
import os

namespace = sys.argv[1]
fname = sys.argv[2]

if len(sys.argv) > 3:
    writebash = True
else:
    writebash = False

r = re.compile('\<link href\=(\"\.\.\/\.\.\/)\S*(\")\S*')
# substitute "../.." in '<link href="../../dist/css/bootstrap.min.css" rel="stylesheet">'
# "../../ == match group 1
# " == match group 2

r1 = re.compile('\<script src=(\"\.\.\/\.\.\/)\S*(\")\>\<')
# <script src="../../assets/js/ie-emulation-modes-warning.js"></script>
# "../../ == match group 1
# " == match group 2

r2 = re.compile('\<link href=(\")\S*\.css(\").*')
# <link href="jumbotron.css" rel="stylesheet">
# " == match group 1
# " == match group 2

r3 = re.compile('\<script src=\"(http\S*)\"(.*)')
# <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
# on-line scripts to static ones

r4 = re.compile('lang=\"(\S*)\"')
# <html lang="en">

if writebash:
    dfile = open("__download__.bash", "w")
    dfile.write("#!/bin/bash\n")

def getJSfname(line):
    m = r3.search(line)
    if m is not None:
        url = line[m.start(1):m.end(1)]
        if writebash:
            dfile.write("wget %s\n" % (url))

        fname = url.split("/")[-1]
        newline = line[0:m.start(1)] + \
            "{{request.static_url('"+namespace+":static/js/" + fname + "')}}\"" + \
            line[m.start(2):]
        return newline
    else:
        return None


rs = [r, r1, r2]


with open(fname) as f:
    for line in f:

        newline = None
        for r in rs:
            m = r.search(line)
            if m is not None:
                newline = line[0:m.start(1)] + \
                    "\"{{request.static_url('"+namespace+":static/bootstrap/" + \
                    line[m.end(1):m.start(2)] + \
                    "')}}" + \
                    line[m.start(2):]
                break

        if newline is None:
            # change dynamic fetching of js (jquery, etc.) to static files
            newline = getJSfname(line)

        if newline is None:
            m = r4.search(line)
            if m is not None:
                newline = line[0:m.start(1)] + '{{request.locale_name}}' + line[m.end(1):]

        if newline is not None:
            print(newline, end="")
        else:
            print(line, end="")
if writebash:
    dfile.close()
    os.system("chmod a+x __download__.bash")

