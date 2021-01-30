#ToDo page to view current device
# (no backend needed)

from storage import app, navBarElementsCallName, navBarElements
import config
from views import basicContentContainer

modulePrefix = "thisDevice"


def content():
    app.addLabel(modulePrefix + "test", "Device")


def createContent():
    basicContentContainer.create("This Device", content)