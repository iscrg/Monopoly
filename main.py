import threading
from time import sleep
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtCore

class ui(QMainWindow):
    def __init__(self):
        super().__init__()

        #Connect to signals
        self.sgnl = Signals()
        self.sgnl.kapyTextEditSgnl.connect(self.kapyTextEdit)
        self.sgnl.dogTextEditSgnl.connect(self.dogTextEdit)
        self.sgnl.gazmanovTextEditSgnl.connect(self.gazmanovTextEdit)
        self.sgnl.parrotTextEditSgnl.connect(self.parrotTextEdit)
        self.sgnl.consoleMessageSgnl.connect(self.printMessage)

        #Start UI
        self.ui = uic.loadUi('ui.ui')
        self.ui.show()

        #Hide players and score
        self.ui.pushButton.setEnabled(False)
        self.ui.kapyScore.setHidden(True)
        self.ui.kapyPlayer.setHidden(True)
        self.ui.dogScore.setHidden(True)
        self.ui.dogPlayer.setHidden(True)
        self.ui.gazmanovScore.setHidden(True)
        self.ui.gazmanovPlayer.setHidden(True)
        self.ui.parrotScore.setHidden(True)
        self.ui.parrotPlayer.setHidden(True)

        #Connect to button
        self.ui.pushButton.clicked.connect(self.readValue)

    #Printing message
    def printMessageEvnt(self, value):
        self.sgnl.consoleMessageSgnl.emit(value)

    def printMessage(self, value):
        self.ui.console.append(f'<span style="font-weight:600;"> [Система]</span> {value}')

    #Reading data from chat.
    def buttonEnadle(self):
        self.ui.pushButton.setEnabled(True)

    def readValue(self):
        global chatData
        global CurrentPlayer

        self.ui.pushButton.setEnabled(False)

        player = CurrentPlayer

        self.ui.console.append(f'<span style="font-weight:600;"> [{player}]</span> {self.ui.inputLine.text()}')
        chatData = self.ui.inputLine.text()
        dataReadyEvent.set()

    #Kapy control
    def kapyEnable(self, value):
        self.ui.kapyScore.setHidden(value)
        self.ui.kapyPlayer.setHidden(value)

    def kapyTextEditEvnt(self, initValue, finalValue):
        self.sgnl.kapyTextEditSgnl.emit(initValue, finalValue)

    def kapyPosEdit(self, x, y):
        self.ui.kapyPlayer.move(x, y)

    def kapyTextEdit(self, initValue, finalValue):
        print(initValue, finalValue)
        html = self.ui.kapyScore.toHtml()
        print(html)
        html = html.replace(initValue, finalValue)
        self.ui.kapyScore.setHtml(html)

    #Dog control
    def dogEnable(self, value):
        self.ui.dogScore.setHidden(value)
        self.ui.dogPlayer.setHidden(value)

    def dogTextEditEvnt(self, initValue, finalValue):
        self.sgnl.dogTextEditSgnl.emit(initValue, finalValue)

    def dogPosEdit(self, x, y):
        self.ui.dogPlayer.move(x, y)

    def dogTextEdit(self, initValue, finalValue):
        html = self.ui.dogScore.toHtml()
        html = html.replace(initValue, finalValue)
        self.ui.dogScore.setHtml(html)


    #Gazmanov control
    def gazmanovEnable(self, value):
        self.ui.gazmanovScore.setHidden(value)
        self.ui.gazmanovPlayer.setHidden(value)

    def gazmanovTextEditEvnt(self, initValue, finalValue):
        self.sgnl.gazmanovTextEditSgnl.emit(initValue, finalValue)

    def gazmanovPosEdit(self, x, y):
        self.ui.gazmanovPlayer.move(x, y)

    def gazmanovTextEdit(self, initValue, finalValue):
        html = self.ui.gazmanovScore.toHtml()
        html = html.replace(initValue, finalValue)
        self.ui.gazmanovScore.setHtml(html)


    #Parrot control
    def parrotEnable(self, value):
        self.ui.parrotScore.setHidden(value)
        self.ui.parrotPlayer.setHidden(value)

    def parrotTextEditEvnt(self, initValue, finalValue):
        self.sgnl.parrotTextEditSgnl.emit(initValue, finalValue)

    def parrotPosEdit(self, x, y):
        self.ui.parrotPlayer.move(x, y)

    def parrotTextEdit(self, initValue, finalValue):
        html = self.ui.parrotScore.toHtml()
        html = html.replace(initValue, finalValue)
        self.ui.parrotScore.setHtml(html)


    #Dice control
    def dice(self, value):
        self.ui.imgDice.setPixmap(QtGui.QPixmap(f"img/dice/{value}.png"))

#Adding signals for edit score tables.
class Signals(QtCore.QObject):
    kapyTextEditSgnl = QtCore.pyqtSignal(str, str)
    dogTextEditSgnl = QtCore.pyqtSignal(str, str)
    gazmanovTextEditSgnl = QtCore.pyqtSignal(str, str)
    parrotTextEditSgnl = QtCore.pyqtSignal(str, str)
    consoleMessageSgnl = QtCore.pyqtSignal(str)

#Class for controlling UI.
class uiControl():
    def readData(player):
        global chatData
        global CurrentPlayer

        chatData = None
        CurrentPlayer = player

        dataReadyEvent.clear()
        ui.buttonEnadle(ex)
        dataReadyEvent.wait()
        dataReadyEvent.clear()

        return chatData
        

    class move():
        def kapy(x, y):
            ui.kapyPosEdit(ex, x, y)

        def dog(x, y):
            ui.dogPosEdit(ex, x, y)

        def gazmanov(x, y):
            ui.gazmanovPosEdit(ex, x, y) 

        def parrot(x, y):
            ui.gazmanotPosEdit(ex, x, y)

    class score():
        class property():
            class add():

                def kapy(value):
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                def dog(value):
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                def gazmanov(value):
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                def parrot(value):
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)


            class remove():

                def kapy(value):
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                def dog(value):
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                def gazmanov(value):
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                def parrot(value):
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)


        class balance():
            def kapy(initValue, finalValue):
                initValue_ = f'</span> {initValue}<br />'
                finalValue_ = f'</span> {finalValue}<br />'
                ui.kapyTextEditEvnt(ex, initValue_, finalValue_)

            def dog(initValue, finalValue):
                initValue_ = f'</span> {initValue}<br />'
                finalValue_ = f'</span> {finalValue}<br />'
                ui.dogTextEditEvnt(ex, initValue_, finalValue_)

            def gazmanov(initValue, finalValue):
                initValue_ = f'</span> {initValue}<br />'
                finalValue_ = f'</span> {finalValue}<br />'
                ui.gazmanovTextEditEvnt(ex, initValue_, finalValue_)

            def parrot(initValue, finalValue):
                initValue_ = f'</span> {initValue}<br />'
                finalValue_ = f'</span> {finalValue}<br />'
                ui.parrotTextEditEvnt(ex, initValue_, finalValue_)

        class status():
            def kapy(initValue, finalValue):
                initValue_ = f'</span>{initValue}<br />'
                finalValue_ = f'</span>{finalValue}<br />'
                ui.kapyTextEditEvnt(ex, initValue_, finalValue_)

            def dog(initValue, finalValue):
                initValue_ = f'</span> {finalValue}<br />'
                finalValue_ = f'</span> {finalValue}<br />'
                ui.dogTextEditEvnt(ex, initValue_, finalValue_)

            def gazmanov(initValue, finalValue):
                initValue_ = f'</span> {finalValue}<br />'
                finalValue_ = f'</span> {finalValue}<br />'
                ui.gazmanovTextEditEvnt(ex, initValue_, finalValue_)

            def parrot(initValue, finalValue):
                initValue_ = f'</span> {finalValue}<br />'
                finalValue_ = f'</span> {finalValue}<br />'
                ui.parrotTextEditEvnt(ex, initValue_, finalValue_)

    def diceValue(value):
            ui.dice(ex, value)
        

    def message(value):
        ui.printMessageEvnt(ex, value)

    class hide:
        def kapy(value):
            ui.kapyEnable(ex, value)

        def dog(value):
            ui.dogEnable(ex, value)

        def gazmanov(value):
            ui.gazmanovEnable(ex, value)

        def parrot(value):
            ui.parrotEnable(ex, value)

def backend():
    check = True
    while check == True:
        data = uiControl.readData('Система')
        if data == '2':
            uiControl.hide.kapy(False)
            uiControl.hide.dog(False)
            check = False
        elif data == '3':
            uiControl.hide.kapy(False)
            uiControl.hide.dog(False)
            uiControl.hide.gazmanov(False)
            check =  False
        elif data == '4':
            uiControl.hide.kapy(False)
            uiControl.hide.dog(False)
            uiControl.hide.gazmanov(False)
            uiControl.hide.parrot(False)
            check = False
        else:
            uiControl.message('Выберите от 2 до 4 игроков!')
            continue

    uiControl.readData('Капибара')

    uiControl.readData('Собака')

    uiControl.readData('Олег Газманов')

    uiControl.readData('Попугай')

def main():
    global ex
    global dataReadyEvent
    app = QApplication(sys.argv)
    ex = ui()

    dataReadyEvent = threading.Event()

    trd = threading.Thread(target=backend)
    trd.start()

    app.exec_()


if __name__ == '__main__':
    main()