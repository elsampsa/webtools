#!/bin/bash
# Usage: copy_bs.bash bootstrap_main_dir theme_name
# example: ./copy_bs.bash ~/Downloads/bootstrap-3.4.1 jumbotron
mkdir static/bootstrap
cp -r $1/dist static/bootstrap/
cp -r $1/docs/assets static/bootstrap/
cp $1/docs/examples/$2/$2.css static/bootstrap/
cp $1/docs/examples/$2/index.html .
