from flask_script import Manager,Server

from app import create_app,db

app = create_app()

manager =  Manager(app)
manager.add_command('run',Server(use_debugger=True))

@manager.shell
def make_shell_context():
    return dict(app = app,db = db)

if __name__ == '__main__':
    manager.run()