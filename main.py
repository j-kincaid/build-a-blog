from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:introducingKat@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    completed = db.Column(db.Boolean)

    def __init__(self, name):
        self.name = name
        self.completed = False


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        entry_name = request.form['entry']
        new_entry = Blog(entry_name)
        db.session.add(new_entry)
        db.session.commit()

# Change template name

    entries = Blog.query.filter_by(completed=False).all()
    completed_entries = Blog.query.filter_by(completed=True).all()
    return render_template('entries.html',title="Build a Blog!", 
        entries=entries, completed_entries=completed_entries)


@app.route('/delete-entry', methods=['POST'])
def delete_entry():

    entry_id = int(request.form['entry-id'])
    entry = Entry.query.get(entry_id)
    entry.completed = True
    db.session.add(entry)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()