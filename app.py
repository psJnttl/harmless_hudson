from flask import Flask
from lotto import lottery_numbers

app = Flask(__name__)

doc = """
<html>
  <title>Lotto App</title>
  <body>
    <h4>Select Lotto Flavour</h4>
    <a href='/veikkauslotto'>Veikkaus Lotto</a>
  </body>
</html>
"""

@app.route('/')
def root():
    return doc

@app.route('/veikkauslotto')
def veikkauslotto():
    new_numbers = "<span class='lotto-numbers'>"
    for number in lottery_numbers(7, 1, 40):
        new_numbers += f'{number} '
    new_numbers += "</span>"
    output = f"<html><head><title>Veikkaus Lotto</title></head><body><h5>New numbers for Veikkaus Lotto</h5>{new_numbers}</body></h>
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0')
