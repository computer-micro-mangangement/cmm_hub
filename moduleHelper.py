import json
import os
import shutil
import urllib.request
from zipfile import ZipFile
import config
import storage

modulesPath = "./modules/"
moduleInfoFileName = "info.json"


def getInstallableModules():
    return storage.getInstallableModules()


def getInstallableModuleByName(name):
    installableModules = getInstallableModules()
    for moduleName in installableModules:
        if moduleName.lower() == name.lower():
            return installableModules[moduleName]
    return {"version": "Na", "name": "Na"}


def getInstalledModules():
    if not os.path.isdir(modulesPath):
        os.makedirs(modulesPath)
    items = os.listdir(modulesPath)
    modules = {}
    for item in items:
        path = modulesPath + item
        if os.path.isdir(path):
            moduleInfoPath = path + "/" + moduleInfoFileName
            if os.path.isfile(moduleInfoPath):
                jsonData = json.load(open(moduleInfoPath, 'r'))
                version = jsonData["version"]
                name = jsonData["name"]
                modules[name] = {"version": version, "name": name, "link": "na"}
    return modules


def getInstalledModuleByName(name):
    installedModules = getInstalledModules()
    for moduleName in installedModules:
        if moduleName.lower() == name.lower():
            return installedModules[moduleName]
    return {"version": "Na", "name": "Na", "link": "na"}


def getAllModules():
    installed = getInstalledModules()
    web = getInstallableModules()
    allModules = {}
    for m in installed:
        if m not in allModules:
            allModules[m] = installed[m]
    for m in web:
        if m not in allModules:
            allModules[m] = web[m]
    return allModules


def downloadModule(name):
    module = getInstallableModuleByName(name)
    link = module["link"]
    path = modulesPath + name
    downloadPath = modulesPath + "tmp"
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isdir(downloadPath):
        os.makedirs(downloadPath)
    zipPath = downloadPath + "/" + name + ".zip"
    urllib.request.urlretrieve(link, zipPath)
    with ZipFile(zipPath, 'r') as zipFile:
        listOfFileNames = zipFile.namelist()
        unzippedPath = downloadPath + "/unzipped"
        zipFile.extractall(unzippedPath)
        items = os.listdir(unzippedPath)
        shutil.rmtree(path)
        shutil.move(unzippedPath + "/" + items[0], path)
    shutil.rmtree(downloadPath)

