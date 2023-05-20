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
        self.ui.endImg.setHidden(True)

        # Connect to button
        self.ui.inputLine.returnPressed.connect(self.readValue)
        self.ui.pushButton.clicked.connect(self.readValue)

    # Printing message
    def printMessageEvnt(self, value):
        self.sgnl.consoleMessageSgnl.emit(value)

    def printMessage(self, msg):
        self.ui.console.append(f'<span style=" font-size:12pt;">{msg}</span></body></html>')

    # Reading data from chat.
    def buttonEnadle(self):
        self.ui.pushButton.setEnabled(True)

    def readValue(self):
        global chatData
        global CurrentPlayer

        self.ui.pushButton.setEnabled(False)

        player = CurrentPlayer

        self.ui.console.append(f'<span style="font-weight:600;font-size:12pt;">[{player}]</span> <span style="font-size:12pt;">{self.ui.inputLine.text()}</span>')
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

    def endImgHide(self):
        self.ui.endImg.setHidden(False)


# Adding signals for edit score tables.
class Signals(QtCore.QObject):
    kapyTextEditSgnl = QtCore.pyqtSignal(str, str)
    dogTextEditSgnl = QtCore.pyqtSignal(str, str)
    gazmanovTextEditSgnl = QtCore.pyqtSignal(str, str)
    parrotTextEditSgnl = QtCore.pyqtSignal(str, str)
    consoleMessageSgnl = QtCore.pyqtSignal(str)


# Class for controlling UI.
class uiCtrl():
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
                initValue = '</p></body></html>'
                finalValue = f'<br /><span style="font-size:10pt;">{value}</span></p></body></html>'

                if player == 'kapy':
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                elif player == 'dog':
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                elif player == 'gazmanov':
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                elif player == 'parrot':
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)

            def remove(player, value):
                initValue = f'<br /><span style="font-size:10pt;">{value}</span></p></body></html>'
                finalValue = ''

                if player == 'kapy':
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                elif player == 'dog':
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                elif player == 'gazmanov':
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                elif player == 'parrot':
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)

        def bs(player, initValue, finalValue):
            initValue_ = f'>{initValue}<'
            finalValue_ = f'>{finalValue}<'

            if player == 'kapy':
                ui.kapyTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'dog':
                ui.dogTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'gazmanov':
                ui.gazmanovTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'parrot':
                ui.parrotTextEditEvnt(ex, initValue_, finalValue_)

        def status(player, initValue, finalValue):
            initValue_ = f'>{initValue}<'
            finalValue_ = f'>{finalValue}<'

            if player == 'kapy':
                ui.kapyTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'dog':
                ui.dogTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'gazmanov':
                ui.gazmanovTextEditEvnt(ex, initValue_, finalValue_)

            elif player == 'parrot':
                ui.parrotTextEditEvnt(ex, initValue_, finalValue_)

    def diceVal(value):
        ui.dice(ex, value)

    def message(type_, msg):
        if type_ == 'dev':
            msg = f'<span style="font-weight:600;font-size:12pt;">[Сказочные Разработчики]</span> <span style="font-size:12pt;">{msg}</span>'
        elif type_ == 'separator':
            msg = '<hr>'
        ui.printMessageEvnt(ex, msg)

    def hide(player, value):
        if player == 'kapy':
            ui.kapyEnable(ex, value)

        elif player == 'dog':
            ui.dogEnable(ex, value)

        elif player == 'gazmanov':
            ui.gazmanovEnable(ex, value)

        elif player == 'parrot':
            ui.parrotEnable(ex, value)

    def endImg():
        ui.endImgHide(ex)


def backend():
    pNames = ['kapy', 'dog', 'gazmanov', 'parrot']

    data = {
        'kapy': {
            'name': 'Капибара',
            'bs': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': [],
            'countNSU': 0
        },

        'dog': {
            'name': 'Опухший пес',
            'bs': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': [],
            'countNSU': 0
        },

        'gazmanov': {
            'name': 'Олег Газманов',
            'bs': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': [],
            'countNSU': 0
        },

        'parrot': {
            'name': 'Попуг',
            'bs': 0,
            'status': 'Не в игре',
            'position': 0,
            'property': [],
            'countNSU': 0
        }

    }

    playersQuantity = 0

    countMoves = 0

    streetsCombin = [[1, 3],
                     [5, 7, 8],
                     [10, 13, 14],
                     [16, 17, 19],
                     [21, 23],
                     [2, 11],
                     [4, 15, 22]]

    pointPos = {
        'kapy': [],
        'dog': [],
        'gazmanov': [],
        'parrot': []
    }

    for pName in pNames:
        with open(f'pos/{pName}.txt') as file:
            for line in file.readlines():
                line = line.rstrip('\n').split(' ')
                pointPos[pName].append(line)

    diceMsg = []
    with open('data/dicemsg.txt', encoding='utf-8') as file:
        for line in file.readlines():
            diceMsg.append(line.rstrip('\n'))

    evnData = []
    with open('data/events.txt', encoding="utf-8") as file:
        for line in file.readlines():
            evnData.append(line.rstrip('\n'))

    posmsgPos = []
    with open('pos/posmsg.txt', encoding="utf-8") as file:
        for line in file.readlines():
            posmsgPos.append(line.rstrip('\n'))

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

    def startgame():
        nonlocal playersQuantity
        nonlocal pNames
        nonlocal data

        while True:
            uiCtrl.message('dev', 'Введите количество игроков от 2 до 4.')
            playersQuantity = uiCtrl.readData('Игрок')

            try:
                playersQuantity = int(playersQuantity)
                if not (2 <= playersQuantity <= 4):
                    continue
            except ValueError:
                continue

            pNames = pNames[:playersQuantity]

            for pName in pNames:
                uiCtrl.hide(pName, False)
                uiCtrl.score.bs(pName, 0, 1000)
                data[pName]['bs'] = 1000
                data[pName]['status'] = 'В игре'
                uiCtrl.score.status(pName, 'Не в игре', 'В игре')
            break

    def propertySell(limit):
        nonlocal pNames
        nonlocal data
        nonlocal pName
        nonlocal costData
        nonlocal pointsData

        while data[pName]['bs'] < limit:
            if len(data[pName]['property']) == 0:
                uiCtrl.message('dev', f'{data[pName]["name"]}, на вашем счёте недостаточно средств. У вас отсутствует недвижимость для продажи - вы банкрот! Вы покидаете Академгородок!')
                pNames.remove(pName)

                pStatus = data[pName]['status']
                uiCtrl.score.status(pName, pStatus, 'Не в игре')
                uiCtrl.hide(pName, True)

                break
            else:
                uiCtrl.message('dev', f'{data[pName]["name"]}, на вашем счёте недостаточно средств. У вас есть недвижимость для продажи. Введите название объекта, который хотите продать!')
                prop = uiCtrl.readData(data[pName]['name'])

                while prop not in pointsData:
                    uiCtrl.message('dev', f'{data[pName]["name"]}, введите корректное название объекта.')
                    prop = uiCtrl.readData(data[pName]['name'])

                propPos = pointsData.index(prop)

                while propPos not in data[pName]['property']:
                    uiCtrl.message('dev', f'{data[pName]["name"]}, введите корректное название объекта.')
                    prop = uiCtrl.readData(data[pName]['name'])
                    propPos = pointsData.index(prop)

                data[pName]['property'].remove(propPos)
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + costData[propPos])

                data[pName]['bs'] += costData[propPos]
                uiCtrl.message('dev', f'{data[pName]["name"]}, вы успешно продали {prop} по цене {costData[propPos]}₽.')
                uiCtrl.score.property.remove(pName,
                                             pointsData[propPos])

    def eventHandler():
        nonlocal data
        nonlocal pName
        nonlocal pointPos
        nonlocal pName_

        event = random.randint(0, 9)

        decision = uiCtrl.readData(data[pName]['name'])

        while decision != 'y':
            uiCtrl.message('dev', 'Введите "y"')
            decision = uiCtrl.readData(data[pName]['name'])

            if event == 0:
                uiCtrl.message('dev', evnData[event])

                xPos = pointPos[pName][6][0]
                yPos = pointPos[pName][6][1]

                uiCtrl.move(pName, xPos, yPos)
                data[pName]['position'] = 6

                propertySell(195)
                if data[pName]['status'] != 'Не в игре':
                    uiCtrl.score.bs(pName,
                                    data[pName]['bs'],
                                    data[pName]['bs'] - 195)
                    data[pName]['bs'] = data[pName]['bs'] - 195

                    uiCtrl.score.status(pName, 'В игре', 'В НГУ')
                    data[pName]['countNSU'] = 2

            elif event == 1:
                uiCtrl.message('dev', evnData[event])

                xPos = pointPos[pName][23][0]
                yPos = pointPos[pName][23][1]

                uiCtrl.move(pName, xPos, yPos)
                data[pName]['position'] = 23

                used_flag = True
                mine_flag = False

                for pName_ in pNames:
                    if data[pName]['position'] in data[pName_]['property']:
                        if pName_ == pName:
                            mine_flag = True
                            continue
                        else:
                            used_flag = False
                            propertyPayment()
                            break

                if used_flag:
                    if mine_flag:
                        uiCtrl.message('dev', f'{data[pName]["name"]}, этот объект принадлежит вам!')
                    else:
                        propertyPurch()

            elif event == 2:
                uiCtrl.message('dev', evnData[event])

                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + 100)
                data[pName]['bs'] = data[pName]['bs'] + 100

                xPos = pointPos[pName][2][0]
                yPos = pointPos[pName][2][1]

                uiCtrl.move(pName, xPos, yPos)
                data[pName]['position'] = 2

                used_flag = True
                mine_flag = False

                for pName_ in pNames:
                    if data[pName]['position'] in data[pName_]['property']:
                        if pName_ == pName:
                            mine_flag = True
                            continue
                        else:
                            used_flag = False
                            propertyPayment()
                            break

                if used_flag:
                    if mine_flag:
                        uiCtrl.message('dev', f'{data[pName]["name"]}, этот объект принадлежит вам!')
                    else:
                        propertyPurch()

            elif event == 3:
                uiCtrl.message('dev', evnData[event])

                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + 50)
                data[pName]['bs'] = data[pName]['bs'] + 50

            elif event == 4:
                uiCtrl.message('dev', evnData[event])

                if data[pName]['position'] > 19:
                    uiCtrl.score.bs(pName,
                                    data[pName]['bs'],
                                    data[pName]['bs'] + 100)
                    data[pName]['bs'] = data[pName]['bs'] + 100

                uiCtrl.move(pName,
                            pointPos[pName][19][0],
                            pointPos[pName][19][1])
                data[pName]['position'] = 19

                used_flag = True
                mine_flag = False

                for pName_ in pNames:
                    if data[pName]['position'] in data[pName_]['property']:
                        if pName_ == pName:
                            mine_flag = True
                            continue
                        else:
                            used_flag = False
                            propertyPayment()
                            break

                if used_flag:
                    if mine_flag:
                        uiCtrl.message('dev', f'{data[pName]["name"]}, этот объект принадлежит вам!')
                    else:
                        propertyPurch()

            elif event == 5:
                uiCtrl.message('dev', evnData[event])

                if data[pName]['position'] > 15:
                    uiCtrl.score.bs(pName, data[pName]['bs'], data[pName]['bs'] + 100)
                    data[pName]['bs'] = data[pName]['bs'] + 100

                uiCtrl.move(pName,
                            pointPos[pName][15][0],
                            pointPos[pName][15][1])
                data[pName]['position'] = 15

                used_flag = True
                mine_flag = False

                for pName_ in pNames:
                    if data[pName]['position'] in data[pName_]['property']:
                        if pName_ == pName:
                            mine_flag = True
                            continue
                        else:
                            used_flag = False
                            propertyPayment()
                            break

                if used_flag:
                    if mine_flag:
                        uiCtrl.message('dev', f'{data[pName]["name"]}, этот объект принадлежит вам!')
                    else:
                        propertyPurch()

            elif event == 6:
                uiCtrl.message('dev', evnData[event])

                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + 100)
                data[pName]['bs'] = data[pName]['bs'] + 100

                uiCtrl.move(pName,
                            pointPos[pName][0][0],
                            pointPos[pName][0][1])
                data[pName]['position'] = 0

            elif event == 7:
                uiCtrl.message('dev', evnData[event])

                propertySell(70)
                if data[pName]['status'] != 'Не в игре':
                    uiCtrl.score.bs(pName,
                                    data[pName]['bs'],
                                    data[pName]['bs'] - 70)
                    data[pName]['bs'] = data[pName]['bs'] - 70

            elif event == 8:
                uiCtrl.message('dev', evnData[event])

                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + 50)
                data[pName]['bs'] = data[pName]['bs'] + 50

                xPos = pointPos[pName][4][0]
                yPos = pointPos[pName][4][1]

                uiCtrl.move(pName, xPos, yPos)
                data[pName]['position'] = 4

                used_flag = True
                mine_flag = False

                for pName_ in pNames:
                    if data[pName]['position'] in data[pName_]['property']:
                        if pName_ == pName:
                            mine_flag = True
                            continue
                        else:
                            used_flag = False
                            propertyPayment()
                            break

                if used_flag:
                    if mine_flag:
                        uiCtrl.message('dev', f'{data[pName]["name"]}, этот объект принадлежит вам!')
                    else:
                        propertyPurch()

            elif event == 9:
                uiCtrl.message('dev', evnData[event])
                propertySell(70)
                if data[pName]['status'] != 'Не в игре':
                    uiCtrl.score.bs(pName,
                                    data[pName]['bs'],
                                    data[pName]['bs'] - 70)
                    data[pName]['bs'] = data[pName]['bs'] - 70

    def propertyPurch():
        nonlocal data
        nonlocal pName
        nonlocal costData
        nonlocal pointsData

        uiCtrl.message('dev', 'Если хотите купить этот объект - введите "b". В противном случае "n"')
        decision = uiCtrl.readData(data[pName]['name'])

        while decision != 'b' and decision != 'n':
            uiCtrl.message('dev', 'Если хотите купить этот объект - введите "b". В противном случае "n"')
            decision = uiCtrl.readData(data[pName]['name']) 

        if decision == 'b':
            if data[pName]['bs'] >= costData[data[pName]['position']]:
                data[pName]['property'].append(data[pName]['position'])

                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                (data[pName]['bs'] -
                                 costData[data[pName]['position']]))

                data[pName]['bs'] -= costData[data[pName]['position']]
                uiCtrl.score.property.add(pName,
                                          pointsData[data[pName]['position']])

                uiCtrl.message('dev', 'Поздравляем с покупкой!')
            else:
                uiCtrl.message('dev', 'Недостаточно средств!')
        elif decision == 'n':
            pass

    def nsuAdmition():
        nonlocal data
        nonlocal pName
        nonlocal pointPos

        xPos = pointPos[pName][6][0]
        yPos = pointPos[pName][6][1]
        uiCtrl.move(pName, xPos, yPos)
        data[pName]['position'] = 6

        propertySell(195)
        if data[pName]['status'] != 'Не в игре':
            uiCtrl.score.bs(pName,
                            data[pName]['bs'],
                            data[pName]['bs'] - 195)
            data[pName]['bs'] = data[pName]['bs'] - 195

            uiCtrl.score.status(pName, 'В игре', 'В НГУ')
            data[pName]['status'] = 'В НГУ'
            data[pName]['countNSU'] = 2

    def moveMechanism():
        nonlocal data
        nonlocal pName
        nonlocal posmsgPos
        nonlocal diceMsg
        nonlocal pointPos

        countMoves = 0

        uiCtrl.message('dev', f'{data[pName]["name"]}, чтобы кинуть кубик - введите "k"')
        decision = uiCtrl.readData(data[pName]['name'])

        while decision != 'k':
            uiCtrl.message('dev', f'{data[pName]["name"]}, чтобы кинуть кубик - введите "k"')
            decision = uiCtrl.readData(data[pName]['name'])

        if decision == 'k':
            dice_number = random.randint(1, 6)
            uiCtrl.diceVal(dice_number)
            uiCtrl.message('dev', diceMsg[dice_number-1])

            playerPos = data[pName]['position']

            if playerPos + dice_number > 23:
                playerPos = dice_number - (24-playerPos)
                countMoves += 1
                xPos = pointPos[pName][playerPos][0]
                yPos = pointPos[pName][playerPos][1]

                uiCtrl.move(pName, xPos, yPos)
                if countMoves > 0:
                    uiCtrl.score.bs(pName,
                                    data[pName]['bs'],
                                    data[pName]['bs'] + 100)
                    data[pName]['bs'] += 100
                    uiCtrl.message('dev', 'Вы прошли круг, получите 100₽')
                    countMoves = 0

            else:
                playerPos += dice_number

                xPos = pointPos[pName][playerPos][0]
                yPos = pointPos[pName][playerPos][1]

                uiCtrl.move(pName, xPos, yPos)

            data[pName]['position'] = playerPos
            uiCtrl.message('dev', posmsgPos[data[pName]['position']])

    def propertyPayment():
        nonlocal streetsCombin
        nonlocal pName_
        nonlocal data
        nonlocal rentData
        nonlocal pName

        combin_flag = False

        for streetCombin in streetsCombin:
            if data[pName]['position'] in streetCombin:
                if set(streetCombin).issubset(set(data[pName_]['property'])):
                    combin_flag = True
                break

        if combin_flag:
            cost = 1
        else:
            cost = 0

        uiCtrl.message('dev', f'Этот объект пренадлежит игроку "{data[pName_]["name"]}". Заплатите ему {rentData[data[pName]["position"]][cost]}₽, для этого введите - "p"')
        decision = uiCtrl.readData(data[pName]['name'])

        while decision != 'p':
            uiCtrl.message('dev', f'Вы промазали по клавиатуре, введите - "p"')
            decision = uiCtrl.readData(data[pName]['name'])

        if decision == 'p':
            propertySell(rentData[data[pName]['position']][cost])
            if data[pName]['status'] != 'Не в игре':
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                (data[pName]['bs'] -
                                 rentData[data[pName]['position']][cost]))
                data[pName]['bs'] -= rentData[data[pName]['position']][cost]

                uiCtrl.score.bs(pName_,
                                data[pName_]['bs'],
                                (data[pName_]['bs'] +
                                 rentData[data[pName]['position']][cost]))
                data[pName_]['bs'] += rentData[data[pName]['position']][cost]

    def strokeLoss():
        nonlocal pName
        nonlocal data

        uiCtrl.message('dev', f"{data[pName]['name']} пропускает ход, так как он учится")
        data[pName]['countNSU'] -= 1

    startgame()
    while len(pNames) > 1:
        for pName in pNames:

            uiCtrl.message('separator', None)
            if data[pName]['countNSU'] <= 0:
                
                uiCtrl.score.status(pName, data[pName]['status'] , 'В игре')
                data[pName]['status'] = 'В игре'

                moveMechanism()
                if data[pName]['position'] in [9, 20]:
                    eventHandler()

                elif data[pName]['position'] in [0, 6, 12]:
                    pass

                elif data[pName]['position'] == 18:
                    nsuAdmition()

                else:
                    used_flag = True
                    mine_flag = False

                    for pName_ in pNames:
                        if (pName_ == pName and

                            (data[pName]['position'] in
                             data[pName_]['property'])):

                            mine_flag = True
                            continue

                        if data[pName]['position'] in data[pName_]['property']:
                            used_flag = False
                            propertyPayment()
                            break

                    if used_flag:
                        if mine_flag:
                            uiCtrl.message('dev', f'{data[pName]["name"]}, этот объект принадлежит вам!')
                            continue
                        else:
                            propertyPurch()

            else:
                strokeLoss()

    uiCtrl.message('dev', f'{pNames[0]}, поздравляем, ты победил, возьми с полки пирожок и возвращайся за новым! Андрей Геннадьевич, проверьте досрок, пожалуйста...')
    uiCtrl.endImg()


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
