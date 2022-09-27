from flask import Flask, redirect, url_for, render_template

app = Flask(__name__,
    static_url_path='', 
    static_folder='static'
)

@app.route("/")
def home():
    import os
    cwd = os.getcwd()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)