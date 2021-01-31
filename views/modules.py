# ToDo module page, to view installed and downloadable modules, and make them installable and uninstallable
# get data from ccmModuleList (.csv)
import storage
from storage import app
import config
from views import basicContentContainer

modulePrefix = "modules"


def content():
    modules = storage.getInstallableModules()
    app.addLabel(modulePrefix + "test", "Modules")
    app.addLabel(modulePrefix + "test1", "Modules")
    app.addLabel(modulePrefix + "test2", "Modules")
    app.addLabel(modulePrefix + "test3", "Modules")
    app.addLabel(modulePrefix + "test4", "Modules")
    app.addLabel(modulePrefix + "test5", "Modules")
    app.addLabel(modulePrefix + "test6", "Modules")


def createContent():
    basicContentContainer.create("Modules manager", content)
