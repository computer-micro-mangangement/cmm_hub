# import the library

from views import register, containerHandler
import config
from storage import app

# create app container with basi settings
app.setBg("#2d2d2d", override=True)
app.setFg("whitesmoke", override=True)
app.setIcon("./favicon.ico")
app.setResizable(canResize=True)
app.setFont(size=10)
app.setPadding([20, 20])

# load config, create if not exists
config.config = config.load()
if config.config["secret"] == "":
    register.openRegisterWindow()

# creating content container
containerHandler.create()

app.go()
