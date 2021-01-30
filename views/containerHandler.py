import config
import storage
from storage import app
from views import navbar, modules, thisDevice, server, user


def switchContainer(name):
    if storage.currentContainer != "":
        app.hideLabelFrame(storage.currentContainer)
    containerToSwitchTo = ""
    for navEleCallName in storage.navBarElementsCallName:
        if name in navEleCallName:
            containerToSwitchTo = navEleCallName
            break
    app.showLabelFrame(containerToSwitchTo)
    storage.currentContainer = containerToSwitchTo


# register nav bar presses
def navButtonPress(name):
    switchContainer(name)


def basicContent():
    app.addLabel("test", config.config["endpointURL"])


def registerContainer():
    modules.createContent()
    thisDevice.createContent()
    server.createContent()
    user.createContent()


def create():
    # register content
    app.startFrame("content", row=0, column=1)
    app.setStretch("both")
    app.setSticky("nesw")
    registerContainer()
    app.stopFrame()
    # navbar
    navbar.openNavBar(navButtonPress)
    switchContainer(storage.navBarElements[0])