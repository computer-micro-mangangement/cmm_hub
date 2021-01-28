# import the library

import register
from storage import app


def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)


def login(btn):
    app.hideSubWindow("Login")
    app.show()


# create a GUI variable called app

app.setBg("#2d2d2d", override=True)
app.setFg("whitesmoke", override=True)
app.setIcon("./favicon.ico")
app.setResizable(canResize=True)
app.setFont(size=10)

app.addLabel("test", "hulu")

register.openRegisterWindow()

app.go()
