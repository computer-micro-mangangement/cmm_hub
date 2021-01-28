from storage import app


def registerPress():
    addr: str = app.getEntry("Server Address")
    token: str = app.getEntry("Device-Token")
    if addr != "" and token != "":
        if addr.
            app.setLabel("info", "Trying to contact cmm server")

        app.setLabel("info", "Successfully registered device")
        app.hideSubWindow("Register this device")
    else:
        app.setLabel("info", "You have to specify everything")


def openRegisterWindow():
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
