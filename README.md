# dcc_zero_level_generator
A command-line and web-based interface for creating 0-level
character sheets for the Dungeon Crawl Classics RPG

External dependencies:
  lxml 4.4.2
  CairoSVG 2.4.2 
  Flask 1.1.1

character_funnel2.py can be run from the command-line and
will output a .pdf in whichever app your os is set to display
.pdf files in.
The .pdf file will be saved in a folder called new_sheets in the 
static folder of the app.

web_dcc.py is a simple flask app which offers a web interface
and will output the .pdf file in a webpage.
The .pdf file will be saved in a folder called new_sheets in the
static folder of the app if you are running it locally, otherwise
you can save the file from the webpage if you want to keep it.
