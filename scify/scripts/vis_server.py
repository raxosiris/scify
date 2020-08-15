from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
app = FastAPI()
from urllib.parse import parse_qs, parse_qsl

@app.get("/items/{tree}", response_class=HTMLResponse)
async def display_tree(tree):
    def script_embeddable_json(value):
        return (
            json.dumps(json.dumps(value))
            .replace("<", "\\u003c")
            .replace("\u2028", "\\u2028")
            .replace("\u2029", "\\u2029"))

    # d = eval(tree)
    # print("KKKKKK", d)
    # tree_json = json.dumps(d)

    # f = open("jj.json", "w+")
    # f.write(d)
    # f.close()
    # return d
    
    with open("temp_vis.json", "r+") as ff:
        tree_json = json.dumps(json.load(ff))

    
    #print("item",dict(urllib.parse.parse_qsl(item) ))
    print(tree_json, "treee", type(tree_json))
    html = """
    <!DOCTYPE html><html>
  <head>
    <title>Hierplane!</title>
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/hierplane@0.2.1/dist/static/hierplane.min.css">
    <script src="https://unpkg.com/hierplane@0.2.1/dist/static/hierplane.min.js"></script>
    </head>
  <body>
    <script>
    
      hierplane.renderTree(JSON.parse(JSON.stringify({tree_json})));
    </script>
  </body>
</html>""".format(tree_json=tree_json) 

    with open("temp_vis.html", "w") as h:
        h.write(html)

    return html