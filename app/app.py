from flask import Flask
from lotto import get_lottery_numbers, get_eurojackpot_lottery_numbers, get_joker_numbers

app = Flask(__name__)
style = """
table a {
    color: #0099ff;
    text-decoration: none;
}
table a:hover {
    color: white;
    background-color: #0099ff;
}
body {
    padding-top: 10px
}
"""

doc = f"""
<html>
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
    <style>{style}</style>
    <title>Lotto App</title>
  </head>
  <body>
    <div class="container">
      <h4>Select Lotto Flavour</h4>
      <table class="table table-striped">
        <thead>
            <tr>
            <th scope="col">Flavour</th>
            <th scope="col">Rules</th>
            <th scope="col">Permutations</th>
            </tr>
        </thead>
        <tbody>
          <tr>
            <td><a href="/veikkauslotto">Veikkaus</a></td>
            <td>7 unique numbers, range 1-50</td>
            <td>18643560</td>
          </tr>
          <tr>
            <td><a href="/vikinglottery">Viking</a></td>
            <td>6 unique numbers, range 1-48</td>
            <td>12271512</td>
          </tr>
          <tr>
            <td><a href="/eurojackpotlotto">Euro Jackpot</a></td>
            <td>5 unique numbers, range 1-50 and 2 unique numbers, range 1-12</td>
            <td>139838160</td>
          </tr>
          <tr>
            <td><a href="/jokeri">Jokeri</a></td>
            <td>7 non-unique numbers, range 0-9</td>
            <td>10000000</td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>
"""

style += """
.star-numbers {
    padding-left: 5px
}
"""

def lotto_page_generator(numbers: str, title: str):
    return f"""
<html>
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
    <style>{style}</style>
    <title>{title}</title>
  </head>
  <body>
    <div class="container">
      <table>
        <thead>
          <tr>
            <th scope="col">New numbers for {title}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{numbers}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>
"""

@app.route('/')
def root():
    return doc

@app.route('/veikkauslotto')
def veikkauslotto():
    new_numbers = get_lottery_numbers(7, 1, 40)
    return lotto_page_generator(new_numbers, "Veikkaus Lotto")

@app.route('/vikinglottery')
def vikinglottery():
    new_numbers = get_lottery_numbers(6, 1, 48)
    return lotto_page_generator(new_numbers, "Viking Lotto")

@app.route('/eurojackpotlotto')
def eurojackpotlotto():
    new_numbers = get_eurojackpot_lottery_numbers()
    return lotto_page_generator(new_numbers, "Euro Jackpot Lotto")

@app.route('/jokeri')
def veikkausjokeri():
    new_numbers = get_joker_numbers()
    return lotto_page_generator(new_numbers, "Veikkaus Jokeri")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
