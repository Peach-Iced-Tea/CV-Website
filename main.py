from flask import Flask, render_template, abort
import json, os
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    with open("./links.json") as f:
        jsObjects = json.loads(f.read())
    return render_template("index.html", urls=jsObjects)

@app.route("/<post>")
def postView(post):
    path = f'{os.path.dirname(__file__)}/posts/{post}.md'
    print(path)
    if not(os.path.exists(path)):
        abort(404)
    else:
        with open(path, 'r') as f:
            text=f.read()
        content = markdown.markdown(text)
        return render_template("post.html", test=content)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)