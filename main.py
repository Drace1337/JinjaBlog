from flask import Flask, render_template, url_for
from post import Post
import requests
import datetime


app = Flask(__name__)
posts = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

year = datetime.datetime.now().year

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects, year=year)

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template('post.html', post=requested_post, year=year)

if __name__ == "__main__":
    app.run(debug=True)
