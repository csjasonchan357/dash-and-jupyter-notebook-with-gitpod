import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dcc.Markdown.dangerously_allow_html = True
app.layout =  dcc.Markdown('''
### Markdown 

Markdown
* **Markdown** is a simple way to format text.  
* It doesn’t do anything fancy like 
change the font size, color, or type, for that you need to add `html` tags.  
* A markdown processor converts markdown text into various renderable formats (like HTML or PDF).
* There are different many different [Markdown processors](https://github.com/markdown/markdown.github.com/wiki/Implementations).  
[GitHub Flavored Markdown](https://github.github.com/gfm/) is one.  
[Commonmark](commonmark.org) is another.

The [Dash Markdown component](https://dash.plot.ly/dash-core-components/markdown) 
documentation says it uses the [CommonMark](https://commonmark.org/) specification of Markdown,
and it _mostly_ seems to do so. (e.g., lists don't look good, GitHub Flavored Markdown
tables are supported)

Resources:
* [MardownGuide.org](https://www.markdownguide.org/getting-started/) 
  * basic syntax (works in all versions)
  * extended syntax (stuff like tables)
  * html tags (tweaks that improve formatting) 
  * list of markdown processors
  * list of tools (like slack and github that support markdown)
* [CommonMark Cheat Sheet]()
* [10 Minute CommonMark Tutorial](https://commonmark.org/help/tutorial/)

---
### Examples are below

#### Tables

| Qty | Description |
| --- | -------------------|
| 1   | Webserver (Flask)  |
| 2   | Database Types     |

**Tip:** Creating tables with hyphens and pipes can be tedious. 
To speed up the process, try using the 
[Markdown Tables Generator](http://www.tablesgenerator.com/markdown_tables). 
Build a table using the graphical interface, 
and then copy the generated Markdown-formatted text into your file.

#### Text style
*This text will be italic* <br> 
_This will also be italic_ <br>
**This text will be bold** <br>
__This will also be bold__ <br>
_You **can** combine them_

#### Lists

* Item 1
* Item 2
  * Item 2a
  * Item 2b

#### Indentation

>
> Block quotes are used to highlight text.
>

## Links
[Dash User Guide](https://dash.plot.ly/)

## Displaying Code
Inline code snippet: `True`

Block code snippet (here py specifies the code high-lighting to use):
```py
import urllib2
import urllib
import json

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
query = raw_input("What do you want to search for ? >> ")
query = urllib.urlencode( {'q' : query } )
response = urllib2.urlopen (url + query ).read()
data = json.loads ( response )
results = data [ 'responseData' ] [ 'results' ]

for result in results:
    title = result['title']
    url = result['url']
    print ( title + '; ' + url )
``` 

Block indenting works too:
>
    import urllib2
    import urllib
    import json
>
    url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
    query = raw_input("What do you want to search for ? >> ")
    query = urllib.urlencode( {'q' : query } )
    response = urllib2.urlopen (url + query ).read()
    data = json.loads ( response )
    results = data [ 'responseData' ] [ 'results' ]
>
    for result in results:
        title = result['title']
        url = result['url']
        print ( title + '; ' + url )
    

''')



if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")