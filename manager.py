from flask_migrate import Migrate, MigrateCommand
from flask_script import Server, Manager

from blog import create_app
from blog.models import Article
from config import BaseConfig
from extand import db

app = create_app(BaseConfig)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def manager_shell_context():
    return dict(Article=Article)


if __name__ == '__main__':
    manager.run()
