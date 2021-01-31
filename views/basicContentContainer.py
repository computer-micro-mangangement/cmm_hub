from storage import app, navBarElementsCallName, navBarElements


def create(name: str, contentFunc):
    navBarElements.append(name)

    containerName = name + "container"
    navBarElementsCallName.append(containerName)

    app.setFg("whitesmoke", override=True)
    app.setStretch("both")
    app.setSticky("nesw")
    app.startLabelFrame(containerName, row=0)
    app.setLabelFrameFg(containerName, "whitesmoke")
    app.setStretch("both")
    app.setSticky("nesw")

    app.startScrollPane(name + "scroll")
    app.setFont(size=10)
    app.setPadding([20, 20])
    app.setStretch("both")
    app.setSticky("nesw")
    app.setBg("#2d2d2d", override=True)
    app.setFg("whitesmoke", override=True)

    app.setStretch("none")
    app.setSticky("nw")
    app.setPadding([2, 2])
    contentFunc()

    app.stopScrollPane()
    app.stopLabelFrame()
    app.hideLabelFrame(containerName)
