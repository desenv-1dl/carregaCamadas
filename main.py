# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis.utils
import psycopg2
import pprint
from PyQt4.QtCore import QSettings
import os


import resources

from interface import *


class Testcamadas:  
    def __init__(self, iface):
        self.iface = iface
    
    def initGui(self):
        self.action = QAction(QIcon(":/plugins/carregaCamadas/icon.png"), "Carrega camadas", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
    
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
    
    def run(self):
        self.caixote = QDialog(self.iface.mainWindow())
        self.ui = Ui_Dialog(self.caixote, self.iface)
        self.caixote.show()
        self.s = QSettings()
        self.s.beginGroup("PostgreSQL/connections")
        self.addCon()
        self.ui.pushButton.clicked.connect(self.acao)

    def acao(self):   
        if (self.ui.comboBox.currentIndex() != 0) and (self.ui.comboBox_2.currentIndex() != 0) and (self.ui.comboBox_4.currentIndex() != 0):
            self.teste=None
            try:
                db=self.ui.comboBox.currentText().replace(" ","")
                s = QSettings()
                s.beginGroup("PostgreSQL/connections")
                a=db+"/host"
                b=db+"/port"
                c=db+"/database"
                d=db+'/username'
                e=db+'/password'
                banconame = s.value(c)
                uri = QgsDataSourceURI()
                uri.setConnection(s.value(a), s.value(b), s.value(c), s.value(d), s.value(e))
                conn_string = "host="+s.value(a)+" dbname="+s.value(c)+" user="+s.value(d)+" password="+s.value(e)+" port="+s.value(b)
                conn = psycopg2.connect(conn_string)
                cursor = conn.cursor()
                self.layers = dict()
                cursor.execute("select f_table_schema, f_table_name, type from public.geometry_columns ;")
                for valores in cursor.fetchall():
                    if (valores[0] != 'tiger') and (valores[0] != 'public') and (valores[0] != 'validation'):
                        self.layers[valores[1]] = (valores[0],valores[2])
                self.styles={}
                cursor.execute("select id, stylename from layer_styles;")
                for valores in cursor.fetchall():
                    self.styles[valores[1]] = valores[0]
                cursor.close()    
             
            except:
                QMessageBox.warning(self.iface.mainWindow(),u"ERRO", u"Conecte-se a um 'BANCO DE DADOS' e salve seu 'USUÁRIO' e sua 'SENHA' e coloque a 'MÁQUINA' que está seu banco de dados")
                self.teste = "erro"
                
            if not self.teste == "erro":
                self.teste=None
                estilo = self.ui.comboBox_4.currentIndex()
                tipoCarregamento = self.ui.comboBox_2.currentIndex()
                self.loadDataBase(tipoCarregamento, estilo, uri, banconame)
                self.caixote.close()    
        else:
    		QMessageBox.warning(self.iface.mainWindow(),"ERRO", u"<font color=red>Para realizar a operação todos os campos devem estar definidos</font>")
 
    def initDialog(self):
        self.ui.comboBox_2.setCurrentIndex(0) 
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_4.setCurrentIndex(0) 
 
    def loadDataBase(self, tipoCarregamento, estilo, uri, banconame):
        root = QgsProject.instance().layerTreeRoot()
        grupodb = root.addGroup(banconame)
        p = grupodb.addGroup ('PONTO')
        l = grupodb.addGroup ('LINHA')
        a = grupodb.addGroup ('AREA')
        tipoGeom = {'MULTIPOLYGON': a, 'MULTILINESTRING': l, 'MULTIPOINT': p, 'POLYGON': a}
        schemaDic = {'MULTIPOLYGON':{},'MULTIPOINT':{},'MULTILINESTRING':{}, 'POLYGON' : {}}
        for layer in self.layers:
            layerName = layer
            schemaName = self.layers[layer][0]
            tipoLayer = self.layers[layer][1]
            layer = self.loadLayer(uri, layerName, tipoCarregamento)
            if layer:
                if not (tipoGeom[tipoLayer].findGroup(schemaName)):
                    schemaGrupo = tipoGeom[tipoLayer].addGroup(schemaName)
                    schemaDic[tipoLayer][schemaName] = schemaGrupo
                self.carregarEstilos(layer, estilo)
                schemaDic[tipoLayer][schemaName].addLayer(layer)
            
    def loadLayer(self, uri, layer, tipoCarregamento):
        uri.setDataSource(self.layers[layer][0], layer,"geom","","id")
        vlayer = QgsVectorLayer(uri.uri(), layer, "postgres")
        if (tipoCarregamento == 1) and (vlayer.allFeatureIds() != []):
            layer = QgsMapLayerRegistry.instance().addMapLayer(vlayer, False)
            return layer
        elif (tipoCarregamento == 2):
            layer = QgsMapLayerRegistry.instance().addMapLayer(vlayer, False)
            return layer
        else:
            return False 
    
    def carregarEstilos(self, layer, tipo):
        layer.loadDefaultStyle()
        tipoEstilo = { 1 : 'aquisicao_', 2 : 'reambulacao_', 3 : 'revisao_', 4 : 'vetorizacao_'}
        nomeEstilo = tipoEstilo[tipo]+layer.name()
        Estilo = layer.getStyleFromDatabase(str(self.styles.get(nomeEstilo)), "Estilo não encontrado")
        layer.applyNamedStyle(Estilo)			
            
    def addCon(self):
        try:
            connects=[]
            for x in self.s.allKeys():
                if x[-9:] == "/username":
                    connects.append(x[:-9])
            self.ui.comboBox.addItems(connects)
        except:
            QMessageBox.warning(self.iface.mainWindow(),"ERRO", u"Erro ao ler 'Conexões'")



