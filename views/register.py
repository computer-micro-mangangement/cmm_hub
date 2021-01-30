import json
import platform

import requests as req

from storage import app
from sysInfo import printAll
import config


def registerPress():
    addr: str = app.getEntry("Server Address")
    token: str = app.getEntry("Device-Token")
    uname = platform.uname()

    if addr != "" and token != "":
        if "http" not in addr:
            addr = "http://" + addr
        app.setLabel("info", "Trying to contact cmm server")
        registerRequest = req.post(addr + "/api/devices/register", json={
            "loginsecret": token,
            "name": uname.node,
            "os": uname.system,
            "osshort": uname.system[0:3],
            "arch": uname.machine,
            "mac": "Na"
        }, verify=False)
        responseCode = registerRequest.status_code
        if responseCode <= 200 or responseCode >= 300:
            app.setLabel("info", "Something went wrong, token probably invalid\nStatus code: " + str(responseCode))
        else:
            jsonData = json.loads(registerRequest.text)
            config.config["endpointURL"] = addr
            config.config["secret"] = jsonData["clientSecret"]
            config.config["uuid"] = jsonData["uuid"]
            config.save(config.config)
            app.setLabel("info", "Successfully registered device")
            app.hideSubWindow("Register this device")
    else:
        app.setLabel("info", "You have to specify everything")


def openRegisterWindow():
    printAll()
    app.startSubWindow("Register this device", modal=True)
    app.setBg("#2d2d2d", override=True)
    app.setFg("whitesmoke", override=True)
    app.setIcon("./favicon.ico")
    app.setResizable(canResize=True)
    app.setFont(size=10)
    app.setSize(500, 210)
    app.setPadding([20, 20])
    app.setStretch("column")
    app.setSticky("nesw")
    app.setOnTop(True)

    app.enableEnter(registerPress)

    app.addLabelEntry("Server Address")
    app.setEntryDefault("Server Address", "enter the server address here")

    app.addLabelEntry("Device-Token")
    app.setEntryDefault("Device-Token", "Paste the device token here")

    app.setPadding([0, 0])
    app.addLabel("info", text="")
    app.setPadding([20, 20])

    app.addButton("Claim Token and register this Device", registerPress)
    app.setButtonBg("Claim Token and register this Device", "#3a3a3a")
    app.setButtonFg("Claim Token and register this Device", "whitesmoke")

    app.stopSubWindow()
    app.showSubWindow("Register this device")
