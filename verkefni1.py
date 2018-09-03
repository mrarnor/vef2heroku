from bottle import route, run, template

@route("/")
def index():
    return """
    <h2>Verkefni 1</h2>
    <a href="/about"> About </a></p>
    <a href="/bio"> Biography </a></p>
    <a href="/pics"> pictures </a></p>
    """


@route("/about")
def name():
    return "Hér er about"

@route("/bio")
def name():
    return "Hér er bio"

@route("/pics")
def name():
    return "Hér er pics"




run(host='localhost', port=7500)
