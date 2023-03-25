from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

from filter import main
inst = main()


# dictionaries of types of constraints
constraints_random = {"revenue_growth": 0.2, "debt_to_ebitda": 0.2}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['string']
        watchlist_from_request = {'user_on_site': [word]}
        watchlist_kfc = {'david': ['aapl', 'META', 'ANET', 'PAYC']}
        result = inst.filter_stocks(watchlist_from_request, constraints_random)
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()   