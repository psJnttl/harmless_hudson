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

def lotto_page_generator(numbers: str, title: str):
    return f"""
<html>
  <head>
    <title>{title}</title>
  </head>
  <body>
    <h5>New numbers for {title}</h5>
    {numbers}
  </body>
</html>
"""

@app.route('/')
def root():
    return doc

@app.route('/veikkauslotto')
def veikkauslotto():
    new_numbers = get_lottery_numbers(7, 1, 40)
    return return lotto_page_generator(new_numbers, "Veikkaus Lotto")

@app.route('/vikinglottery')
def vikinglottery():
    new_numbers = get_lottery_numbers(6, 1, 48)
    return lotto_page_generator(new_numbers, "Viking Lotto")

@app.route('/eurojackpotlotto')
def eurojackpotlotto():
    new_numbers = get_eurojackpot_lottery_numbers()
    return lotto_page_generator(new_numbers, "Euro Jackpot Lotto")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
