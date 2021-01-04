from flask import Flask, render_template, session

import random


app = Flask(__name__)
app.debug = True

app.secret_key='asdasdfasdf sadf sdf s'

@app.route('/')
def hod_kostkou():
    hrac = random.randint(1, 6)
    bot = random.randint(1, 6)

    if not 'hrac' in session:
        session['hrac'] = 0
        session['bot'] = 0

 
    if (hrac > bot):
        vyhra="Vyhral jsi!"
        session['hrac'] = session['hrac'] + 1
        
    elif (hrac < bot):
        vyhra="Prohral jsi :C Zkus to znova !"
        session['bot'] = session['bot'] + 1
        
    else:
        vyhra="remiza!"

    HracVyhry = session['hrac'] 
    BotVyhry = session['bot'] 

    return render_template('hra.html', hrac=hrac, bot=bot, vyhra=vyhra, HracVyhra = HracVyhry, BotVyhra = BotVyhry)




if __name__ == '__main__':
    app.run()