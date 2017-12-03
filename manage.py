from flask_script import Manager
from project import app, db
import unittest

manager = Manager(app)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()

