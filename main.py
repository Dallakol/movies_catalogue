from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    r = range(5)
    movies = [*r]
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)