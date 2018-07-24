"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():

    response = request.args.get("choice")

    if response == "no":
        return render_template('goodbye.html')
    elif response == "yes":
        return render_template('game.html')


@app.route('/madlib')
def show_madlib():

    name = request.args.get('name')

    color = request.args.get('color').lower()

    n1 = request.args.get('noun').lower()

    adj = request.args.get('adj').lower()


    choice_nouns = ['bottle', 'dog', 'car', 'cat', 'table', 'peanuts', 'candy', 'kitty']
    nouns = []

    # for noun in choice_nouns:
    #     if request.args.get(noun) == 'on':
    #         nouns.append(noun)  


    new_nouns = request.args.getlist('nounz')

    # for i in range(len(nouns)):
    #     random.choice(nouns, i)  

    madlibs_templates = ['madlibs.html', 'madlibs1.html', 'madlibs2.html']              


    #return render_template('madlibs.html', color=color, noun=n1, person=name, adjective=adj, nouns=nouns)

    return render_template(choice(madlibs_templates), color=color, noun=n1, person=name, adjective=adj, nouns=new_nouns)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
