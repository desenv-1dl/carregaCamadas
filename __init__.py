# -*- coding: latin1 -*-

from main import Testcamadas     


def name():
  return "UTM_DMS"
def description():
  return "converte coordenadas utm"
def version():
  return "Version 0.1"
def classFactory(iface):
  return Testcamadas(iface)
def qgisMinimumVersion():
  return "2.0"
def author():
  return "frank"
def email():
  return "me@hotmail.com"
def icon():
  return "icon.png"

## any other initialisation needed
