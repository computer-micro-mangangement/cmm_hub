#ToDo info page for server
# equivalent to /api/info
import storage
from storage import app
import config
from views import basicContentContainer

modulePrefix = "server"


def content():
    storage.getServerInfo()
    app.addLabel(modulePrefix + "test", "Server")


def createContent():
    basicContentContainer.create("Your Server", content)