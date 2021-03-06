# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from ride_beta import app, db


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

#manager.add_command("testentries", addTestEntries())

if __name__ == "__main__":
    print("run manager")
    manager.run()