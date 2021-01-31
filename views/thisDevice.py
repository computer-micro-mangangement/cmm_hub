# ToDo page to view current device
# (no backend needed)
import helper
import storage
from storage import app, navBarElementsCallName, navBarElements
import config
from views import basicContentContainer

modulePrefix = "thisDevice"


def content():
    deviceInfo = storage.getDeviceInfo()
    helper.displayJson(modulePrefix, deviceInfo)


def createContent():
    basicContentContainer.create("This Device", content)
