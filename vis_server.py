from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
app = FastAPI()
from urllib.parse import parse_qsl

@app.get("/items/{tree}", response_class=HTMLResponse)
async def display_tree(tree):
    tree_json = json.dumps(dict(parse_qsl(tree) ))
    #print("item",dict(urllib.parse.parse_qsl(item) ))

    return """
    <!DOCTYPE html><html>
  <head>
    <title>Hierplane!</title>
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/hierplane@0.2.1/dist/static/hierplane.min.css">
    <script src="https://unpkg.com/hierplane@0.2.1/dist/static/hierplane.min.js"></script>
    </head>
  <body>
    <script>
      const tree = {
        text: 'Sam likes boats',
        root: {
          nodeType: 'event',
          word: 'like',
          spans: [
            {
              start: 4,
              end: 9
            }
          ],
          children: [
            {
              nodeType: 'entity',
              word: 'Sam',
              link: 'subject',
              attributes: [ 'Person' ],
              spans: [
                {
                  start: 0,
                  end: 3
                }
              ]
            },
            {
              nodeType: 'entity',
              word: 'boat',
              link: 'object',
              attributes: [ '>1'],
              spans: [
                {
                  start: 10,
                  end: 17
                }
              ]
            }
          ]
        }
      };
      hierplane.renderTree(JSON.parse(JSON.stringify(tree)));
    </script>
  </body>
</html>
    """