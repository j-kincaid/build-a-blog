from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:introducingKat@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model): # Create an instance of the Blog class
    id = db.Column(db.Integer, primary_key=True) # Cretes a new property of our class that will map to an integer column in the blog table. The column name will be generated from the property name to be id as well. The column will be a primary key column on the table.
    #The name is the column within blog name
    title = db.Column(db.String(500)) # Creates a property that will map to a column of type VARCHAR(120) in the blog table.
    body = db.Column(db.String(1000))

# Create a constructor: 
    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog = request.form['blog']
        new_blog = Blog(blog) # To create an instance of our persistent Blog class, we use the same syntax as always.
        db.session.add(new_blog) # Store the object in the database
        db.session.commit() # commit it to the db


    blogs = Blog.query.filter_by(body=False).all() # Here, Blog.query.all() has the net effect of running SELECT * FROM blog and then taking the results and turning them into a list of Blog objects.

    # only give me the blogs for which the body column has the value False
    body_blogs = Blog.query.filter_by(body=True).all()
    return render_template('newpost.html',title="Add a New Entry!", blogs=blogs, body_blogs=body_blogs)


# @app.route('/blog') # The blog route displays all posts.
# def index():
#     return render_template('blog.html')

@app.route('/blog', methods=['POST'])
def add_entry():

    if request.method == 'POST':
        blog_name = request.form['post']
        new_blog = Blog(blog_name)
        db.session.add(new_blog)
        db.session.commit()

    return render_template('blog.html')


@app.route('/newpost', methods=['POST']) # Submit your blogs through '/newpost' 
# After you submit, the main page is displayed.
def process_add_entry():

    blog_id = int(request.form['blog-id'])
    blog = Blog.query.get(blog_id) # Calling query.get() will query for the specific object/row by its primary key.
    blog.body = True
    db.session.add(blog)
    db.session.commit()

    return redirect('/blog')

if __name__ == '__main__':

    app.run()