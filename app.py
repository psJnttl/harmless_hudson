from flask import Flask
from lotto import get_lottery_numbers, get_eurojackpot_lottery_numbers

app = Flask(__name__)

doc = """
<html>
  <title>Lotto App</title>
  <body>
    <h4>Select Lotto Flavour</h4>
    <a href='/veikkauslotto'>Veikkaus Lotto</a>
    <a href='/vikinglottery'>Viking Lotto</a>
    <a href='/eurojackpotlotto'>Euro Jackpot Lotto</a>
  </body>
</html>
"""

@app.route('/')
def root():
    return doc

@app.route('/veikkauslotto')
def veikkauslotto():
    new_numbers = get_lottery_numbers(7, 1, 40)
    output = f"<html><head><title>Veikkaus Lotto</title></head><body><h5>New numbers for Veikkaus Lotto</h5>{new_numbers}</body></html>"
    return output

@app.route('/vikinglottery')
def vikinglottery():
    new_numbers = get_lottery_numbers(6, 1, 48)
    output = f"<html><head><title>Viking Lotto</title></head><body><h5>New numbers for Viking Lotto</h5>{new_numbers}</body></html>"
    return output

@app.route('/eurojackpotlotto')
def eurojackpotlotto():
    new_numbers = get_eurojackpot_lottery_numbers()
    output = f"<html><head><title>Viking Lotto</title></head><body><h5>New numbers for Eurojackpot Lotto</h5>{new_number}</body></html>"
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0')
