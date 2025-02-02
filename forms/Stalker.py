import os

from PyQt5.QtWidgets import QDialog, QMessageBox

from ui.stalker import Ui_StalkerDialog


class stalkerForm(QDialog,Ui_StalkerDialog):
    def __init__(self, parent=None):
        super(stalkerForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowOpacity(0.93)
        self.btnSubmit.clicked.connect(self.submit)
        self.btnClear.clicked.connect(self.clearUi)
        self.clearUi()
        self.flushCmb()
        self.listModule.itemClicked.connect(self.ModuleItemClick)
        self.txtModule.textChanged.connect(self.changeModule)
        self.cmbPackage.currentTextChanged.connect(self.changePackage)
        self.modules = None

    def initData(self):
        self.listModule.clear()
        for item in self.modules:
            self.listModule.addItem(item)

    def flushCmb(self):
        self.cmbPackage.clear()
        files = os.listdir("./tmp/")
        self.cmbPackage.addItem("tmp data")
        for item in files:
            if ".modules.txt" in item:
                self.cmbPackage.addItem(item.replace(".modules.txt", ""))

    def ModuleItemClick(self, item):
        self.txtModule.setText(item.text())

    def changeModule(self, data):
        if self.modules==None or len(self.modules)<=0:
            return
        if data == "" or data == "tmp data":
            return
        self.listModule.clear()
        if len(data) > 0:
            for item in self.modules:
                if data in item:
                    self.listModule.addItem(item)
        else:
            for item in self.modules:
                self.listModule.addItem(item)

    def changePackage(self, data):
        if data=="" or data=="tmp data":
            return
        filepath = "./tmp/" + data + ".modules.txt"
        with open(filepath, "r", encoding="utf-8") as packageFile:
            res = packageFile.read()
            self.modules = res.split("\n")
        self.initData()

    def clearUi(self):
        self.txtSymbol.setText("")
        self.txtOffset.setText("")
        self.txtModule.setText("")

    def submit(self):
        moduleName = self.txtModule.text()
        offset = self.txtOffset.text()
        symbol= self.txtSymbol.text()
        if len(moduleName) <= 0:
            QMessageBox().information(self, "hint", "missing module")
            return
        if len(offset) <= 0 and len(symbol)<=0:
            QMessageBox().information(self, "hint", "must enter offset or symbol")
            return
        self.moduleName = moduleName
        self.offset = offset
        self.symbol = symbol
        self.accept()