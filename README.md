 ## Some tools for templating webpages

### bootstrap2jinja.py

- I'm using bootstrap with pyramid
- This script turns a bootstrap template into a pyramid-compatible jinja2 template

Take the "Source Code" option from [this page](https://getbootstrap.com/docs/3.4/getting-started/)

That gives you the bootstrap library and the example templates.  The latter live in "docs/examples".  

Then do this:

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

Some more links: 

- [Using templates](https://getbootstrap.com/docs/3.4/getting-started/#examples)
- [Bootstrap css](https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp)
