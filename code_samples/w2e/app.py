from flask import Flask, render_template #, request, redirect
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/suggest') # 5/24/20 - call this URL "suggest" instead, so the full url is wut2eat.com/suggest
def meal_idea():
  main = open ("main_dish.txt", 'r').read()
  main_split= main.split('\n')
  starch = open ("starch.txt", 'r').read()
  starch_split= starch.split('\n')
  vegetable = open ("vegetable.txt", 'r').read()
  vegetable_split= vegetable.split('\n')
  main_dish = random.choice(main_split)
  starch_side = random.choice(starch_split)
  veggie_side = random.choice(vegetable_split)  
  suggested = 'How about ' + main_dish + ' with ' + starch_side + ' and ' + veggie_side + '?'
  return render_template('w2e.html', result=suggested)
if __name__  == '__main__':
  app.run(debug=True,host='0.0.0.0', port=5002)
