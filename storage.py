from appJar import gui
import config
import requests as req
import json

app = gui(title="CMM Hub", showIcon=False)
navBarElements = []
navBarElementsCallName = []

currentContainer = ""


def getServerInfo():
    request = req.get(config.getServerAddress() + "/api/info", verify=False)
    if request.status_code == 200:
        jsonData = json.loads(request.text)
        return jsonData
    return {}


def getUserInfo():
    request = req.get(config.getServerAddress() + "/api/user/currentuser", verify=False,
                      params={"devicesecret": config.getDeviceSecret()})
    if request.status_code == 200:
        jsonData = json.loads(request.text)
        return jsonData
    return {}


def getInstallableModules():
    serverInfo = getServerInfo()
    moduleListURL = serverInfo["moduleListURL"]
    request = req.get(moduleListURL, verify=False)
    if request.status_code == 200:
        data = request.text
        lines = data.split('\n')
        
