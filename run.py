from flaskblog import create_app, db
from flaskblog.models import User
import click

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

@app.cli.command()
@click.argument('username')
@click.argument('email')
@click.argument('password')
def create_user(username, email, password):
    admin = User(username=username, email=email, password=password, is_admin=True)
    db.session.add(admin)
    db.session.commit()
