from flask import Flask, render_template

app=Flask(__name__)
post={
    0:{
    "Title":"First Post",
    "Content":"Contents of the first post"
    }
}

@app.route('/')
def home():
    return '''<!DOCTYPE html>
    <html >
      <head>
      <h1>Hello World</h1>
      </head>
      <body>

      </body>
    </html>'''

@app.route('/post/<int:post_id>')
def index(post_id):
    blog=post.get(post_id)
    return render_template('post.html',message=blog)

if(__name__)=="__main__":
    app.run(debug=True)
