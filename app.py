from flask import Flask

app = Flask(__name__)

doc = """
<html>
  <title>Lotto App</title>
  <body>
    <h4>Here be Lotto flavour choice</h4>
  </body>
</html>
"""

@app.route('/')
def root():
    return doc

if __name__ == '__main__':
    app.run(host='0.0.0.0')
