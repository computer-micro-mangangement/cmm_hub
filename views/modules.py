# ToDo module page, to view installed and downloadable modules, and make them installable and uninstallable
# get data from ccmModuleList (.csv)
import moduleHelper
import storage
from storage import app
import config
from views import basicContentContainer

modulePrefix = "modules"
rowsNeededForModuleEntry = 2


def addTitle(name, row):
    app.addLabel(modulePrefix + name.lower() + "title", name.capitalize(), row=row, column=0, colspan=2)


def changeTitleText(name, newText):
    app.setLabel(modulePrefix + name.lower() + "title", newText)


def buttonPress(btnName: str):
    split = btnName.lower().split(" ")
    func = split[0]
    moduleName = split[1]
    changeTitleText(moduleName, moduleName.capitalize() + " (Downloading)")
    moduleHelper.downloadModule(moduleName)
    changeTitleText(moduleName, moduleName.capitalize() + " (Downloaded)")


def createModuleEntry(name: str, row: int):
    app.setStretch("none")
    app.setSticky("nw")
    app.setPadding([2, 2])

    moduleFromWeb = moduleHelper.getInstallableModuleByName(name)
    moduleFromDrive = moduleHelper.getInstalledModuleByName(name)

    basicElementName = modulePrefix + name.lower()
    addTitle(name, row)

    app.addLabel(basicElementName + "version", "Installed Version: " + moduleFromDrive["version"], row=row + 1,
                 column=1, colspan=1)
    app.addLabel(basicElementName + "newest_version", "Newest Version: " + moduleFromWeb["version"], row=row + 1,
                 column=2, colspan=1)
    app.setSticky("ne")
    if moduleFromWeb["version"] != moduleFromDrive["version"]:
        if "na" not in moduleFromDrive["version"].lower():
            app.addButton("Update " + name.capitalize(), func=buttonPress, row=row, column=3, rowspan=2)
        else:
            app.addButton("Install " + name.capitalize(), func=buttonPress, row=row, column=3, rowspan=2)
    else:
        app.addLabel(basicElementName + "UptoDate", "Up-to-date", row=row, column=3, rowspan=2)


def content():
    modules = moduleHelper.getAllModules()
    row = 0
    for module in modules:
        createModuleEntry(module, row)
        row += rowsNeededForModuleEntry


def createContent():
    basicContentContainer.create("Modules manager", content)
