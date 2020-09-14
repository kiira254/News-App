from app import create_app
from flask_script import Manager, Server

# Create app instance
app = create_app ('development')

Manager= Manager(app)
Manager.add_command('server',Server)
@Manager .command
def test():
    ''' 
    ruun the unit test
    '''
    import unittest
    tests= unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    Manager.run()
