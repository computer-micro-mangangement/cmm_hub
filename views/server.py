# ToDo info page for server
# equivalent to /api/info
import helper
import storage
from storage import app
import config
from views import basicContentContainer

modulePrefix = "server"


def content():
    serverInfo = storage.getServerInfo()
    helper.displayJson(modulePrefix, serverInfo)


def createContent():
    basicContentContainer.create("Your Server", content)
