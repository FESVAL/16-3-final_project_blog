from blog import app, db
from .blog.models import Entry, User, Post


#чи потрібні ці імпорти взагалі?
from .blog.routes import routes
from .blog.models import models

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Post": Post
    }