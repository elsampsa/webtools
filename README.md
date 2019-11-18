## Some tools for templating webpages

*(mainly just for myself)*

### bootstrap2jinja.py

- I'm using bootstrap with pyramid
- This script turns a bootstrap template into a pyramid-compatible jinja2 template

First, start a [new pyramid project](https://github.com/Pylons/pyramid-cookiecutter-starter#usage)

Download bootstrap by taking the "Source Code" option from [this page](https://getbootstrap.com/docs/3.4/getting-started/)

That gives you the bootstrap library and the example templates.  The latter live in "docs/examples".  

Then do this (you can use [this script](copy_bs.bash)):

$DIR = pyramid projects code dir (where you have the subdirectory "static/")

1. Create $DIR/static/bootstrap

2. Copy -r the "dist" folder from bootstrap into $DIR/static/bootstrap/

3. Copy -r the "docs/assets" folder from bootstrap into $DIR/static/bootstrap

4. Copy the template specific css file (say, "jumbotron.css") into $DIR/static/bootstrap/"

5. Copy the template specific ```index.html``` into $DIR

Finally, run ```python3 bootstrap2jinja.py namespace index.html > templates/mytemplate.jinja2```

where ```namespace``` is the namespace of your pyramid project (say, ```my.awesome.project```), i.e. links will look like this:
```
<link href="{{request.static_url('NAMESPACE:static/bootstrap/dist/css/bootstrap.min.css')}}" rel="stylesheet">
```
(most of the time the namespace is just the name of your python package's directory)

Bonus sector:

If you define (any) extra parameter, say ```python3 bootstrap2jinja.py namespace index.html 1 > templates/mytemplate.jinja2```, the scripts will turn any js downloaded from cdn's into local files.

After that, you have to run the script ```__download__.bash``` in your $DIR/static/js/ directory: it will download automagically the .js files

A sample directory tree:
```
your_package_name/
   your_package_name/
        static/
            bootstrap/
                jumbotron.css
                assets/
                    brand
                    css
                    ...
                dist/
                    css
                    fonts
                    ...
            js/
                jquery-1.12.4.min.js
                ...
```

To test, go to the main dir and launch the webserver with:
```
pserve --reload development.ini
```


### Link collection
- [Starting a new Pyramid project](https://github.com/Pylons/pyramid-cookiecutter-starter#usage)
- [Bootstrap basic templates](https://getbootstrap.com/docs/3.4/getting-started/#examples)
- [Bootstrap css](https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp)
- [Bootstrap styleguide](https://codepen.io/joe-watkins/pen/AokJw/)
- [Bootstrap templates](https://startbootstrap.com/)
- [More bootstrap templates](https://themes.getbootstrap.com/)
- [JS DOM](https://www.w3schools.com/jsref/dom_obj_anchor.asp)
- [JS All DOM members](https://www.w3schools.com/jsref/dom_obj_all.asp)
- [JS API](https://developer.mozilla.org/en-US/docs/Web/API)
- [Pyramid Request](https://docs.pylonsproject.org/projects/pyramid/en/latest/api/request.html)
- [Pyramid Response](https://docs.pylonsproject.org/projects/pyramid/en/latest/api/response.html)
- [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/templates/)
- [Redis quickstart](https://pyramid-redis-sessions.readthedocs.io/en/latest/gettingstarted.html) (remember to apt-get install redis-server)
