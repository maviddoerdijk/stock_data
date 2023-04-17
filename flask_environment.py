from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

from filter import main
inst = main()





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stocks_to_search = []
        word = request.form['stocks']
        watchlist_from_request = {'user_on_site': [word]}
        stocks_to_search.append(word)
        # Constraints should be set at some standard value, but changeable by the user 
        constraints_random = {"revenue_growth": 0.2, "debt_to_ebitda": 0.2}
        
        print(stocks_to_search)
        if word:
            satisfying_stocks = inst.filter_stocks(watchlist_from_request, constraints_random)
        else:
            satisfying_stocks = 'No stocks'

        try: 
            result = satisfying_stocks
        except Exception as e:
            print(e)
            result = None
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)