#ToDo page to view user information
# equivalent to /api/user/currentUser

from storage import app
import config
from views import basicContentContainer

modulePrefix = "user"


def content():
    app.addLabel(modulePrefix + "test", "User")


def createContent():
    basicContentContainer.create("You ", content)