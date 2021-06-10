from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from k8s import UpdateSevice
import sys
import os
import re
import yaml
import resource

class Ui_k8s(object):
    def setupUi(self, k8s):
        k8s.setObjectName("k8s")
        k8s.resize(700, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(k8s.sizePolicy().hasHeightForWidth())
        k8s.setSizePolicy(sizePolicy)
        k8s.setMinimumSize(QtCore.QSize(700, 280))
        k8s.setMaximumSize(QtCore.QSize(700, 280))
        self.widget = QtWidgets.QWidget(k8s)
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 11, 651, 235))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.openFile = QtWidgets.QPushButton(self.layoutWidget)
        self.openFile.setObjectName("openFile")
        self.gridLayout.addWidget(self.openFile, 1, 3, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.alpha = QtWidgets.QCheckBox(self.layoutWidget)
        self.alpha.setObjectName("alpha")
        self.gridLayout.addWidget(self.alpha, 0, 1, 1, 1)
        self.pvztest = QtWidgets.QCheckBox(self.layoutWidget)
        self.pvztest.setObjectName("pvztest")
        self.gridLayout.addWidget(self.pvztest, 0, 2, 1, 1)
        self.pvzdev = QtWidgets.QCheckBox(self.layoutWidget)
        self.pvzdev.setObjectName("pvzdev")
        self.gridLayout.addWidget(self.pvzdev, 0, 3, 1, 1)
        self.authtest = QtWidgets.QCheckBox(self.layoutWidget)
        self.authtest.setObjectName("authtest")
        self.gridLayout.addWidget(self.authtest, 0, 4, 1, 1)
        self.view = QtWidgets.QTextBrowser(self.layoutWidget)
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 0, 5, 7, 1)
        self.stage = QtWidgets.QCheckBox(self.layoutWidget)
        self.stage.setObjectName("stage")
        self.gridLayout.addWidget(self.stage, 1, 1, 1, 1)
        self.hbtest = QtWidgets.QCheckBox(self.layoutWidget)
        self.hbtest.setObjectName("hbtest")
        self.gridLayout.addWidget(self.hbtest, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 2)
        self.readVersion = QtWidgets.QPushButton(self.layoutWidget)
        self.readVersion.setObjectName("readVersion")
        self.gridLayout.addWidget(self.readVersion, 4, 2, 1, 3)
        self.toVersion = QtWidgets.QLineEdit(self.layoutWidget)
        self.toVersion.setObjectName("toVersion")
        self.gridLayout.addWidget(self.toVersion, 5, 2, 1, 3)
        self.update = QtWidgets.QPushButton(self.layoutWidget)
        self.update.setObjectName("update")
        self.gridLayout.addWidget(self.update, 6, 2, 1, 3)
        self.getAllDeployment = QtWidgets.QPushButton(self.layoutWidget)
        self.getAllDeployment.setObjectName("getAllDeployment")
        self.gridLayout.addWidget(self.getAllDeployment, 2, 1, 1, 4)
        self.service = QtWidgets.QComboBox(self.layoutWidget)
        self.service.setEditable(True)
        self.service.setObjectName("service")
        self.gridLayout.addWidget(self.service, 3, 2, 1, 3)
        k8s.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(k8s)
        self.statusbar.setObjectName("statusbar")
        k8s.setStatusBar(self.statusbar)

        self.retranslateUi(k8s)
        QtCore.QMetaObject.connectSlotsByName(k8s)

    def retranslateUi(self, k8s):
        _translate = QtCore.QCoreApplication.translate
        k8s.setWindowTitle(_translate("k8s", "Kubernetes Client"))
        self.openFile.setText(_translate("k8s", "选择配置文件"))
        self.label.setText(_translate("k8s", "环境:"))
        self.alpha.setText(_translate("k8s", "alpha"))
        self.pvztest.setText(_translate("k8s", "pvztest"))
        self.pvzdev.setText(_translate("k8s", "pvzdev"))
        self.authtest.setText(_translate("k8s", "authtest"))
        self.stage.setText(_translate("k8s", "stage"))
        self.hbtest.setText(_translate("k8s", "hbtest"))
        self.label_2.setText(_translate("k8s", "请输入需要操作的服务:"))
        self.label_4.setText(_translate("k8s", "请输入需要更新到的版本:"))
        self.readVersion.setText(_translate("k8s", "读取当前版本"))
        self.update.setText(_translate("k8s", "更新服务"))
        self.getAllDeployment.setText(_translate("k8s", "获取全部服务"))

        self.readVersion.clicked.connect(self.getVersion)
        self.update.clicked.connect(self.updateSevice)
        self.openFile.clicked.connect(self.chooseFile)
        self.filenames_path = []
        self.getAllDeployment.clicked.connect(self.getAllDeploymentFromFristEnvironment)
        
    def chooseFile(self):
        self.filenames_path = QFileDialog.getOpenFileNames(None, "选取配置文件",'', "Yaml Files(*.yaml)")[0]
        count_file = len(self.filenames_path)
        self.openFile.setText("%d个文件已选择"%count_file)

    def getEnvironmentList(self):
        all_environment_list = ["alpha", "pvztest", "pvzdev", "authtest", "stage", "hbtest"]
        qt_list = vars(self)
        environment_list = []
        for env in all_environment_list:
            if(qt_list[env].isChecked()):
                # config_file_path = "config/kubeconfig_" + env + ".yaml"
                config_file_path = "config/kubeconfig_" + env + ".yaml"
                config_file_path = self.getResourcePath(config_file_path)
                environment_list.append(config_file_path)

        if(self.filenames_path != []):
            environment_list = environment_list + self.filenames_path

        return environment_list

    def getEnvironmentNameAndNamespace(self, file_path):
        config_file = open(file_path, 'r', encoding='utf-8')
        config = config_file.read()
         
        contexts = yaml.load(config)['contexts']
        environment = contexts[0]["name"]
        namespace = contexts[0]["context"]["namespace"]

        return environment + "::" + namespace

    def getAllDeploymentFromFristEnvironment(self):
        environment_list = self.getEnvironmentList()
        if(environment_list == []):
            self.appendText("请至少选择一个环境！")
        else:
            service_list = []
            for env in environment_list:
                try:
                    client = UpdateSevice(env)
                    response = client.getDeploymentList()
                    # print(response)
                    service_list.extend(response)
                    service_list = sorted(list(set(service_list)))
                    self.appendText("<font color=green>%s全部部署加载完成!</font>"%self.getEnvironmentNameAndNamespace(env))
                    # for service in response:
                    #     self.appendText(service)
                except Exception as e:
                    self.appendText("<font color=red>%s</font>"%str(e))

            self.setSelectList(service_list)

    def getVersion(self):
        environment_list = self.getEnvironmentList()
        if(environment_list == []):
            self.appendText("请至少选择一个环境！")
        else:
            for env in environment_list:
                try:
                    client = UpdateSevice(env)
                    response = client.getCurrentVersion(self.service.currentText())
                    self.appendText("<b>%s</b>:<br/>"%self.getEnvironmentNameAndNamespace(env) + response)
                except Exception as e:
                    self.appendText("<font color=red>%s</font>"%str(e))

    def updateSevice(self):
        environment_list = self.getEnvironmentList()
        if(environment_list == []):
            self.appendText("请至少选择一个环境！")
        else:
            if(re.findall(self.service.currentText() + ':', self.toVersion.text()) != []):
                for env in environment_list:
                    try:
                        client = UpdateSevice(env)
                        response = client.updateServie(self.service.currentText(), self.toVersion.text())
                        self.appendText("<b>%s</b>:<br/>"%self.getEnvironmentNameAndNamespace(env) + response)
                    except Exception as e:
                        self.appendText("<font color=red>%s</font>"%str(e))

            else:
                self.appendText("<font color=#F58220>要更新的版本号格式错误,未执行更新!</font>")

    def setSelectList(self, service_list):
        i = 0
        self.service.clear()
        for deployment in service_list:
            self.service.addItem("")
            self.service.setItemText(i, str(deployment))
            i += 1

    def appendText(self, text):
        self.view.append(text)
        self.view.moveCursor(self.view.textCursor().End)

    def getResourcePath(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        
        return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    k8s_client = QtWidgets.QApplication(sys.argv)
    myWindow = QtWidgets.QMainWindow()
    window = Ui_k8s()
    window.setupUi(myWindow)
    myWindow.setWindowIcon(QtGui.QIcon(":/icon.ico"))# windows添加左上角小图标
    myWindow.show()
    sys.exit(k8s_client.exec_())
