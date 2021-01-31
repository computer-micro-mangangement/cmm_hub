import psutil
from appJar import gui
import config
import requests as req
import json
import platform

import sysInfo

app = gui(title="CMM Hub", showIcon=False)
navBarElements = []
navBarElementsCallName = []

currentContainer = ""


def get_size(bytes, suffix="B"):
  """
  Scale bytes to its proper format
  e.g:
      1253656 => '1.20MB'
      1253656678 => '1.17GB'
  """
  factor = 1024
  for unit in ["", "K", "M", "G", "T", "P"]:
    if bytes < factor:
      return f"{bytes:.2f}{unit}{suffix}"
    bytes /= factor


def getServerInfo():
    request = req.get(config.getServerAddress() + "/api/info", verify=False)
    if request.status_code == 200:
        jsonData = json.loads(request.text)
        return jsonData
    return {}


def getUserInfo():
    request = req.get(config.getServerAddress() + "/api/user/currentUser", verify=False,
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
        modules = {}
        data = request.text
        lines = data.split('\n')
        for line in lines:
            elements = line.split(',')
            modules[elements[0]] = {}
            modules[elements[0]]["link"] = elements[1]
            modules[elements[0]]["name"] = elements[0].capitalize()
            modules[elements[0]]["version"] = elements[2]
        return modules


def getDeviceInfo():
    deviceInfo = {}
    uname = platform.uname()
    deviceInfo["os"] = uname.system + str(uname.release)
    deviceInfo["name"] = uname.node
    deviceInfo["architecture"] = uname.machine
    deviceInfo["processor"] = {}
    deviceInfo["processor"]["processor Declaration"] = uname.processor
    deviceInfo["processor"]["cores"] = psutil.cpu_count(logical=False)
    deviceInfo["processor"]["threads"] = psutil.cpu_count(logical=True)
    svmem = psutil.virtual_memory()
    deviceInfo["installed RAM"] = get_size(svmem.total)
    return deviceInfo
