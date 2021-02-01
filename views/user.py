import helper
import storage
from storage import app
import config
from views import basicContentContainer

modulePrefix = "user"


def content():
    user = storage.getUserInfo()
    helper.displayJson(modulePrefix, user)


def createContent():
    basicContentContainer.create("You ", content)