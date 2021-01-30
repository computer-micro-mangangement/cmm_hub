from storage import app
from storage import navBarElements


def openNavBar(func):
    app.startFrame("navbar", row=0, column=0)
    app.setStretch("none")
    app.setSticky("nesw")
    app.setBg("#2d2d2d", override=True)
    app.setFg("whitesmoke", override=True)
    for ele in navBarElements:
        name = ele
        app.addButton(title=name, func=func)
        app.setButtonFg(name, "#2d2d2d")
        app.setButtonBg(name, "whitesmoke")
    app.stopFrame()
