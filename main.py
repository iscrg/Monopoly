import threading
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtCore


class ui(QMainWindow):
    def __init__(self):
        super().__init__()

        # Connect to signals
        self.sgnl = Signals()
        self.sgnl.kapyTextEditSgnl.connect(self.kapyTextEdit)
        self.sgnl.dogTextEditSgnl.connect(self.dogTextEdit)
        self.sgnl.gazmanovTextEditSgnl.connect(self.gazmanovTextEdit)
        self.sgnl.parrotTextEditSgnl.connect(self.parrotTextEdit)
        self.sgnl.consoleMessageSgnl.connect(self.printMessage)

        # Start UI
        self.ui = uic.loadUi('ui.ui')
        self.ui.show()

        # Hide playersQuantity and score
        self.ui.pushButton.setEnabled(False)
        self.ui.kapyScore.setHidden(True)
        self.ui.kapyPlayer.setHidden(True)
        self.ui.dogScore.setHidden(True)
        self.ui.dogPlayer.setHidden(True)
        self.ui.gazmanovScore.setHidden(True)
        self.ui.gazmanovPlayer.setHidden(True)
        self.ui.parrotScore.setHidden(True)
        self.ui.parrotPlayer.setHidden(True)

        # Connect to button
        self.ui.pushButton.clicked.connect(self.readValue)

    # Printing message
    def printMessageEvnt(self, value):
        self.sgnl.consoleMessageSgnl.emit(value)

    def printMessage(self, value):
        self.ui.console.append(f'<span style="font-weight:600;font-size:12pt;"> [Сказочные Разработчики]</span> <span style="font-size:12pt;">{value}</span>')

    # Reading data from chat.
    def buttonEnadle(self):
        self.ui.pushButton.setEnabled(True)

    def readValue(self):
        global chatData
        global CurrentPlayer

        self.ui.pushButton.setEnabled(False)

        player = CurrentPlayer

        self.ui.console.append(f'<span style="font-weight:600;font-size:12pt;"> [{player}]</span> <span style="font-size:12pt;">{self.ui.inputLine.text()}</span>')
        chatData = self.ui.inputLine.text()
        self.ui.inputLine.setText('')
        dataReadyEvent.set()

    # Kapy control
    def kapyEnable(self, value):
        self.ui.kapyScore.setHidden(value)
        self.ui.kapyPlayer.setHidden(value)

    def kapyTextEditEvnt(self, initValue, finalValue):
        self.sgnl.kapyTextEditSgnl.emit(initValue, finalValue)

    def kapyPosEdit(self, x, y):
        self.ui.kapyPlayer.move(int(x), int(y))

    def kapyTextEdit(self, initValue, finalValue):
        html = self.ui.kapyScore.toHtml()
        html = html.replace(initValue, finalValue)
        self.ui.kapyScore.setHtml(html)

    # Dog control
    def dogEnable(self, value):
        self.ui.dogScore.setHidden(value)
        self.ui.dogPlayer.setHidden(value)

    def dogTextEditEvnt(self, initValue, finalValue):
        self.sgnl.dogTextEditSgnl.emit(initValue, finalValue)

    def dogPosEdit(self, x, y):
        self.ui.dogPlayer.move(int(x), int(y))

    def dogTextEdit(self, initValue, finalValue):
        html = self.ui.dogScore.toHtml()
        html = html.replace(initValue, finalValue)
        self.ui.dogScore.setHtml(html)

    # Gazmanov control
    def gazmanovEnable(self, value):
        self.ui.gazmanovScore.setHidden(value)
        self.ui.gazmanovPlayer.setHidden(value)

    def gazmanovTextEditEvnt(self, initValue, finalValue):
        self.sgnl.gazmanovTextEditSgnl.emit(initValue, finalValue)

    def gazmanovPosEdit(self, x, y):
        self.ui.gazmanovPlayer.move(int(x), int(y))

    def gazmanovTextEdit(self, initValue, finalValue):
        html = self.ui.gazmanovScore.toHtml()
        html = html.replace(initValue, finalValue)
        self.ui.gazmanovScore.setHtml(html)

    # Parrot control
    def parrotEnable(self, value):
        self.ui.parrotScore.setHidden(value)
        self.ui.parrotPlayer.setHidden(value)

    def parrotTextEditEvnt(self, initValue, finalValue):
        self.sgnl.parrotTextEditSgnl.emit(initValue, finalValue)

    def parrotPosEdit(self, x, y):
        self.ui.parrotPlayer.move(int(x), int(y))

    def parrotTextEdit(self, initValue, finalValue):
        html = self.ui.parrotScore.toHtml()
        html = html.replace(initValue, finalValue)
        self.ui.parrotScore.setHtml(html)

    # Dice control
    def dice(self, value):
        self.ui.imgDice.setPixmap(QtGui.QPixmap(f"img/dice/{value}.png"))


# Adding signals for edit score tables.
class Signals(QtCore.QObject):
    kapyTextEditSgnl = QtCore.pyqtSignal(str, str)
    dogTextEditSgnl = QtCore.pyqtSignal(str, str)
    gazmanovTextEditSgnl = QtCore.pyqtSignal(str, str)
    parrotTextEditSgnl = QtCore.pyqtSignal(str, str)
    consoleMessageSgnl = QtCore.pyqtSignal(str)


# Class for controlling UI.
class uiControl():
    def readData(player):
        global chatData
        global CurrentPlayer

        chatData = None
        CurrentPlayer = player

        dataReadyEvent.clear()
        ui.buttonEnadle(ex)
        dataReadyEvent.wait()

        return chatData

    def move(player, x, y):
        if player == 'kapy':
            ui.kapyPosEdit(ex, x, y)

        elif player == 'dog':
            ui.dogPosEdit(ex, x, y)

        elif player == 'gazmanov':
            ui.gazmanovPosEdit(ex, x, y)

        elif player == 'parrot':
            ui.parrotPosEdit(ex, x, y)

    class score():
        class property():
            def add(player, value):

                if player == 'kapy':
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                elif player == 'dog':
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                elif player == 'gazmanov':
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                elif player == 'parrot':
                    initValue = '</p></body></html>'
                    finalValue = f'<br />{value}</p></body></html>'
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)

            def remove(player, value):

                if player == 'kapy':
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                elif player == 'dog':
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                elif player == 'gazmanov':
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                elif player == 'parrot':
                    initValue = f'<br />{value}'
                    finalValue = ''
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)

        def balance(player, initValue, finalValue):
            if player == 'kapy':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.kapyTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'dog':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.dogTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'gazmanov':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.gazmanovTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'parrot':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.parrotTextEditEvnt(ex, initValue_, finalValue_)

        def status(player, initValue, finalValue):
            if player == 'kapy':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.kapyTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'dog':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.dogTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'gazmanov':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.gazmanovTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'parrot':
                initValue_ = f'>{initValue}<'
                finalValue_ = f'>{finalValue}<'
                ui.parrotTextEditEvnt(ex, initValue_, finalValue_)

    def diceValue(value):
        ui.dice(ex, value)

    def message(value):
        ui.printMessageEvnt(ex, value)

    def hide(player, value):
        if player == 'kapy':
            ui.kapyEnable(ex, value)

        elif player == 'dog':
            ui.dogEnable(ex, value)

        elif player == 'gazmanov':
            ui.gazmanovEnable(ex, value)

        elif player == 'parrot':
            ui.parrotEnable(ex, value)


def backend():

    def vanya():
        pass

    def danya():
        eventsData = []
        with open('data/events.txt', encoding="utf-8") as file:
            for line in file.readlines():
                eventsData.append(line.rstrip('\n'))

        pointsData = []
        with open('data/points.txt', encoding="utf-8") as file:
            for line in file.readlines():
                pointsData.append(line.rstrip('\n'))

        rentData = []
        with open('data/rent.txt') as file:
            for line in file.readlines():
                p = line.rstrip('\n').split(' ')
                rentData.append([int(p[0]), int(p[1])])

        posmsgPos = []
        with open('pos/posmsg.txt', encoding="utf-8") as file:
            for line in file.readlines():
                 posmsgPos.append(line.rstrip('\n'))

        if data[playerName]['position'] == 9 or data[playerName]['position'] == 20:
            
            event = random.randint(0,9)

            uiControl.message(posmsgPos[data[playerName]['position']])
            decision = uiControl.readData(data[playerName]['name'])

            if decision == 'y':

                if event == 0:
                    uiControl.message(eventsData[event])

                    xPos = pointPositions[playerName][6][0]
                    yPos = pointPositions[playerName][6][1]

                    uiControl.move(playerName, xPos, yPos)
                    data[playerName]['position'] = 6

                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] - 195)
                    data[playerName]['balance'] = data[playerName]['balance'] - 195
                    print(data[playerName]['balance'])
                    uiControl.score.status(playerName, 'В игре', 'В НГУ')
                
                elif event == 1:
                    uiControl.message(eventsData[event])

                    xPos = pointPositions[playerName][23][0]
                    yPos = pointPositions[playerName][23][1]

                    uiControl.move(playerName, xPos, yPos)
                    data[playerName]['position'] = 23

                elif event == 2:
                    uiControl.message(eventsData[event])

                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                    data[playerName]['balance'] = data[playerName]['balance'] + 100
                    
                    xPos = pointPositions[playerName][2][0]
                    yPos = pointPositions[playerName][2][1]

                    uiControl.move(playerName, xPos, yPos)
                    data[playerName]['position'] = 2
                
                elif event == 3:
                    uiControl.message(eventsData[event])

                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 50)
                    data[playerName]['balance'] = data[playerName]['balance'] + 50

                elif event == 4:
                    uiControl.message(eventsData[event])

                    if data[playerName]['position'] > 19:
                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                        data[playerName]['balance'] = data[playerName]['balance'] + 100
                    
                    xPos = pointPositions[playerName][19][0]
                    yPos = pointPositions[playerName][19][1]

                    uiControl.move(playerName, xPos, yPos)
                    data[playerName]['position'] = 19
                
                elif event == 5:
                    uiControl.message(eventsData[event])

                    if data[playerName]['position'] > 15:
                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                        data[playerName]['balance'] = data[playerName]['balance'] + 100
                    
                    xPos = pointPositions[playerName][15][0]
                    yPos = pointPositions[playerName][15][1]

                    uiControl.move(playerName, xPos, yPos)
                    data[playerName]['position'] = 15
                
                elif event == 6:
                    uiControl.message(eventsData[event])

                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                    data[playerName]['balance'] = data[playerName]['balance'] + 100
                    
                    xPos = pointPositions[playerName][0][0]
                    yPos = pointPositions[playerName][0][1]

                    uiControl.move(playerName, xPos, yPos)
                    data[playerName]['position'] = 0

                elif event == 7:
                    uiControl.message(eventsData[event])

                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] - 70)
                    data[playerName]['balance'] = data[playerName]['balance'] - 70

                elif event == 8:
                    uiControl.message(eventsData[event])

                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 50)
                    data[playerName]['balance'] = data[playerName]['balance'] + 50
                    
                    xPos = pointPositions[playerName][4][0]
                    yPos = pointPositions[playerName][4][1]

                    uiControl.move(playerName, xPos, yPos)
                    data[playerName]['position'] = 4
                
                elif event == 9:
                    uiControl.message(eventsData[event])

                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] - 70)
                    data[playerName]['balance'] = data[playerName]['balance'] - 70

        pass

    def fediuk():
        costData = []
        with open('data/cost.txt') as file:
            for line in file.readlines():
                p = line.rstrip('\n')
                costData.append(int(p))
        rentData = []
        with open('data/rent.txt') as file:
            for line in file.readlines():
                p = line.rstrip('\n').split(' ')
                rentData.append([int(p[0]), int(p[1])])
        pointsData = []
        with open('data/points.txt', encoding="utf-8") as file:
            for line in file.readlines():
                pointsData.append(line.rstrip('\n'))


        for NamePlayer in playerNames:
            if data [playerName]['position'] in data[NamePlayer]['property']:
                pass
        else:
            uiControl.message("Если хотите купить этот объект - введите 'y'. В противном случае 'n'")
            decision = uiControl.readData(playerName)
            if decision == 'y':
                if data[playerName]['balance'] >= costData[data[playerName]['position']]:
                    data[playerName]['property'].append(data[playerName]['position'])
                    uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] - costData[data[playerName]['position']])
                    data[playerName]['balance'] -= costData[data[playerName]['position']]
                    uiControl.score.property.add(playerName, pointsData[data[playerName]['position']])
            elif decision == 'n':
                pass
                

        












    playerNames = ['kapy', 'dog', 'gazmanov', 'parrot']

    data = {
        'kapy': {
            'name': 'Капибара',
            'balance': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': []
        },

        'dog': {
            'name': 'Опухший пес',
            'balance': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': []
        },

        'gazmanov': {
            'name': 'Олег Газманов',
            'balance': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': []
        },

        'parrot': {
            'name': 'Попуг',
            'balance': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': []
        }

    }

    playersQuantity = 0

    diceMessages = []

    eventsData = []

    posmsgPos = []

    pointPositions = {
        'kapy': [],
        'dog': [],
        'gazmanov': [],
        'parrot': []
    }

    for playerName in playerNames:
        with open(f'pos/{playerName}.txt') as file:
            for line in file.readlines():
                line = line.rstrip('\n').split(' ')
                pointPositions[playerName].append(line)

    with open('data/dicemsg.txt', encoding='utf-8') as file:
        for line in file.readlines():
            diceMessages.append(line.rstrip('\n'))
    
    with open('data/events.txt', encoding="utf-8") as file:
        for line in file.readlines():
            eventsData.append(line.rstrip('\n'))
    
    with open('pos/posmsg.txt', encoding="utf-8") as file:
        for line in file.readlines():
                posmsgPos.append(line.rstrip('\n'))

    while True:
        uiControl.message('Введите количество игроков от 2 до 4.')
        playersQuantity = uiControl.readData('Игрок')

        try:
            playersQuantity = int(playersQuantity)
            if not (2 <= playersQuantity <= 4):
                continue
        except:
            continue

        playerNames = playerNames[:playersQuantity]

        for playerName in playerNames:
            uiControl.hide(playerName, False)
            uiControl.score.balance(playerName, 0, 1000)
            data[playerName]['balance'] = 1000
            uiControl.score.status(playerName, 'Не в игре', 'В игре')

        break

    while True:
        for playerName in playerNames:
            uiControl.message(f'{data[playerName]["name"]}, чтобы кинуть кубик - введите "y"')
            decision = uiControl.readData(data[playerName]['name'])

            if decision == 'y':
                dice_number = random.randint(1, 6)
                uiControl.diceValue(dice_number)
                uiControl.message(diceMessages[dice_number-1])

                playerPos = data[playerName]['position']

                if playerPos + dice_number > 23:
                    playerPos = dice_number - (24-playerPos)

                    xPos = pointPositions[playerName][playerPos][0]
                    yPos = pointPositions[playerName][playerPos][1]

                    uiControl.move(playerName, xPos, yPos)

                else:
                    playerPos += dice_number

                    xPos = pointPositions[playerName][playerPos][0]
                    yPos = pointPositions[playerName][playerPos][1]

                    uiControl.move(playerName, xPos, yPos)

                data[playerName]['position'] = playerPos
            
            if data[playerName]['position'] == 9 or data[playerName]['position'] == 20:
            
                event = random.randint(0,9)

                uiControl.message(posmsgPos[data[playerName]['position']])
                decision = uiControl.readData(data[playerName]['name'])

                if decision == 'y':

                    if event == 0:
                        uiControl.message(eventsData[event])

                        xPos = pointPositions[playerName][6][0]
                        yPos = pointPositions[playerName][6][1]

                        uiControl.move(playerName, xPos, yPos)
                        data[playerName]['position'] = 6

                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] - 195)
                        data[playerName]['balance'] = data[playerName]['balance'] - 195
                        print(data[playerName]['balance'])
                        uiControl.score.status(playerName, 'В игре', 'В НГУ')
                    
                    elif event == 1:
                        uiControl.message(eventsData[event])

                        xPos = pointPositions[playerName][23][0]
                        yPos = pointPositions[playerName][23][1]

                        uiControl.move(playerName, xPos, yPos)
                        data[playerName]['position'] = 23

                    elif event == 2:
                        uiControl.message(eventsData[event])

                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                        data[playerName]['balance'] = data[playerName]['balance'] + 100
                        
                        xPos = pointPositions[playerName][2][0]
                        yPos = pointPositions[playerName][2][1]

                        uiControl.move(playerName, xPos, yPos)
                        data[playerName]['position'] = 2
                    
                    elif event == 3:
                        uiControl.message(eventsData[event])

                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 50)
                        data[playerName]['balance'] = data[playerName]['balance'] + 50

                    elif event == 4:
                        uiControl.message(eventsData[event])

                        if data[playerName]['position'] > 19:
                            uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                            data[playerName]['balance'] = data[playerName]['balance'] + 100
                        
                        xPos = pointPositions[playerName][19][0]
                        yPos = pointPositions[playerName][19][1]

                        uiControl.move(playerName, xPos, yPos)
                        data[playerName]['position'] = 19
                    
                    elif event == 5:
                        uiControl.message(eventsData[event])

                        if data[playerName]['position'] > 15:
                            uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                            data[playerName]['balance'] = data[playerName]['balance'] + 100
                        
                        xPos = pointPositions[playerName][15][0]
                        yPos = pointPositions[playerName][15][1]

                        uiControl.move(playerName, xPos, yPos)
                        data[playerName]['position'] = 15
                    
                    elif event == 6:
                        uiControl.message(eventsData[event])

                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 100)
                        data[playerName]['balance'] = data[playerName]['balance'] + 100
                        
                        xPos = pointPositions[playerName][0][0]
                        yPos = pointPositions[playerName][0][1]

                        uiControl.move(playerName, xPos, yPos)
                        data[playerName]['position'] = 0

                    elif event == 7:
                        uiControl.message(eventsData[event])

                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] - 70)
                        data[playerName]['balance'] = data[playerName]['balance'] - 70

                    elif event == 8:
                        uiControl.message(eventsData[event])

                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] + 50)
                        data[playerName]['balance'] = data[playerName]['balance'] + 50
                        
                        xPos = pointPositions[playerName][4][0]
                        yPos = pointPositions[playerName][4][1]

                        uiControl.move(playerName, xPos, yPos)
                        data[playerName]['position'] = 4
                    
                    elif event == 9:
                        uiControl.message(eventsData[event])

                        uiControl.score.balance(playerName, data[playerName]['balance'], data[playerName]['balance'] - 70)
                        data[playerName]['balance'] = data[playerName]['balance'] - 70
            else:
                fediuk()

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
