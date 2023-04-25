from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'themostsecretofkeys' # set a secret key for security purposes

@app.route('/')
def index():
    if len(session.keys()) == 0:
    # if 'gold_amt' not in session.keys():
        session['gold_amt'] = 0
    # if 'activities' not in session.keys():
        session['activities'] = ''
    # if 'moves' not in session.keys():
        session['moves'] = 0
    # if 'game_won' not in session.keys():
        session['game_reset'] = ''
    return render_template('index.html', gold_count=session['gold_amt'],activities=session['activities'],
        moves=12-session['moves'],game_reset=session['game_reset'])


@app.route('/process_money',methods=['POST'])
def process_money():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.form['location'] == 'farm':
        gold_amt = random.randint(10,20)
    elif request.form['location'] == 'cave':
        gold_amt = random.randint(5,10)
    elif request.form['location'] == 'house':
        gold_amt = random.randint(2,5)
    elif request.form['location'] == 'casino':
        gold_amt = random.randint(-50,50)
    session['gold_amt'] += gold_amt
    if request.form['location'] == 'casino':
        if gold_amt < 0:
            message = f"<p class='loss'>Entered a casino and lost {abs(gold_amt)} berries... oof ({current_time})"
        else:
            message = f"<p class='gain'>Entered a casino and won {gold_amt} berries! Yay ({current_time})"
    else:
        message = f"<p class='gain'>Earned {gold_amt} berries from the {request.form['location']}! ({current_time})"
    
    session['activities'] += message+"</p>"
    session['moves'] += 1
    
    if session['gold_amt'] >= 390 or session['moves'] == 12:
        game_status = '<h1> Game Over! </h1>'
        game_status += f"<h2> You finished with {gold_amt} berries in {session['moves']} turns. Would you like to try again?"
        game_status += '</h2>'
        session['activities'] = game_status
        session['game_reset'] = "<div class='reset_button'> <a href='/reset_game'>Restart</a> </div>"
    return redirect('/')

@app.route('/reset_game')
def reset_game():
    session.clear()
    return redirect('/')




if __name__=="__main__":      
    app.run(debug=True) 
