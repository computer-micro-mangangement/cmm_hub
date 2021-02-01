import json

from storage import app


def displayJson(prefix, jsonData, indentation=0):
    for entry in jsonData:
        value = jsonData[entry]
        name = entry.capitalize()
        if "{" not in str(value):
            app.addLabel(prefix + entry, str("    " * indentation) + name + ": " + str(value))
        else:
            app.addLabel(prefix + entry, str("    " * indentation) + name + ":")
            displayJson(prefix, value, (indentation + 1))

