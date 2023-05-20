'''
Powered by:
Popov Ivan (80%)
Fedyakin Dmitry (70%)
Fisher Daniil (75%)
'''

import threading
import sys
import random
import ru_local
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
        self.ui.console.append(ru_local.MSGCONSOLE(msg))

    # Reading data from chat.
    def buttonEnadle(self):
        self.ui.pushButton.setEnabled(True)

    def readValue(self):
        global chatData
        global CurrentPlayer

        self.ui.pushButton.setEnabled(False)

        player = CurrentPlayer

        self.ui.console.append(ru_local.READCONSOLE(player,
                                                    self.ui.inputLine.text()))
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

    # Class to manage score table.
    class score():

        # Class to manage properties of any player.
        class prop():
            def add(player, value):
                initValue = ru_local.INITPROPADD
                finalValue = ru_local.FINALPROPADD(value)

                if player == 'kapy':
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                elif player == 'dog':
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                elif player == 'gazmanov':
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                elif player == 'parrot':
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)

            def remove(player, value):
                initValue = ru_local.INITPROPREMOVE(value)
                finalValue = ''
                if player == 'kapy':
                    ui.kapyTextEditEvnt(ex, initValue, finalValue)

                elif player == 'dog':
                    ui.dogTextEditEvnt(ex, initValue, finalValue)

                elif player == 'gazmanov':
                    ui.gazmanovTextEditEvnt(ex, initValue, finalValue)

                elif player == 'parrot':
                    ui.parrotTextEditEvnt(ex, initValue, finalValue)

        # Function to edit balance of any player in score table.
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

        # Function to edit status of any player in score table.
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

    # Function to edit dice value in the window.
    def diceVal(value):
        ui.dice(ex, value)

    # Function to print messages and separators in console.
    def msg(type_, txt):
        if type_ == 'dev':
            txt = ru_local.DEVELOPERSMSG(txt)
        elif type_ == 'separator':
            txt = '<hr>'

        ui.printMessageEvnt(ex, txt)

    # Function to hide players from gaming field and from the score table.
    def hide(player, value):
        if player == 'kapy':
            ui.kapyEnable(ex, value)

        elif player == 'dog':
            ui.dogEnable(ex, value)

        elif player == 'gazmanov':
            ui.gazmanovEnable(ex, value)

        elif player == 'parrot':
            ui.parrotEnable(ex, value)

    # Function to hide endless message.
    def endImg():
        ui.endImgHide(ex)


def main():
    # Setting variables
    pNames = ['kapy', 'dog', 'gazmanov', 'parrot']

    data = {
        'kapy': {
            'name': f'{ru_local.KAPY}',
            'balance': 0,
            'status': f'{ru_local.LEFTGAME}',
            'pos': 0,
            'prop': [],
            'countNSU': 0
        },
        'dog': {
            'name': f'{ru_local.DOG}',
            'balance': 0,
            'status': f'{ru_local.LEFTGAME}',
            'pos': 0,
            'prop': [],
            'countNSU': 0
        },
        'gazmanov': {
            'name': f'{ru_local.GAZMANOV}',
            'balance': 0,
            'status': f'{ru_local.LEFTGAME}',
            'pos': 0,
            'prop': [],
            'countNSU': 0
        },
        'parrot': {
            'name': f'{ru_local.PARROT}',
            'balance': 0,
            'status': f'{ru_local.LEFTGAME}',
            'pos': 0,
            'prop': [],
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

    # Reading data from files
    for pName in pNames:
        with open(f'data/pos/{pName}.txt') as file:
            for line in file.readlines():
                line = line.rstrip('\n').split(' ')
                pointPos[pName].append(line)

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

    # Function to find out the numbers of players.
    def startgame():
        nonlocal playersQuantity
        nonlocal pNames
        nonlocal data

        # Cycle to read quantity of players
        while True:
            playersQuantity = uiCtrl.readData(ru_local.PLAYER)

            try:
                playersQuantity = int(playersQuantity)
                if not (2 <= playersQuantity <= 4):
                    uiCtrl.msg('dev', ru_local.PLAYER_NUM)
                    continue
            except ValueError:
                uiCtrl.msg('dev', ru_local.PLAYER_NUM)
                continue

            pNames = pNames[:playersQuantity]

            # Unhiding players and score tables
            for pName in pNames:
                uiCtrl.hide(pName, False)
                uiCtrl.score.bs(pName, 0, 1000)
                data[pName]['bs'] = 1000
                data[pName]['status'] = ru_local.INGAME
                uiCtrl.score.status(pName, ru_local.LEFTGAME, ru_local.INGAME)
            break

    # Function to sell properties if the balance is not in setted limit.
    def propSell(limit):
        nonlocal pNames
        nonlocal data
        nonlocal pName
        nonlocal costData

        while data[pName]['bs'] < limit:

            # Cheking for player bankrupting
            if len(data[pName]['prop']) == 0:
                uiCtrl.msg('dev', ru_local.BANKRUPT(data[pName]['name']))
                pNames.remove(pName)

                pStatus = data[pName]['status']
                uiCtrl.score.status(pName, pStatus, ru_local.LEFTGAME)
                uiCtrl.hide(pName, True)

                break

            else:
                # Reading properties to sell.
                uiCtrl.msg('dev', ru_local.PROPSELL(data[pName]['name']))
                prop = uiCtrl.readData(data[pName]['name'])

                # Checking property existence
                while prop not in ru_local.points:
                    uiCtrl.msg('dev',
                               ru_local.CORRECTPROP(data[pName]['name']))
                    prop = uiCtrl.readData(data[pName]['name'])

                propPos = ru_local.points.index(prop)

                # Checking property availability
                while propPos not in data[pName]['prop']:
                    uiCtrl.msg('dev',
                               ru_local.CORRECTPROP(data[pName]['name']))
                    prop = uiCtrl.readData(data[pName]['name'])
                    propPos = ru_local.points.index(prop)

                # Removing property from 'data', score table
                data[pName]['prop'].remove(propPos)
                uiCtrl.score.prop.remove(pName,
                                         (ru_local.points[propPos] +
                                          ru_local.rentScore[propPos]))

                # Changing balance
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + costData[propPos])

                data[pName]['bs'] += costData[propPos]

                # Success message
                uiCtrl.msg('dev', ru_local.SUCCESSSELL(data[pName]['name'],
                                                       prop,
                                                       costData[propPos]))

    # Handling events when the "Chance" points is attacked.
    def eventHandler():
        nonlocal data
        nonlocal pName
        nonlocal pointPos
        nonlocal pName_

        event = random.randint(0, 9)

        decision = uiCtrl.readData(data[pName]['name'])

        while decision != 'y':
            uiCtrl.msg('dev', ru_local.Y)
            decision = uiCtrl.readData(data[pName]['name'])

        if event == 0:
            uiCtrl.msg('dev', ru_local.evnData[event])

            uiCtrl.move(pName,
                        pointPos[pName][6][0],
                        pointPos[pName][6][1])
            data[pName]['pos'] = 6

            propSell(195)
            if data[pName]['status'] != ru_local.LEFTGAME:
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] - 195)
                data[pName]['bs'] = data[pName]['bs'] - 195

                uiCtrl.score.status(pName, ru_local.INGAME, ru_local.INNSU)
                data[pName]['countNSU'] = 2

        elif event == 1:
            uiCtrl.msg('dev', ru_local.evnData[event])

            uiCtrl.move(pName,
                        pointPos[pName][23][0],
                        pointPos[pName][23][1])
            data[pName]['pos'] = 23

            used_flag = True
            mine_flag = False

            for pName_ in pNames:
                if data[pName]['pos'] in data[pName_]['prop']:
                    if pName_ == pName:
                        mine_flag = True
                        continue
                    else:
                        used_flag = False
                        propPayment()
                        break

            if used_flag:
                if mine_flag:
                    uiCtrl.msg('dev',
                               ru_local.YOURSPROP(data[pName]["name"]))
                else:
                    propPurch()

        elif event == 2:
            uiCtrl.msg('dev', ru_local.evnData[event])

            uiCtrl.score.bs(pName,
                            data[pName]['bs'],
                            data[pName]['bs'] + 100)
            data[pName]['bs'] = data[pName]['bs'] + 100

            uiCtrl.move(pName,
                        pointPos[pName][2][0],
                        pointPos[pName][2][1])
            data[pName]['pos'] = 2

            used_flag = True
            mine_flag = False

            for pName_ in pNames:
                if data[pName]['pos'] in data[pName_]['prop']:
                    if pName_ == pName:
                        mine_flag = True
                        continue
                    else:
                        used_flag = False
                        propPayment()
                        break

            if used_flag:
                if mine_flag:
                    uiCtrl.msg('dev',
                               ru_local.YOURSPROP(data[pName]["name"]))
                else:
                    propPurch()

        elif event == 3:
            uiCtrl.msg('dev', ru_local.evnData[event])

            uiCtrl.score.bs(pName,
                            data[pName]['bs'],
                            data[pName]['bs'] + 50)
            data[pName]['bs'] = data[pName]['bs'] + 50

        elif event == 4:
            uiCtrl.msg('dev', ru_local.evnData[event])

            if data[pName]['pos'] > 19:
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + 100)
                data[pName]['bs'] = data[pName]['bs'] + 100

            uiCtrl.move(pName,
                        pointPos[pName][19][0],
                        pointPos[pName][19][1])
            data[pName]['pos'] = 19

            used_flag = True
            mine_flag = False

            for pName_ in pNames:
                if data[pName]['pos'] in data[pName_]['prop']:
                    if pName_ == pName:
                        mine_flag = True
                        continue
                    else:
                        used_flag = False
                        propPayment()
                        break

            if used_flag:
                if mine_flag:
                    uiCtrl.msg('dev',
                               ru_local.YOURSPROP(data[pName]["name"]))
                else:
                    propPurch()

        elif event == 5:
            uiCtrl.msg('dev', ru_local.evnData[event])

            if data[pName]['pos'] > 15:
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] + 100)
                data[pName]['bs'] = data[pName]['bs'] + 100

            uiCtrl.move(pName,
                        pointPos[pName][15][0],
                        pointPos[pName][15][1])
            data[pName]['pos'] = 15

            used_flag = True
            mine_flag = False

            for pName_ in pNames:
                if data[pName]['pos'] in data[pName_]['prop']:
                    if pName_ == pName:
                        mine_flag = True
                        continue
                    else:
                        used_flag = False
                        propPayment()
                        break

            if used_flag:
                if mine_flag:
                    uiCtrl.msg('dev',
                               ru_local.YOURSPROP(data[pName]["name"]))
                else:
                    propPurch()

        elif event == 6:
            uiCtrl.msg('dev', ru_local.evnData[event])

            uiCtrl.score.bs(pName,
                            data[pName]['bs'],
                            data[pName]['bs'] + 100)
            data[pName]['bs'] = data[pName]['bs'] + 100

            uiCtrl.move(pName,
                        pointPos[pName][0][0],
                        pointPos[pName][0][1])
            data[pName]['pos'] = 0

        elif event == 7:
            uiCtrl.msg('dev', ru_local.evnData[event])

            propSell(70)
            if data[pName]['status'] != ru_local.LEFTGAME:
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] - 70)
                data[pName]['bs'] = data[pName]['bs'] - 70

        elif event == 8:
            uiCtrl.msg('dev', ru_local.evnData[event])

            uiCtrl.score.bs(pName,
                            data[pName]['bs'],
                            data[pName]['bs'] + 50)
            data[pName]['bs'] = data[pName]['bs'] + 50

            uiCtrl.move(pName,
                        pointPos[pName][4][0],
                        pointPos[pName][4][1])
            data[pName]['pos'] = 4

            used_flag = True
            mine_flag = False

            for pName_ in pNames:
                if data[pName]['pos'] in data[pName_]['prop']:
                    if pName_ == pName:
                        mine_flag = True
                        continue
                    else:
                        used_flag = False
                        propPayment()
                        break

            if used_flag:
                if mine_flag:
                    uiCtrl.msg('dev',
                               ru_local.YOURSPROP(data[pName]["name"]))
                else:
                    propPurch()

        elif event == 9:
            uiCtrl.msg('dev', ru_local.evnData[event])
            propSell(70)
            if data[pName]['status'] != ru_local.LEFTGAME:
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                data[pName]['bs'] - 70)
                data[pName]['bs'] = data[pName]['bs'] - 70

    # Function of purchase property
    def propPurch():
        nonlocal data
        nonlocal pName
        nonlocal costData

        # Reading player decision
        uiCtrl.msg('dev', ru_local.PROPPURCH)
        decision = uiCtrl.readData(data[pName]['name'])

        while decision != 'b' and decision != 'n':
            uiCtrl.msg('dev', ru_local.PROPPURCH)
            decision = uiCtrl.readData(data[pName]['name'])

        # Positive decision
        if decision == 'b':

            # If the balance is sufficient
            if data[pName]['bs'] >= costData[data[pName]['pos']]:
                data[pName]['prop'].append(data[pName]['pos'])

                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                (data[pName]['bs'] -
                                 costData[data[pName]['pos']]))

                data[pName]['bs'] -= costData[data[pName]['pos']]
                uiCtrl.score.prop.add(pName,
                                      (ru_local.points[data[pName]['pos']]) +
                                      ru_local.rentScore[data[pName]['pos']])

                uiCtrl.msg('dev', ru_local.CONGRATULATION)

            # Refusal
            else:
                uiCtrl.msg('dev', ru_local.NOMONEY)

        # Skip
        elif decision == 'n':
            pass

    # Function of player admissing to NSU
    def nsuAdmition():
        nonlocal data
        nonlocal pName
        nonlocal pointPos

        # Mooving to NSU point
        uiCtrl.move(pName,
                    pointPos[pName][6][0],
                    pointPos[pName][6][1])
        data[pName]['pos'] = 6

        # Cheking for sufficient, changing balance
        propSell(195)
        if data[pName]['status'] != ru_local.LEFTGAME:
            uiCtrl.score.bs(pName,
                            data[pName]['bs'],
                            data[pName]['bs'] - 195)
            data[pName]['bs'] = data[pName]['bs'] - 195

            # Change status.
            uiCtrl.score.status(pName,  ru_local.INGAME,  ru_local.INNSU)
            data[pName]['status'] = ru_local.INNSU

            # Starting counting two semesters of study.
            data[pName]['countNSU'] = 2

    # Function of mooving.
    def moveMechanism():
        nonlocal data
        nonlocal pName
        nonlocal pointPos

        countMoves = 0

        decision = None

        # Reading decision.
        while decision != 'k':
            uiCtrl.msg('dev', ru_local.DICEDROP(data[pName]["name"]))
            decision = uiCtrl.readData(data[pName]['name'])

        if decision == 'k':
            # Roll of the dice.
            dice_number = random.randint(1, 6)
            uiCtrl.diceVal(dice_number)
            uiCtrl.msg('dev', ru_local.diceMsg[dice_number-1])

            playerPos = data[pName]['pos']

            # Mooving action figure.
            # If a player passes the starting field, he gets currency.
            if playerPos + dice_number > 23:
                playerPos = dice_number - (24-playerPos)
                countMoves += 1

                uiCtrl.move(pName,
                            pointPos[pName][playerPos][0],
                            pointPos[pName][playerPos][1])

                if countMoves > 0:
                    uiCtrl.score.bs(pName,
                                    data[pName]['bs'],
                                    data[pName]['bs'] + 100)
                    data[pName]['bs'] += 100
                    uiCtrl.msg('dev', ru_local.CIRCLE)
                    countMoves = 0

            else:
                playerPos += dice_number

                uiCtrl.move(pName,
                            pointPos[pName][playerPos][0],
                            pointPos[pName][playerPos][1])

            data[pName]['pos'] = playerPos
            uiCtrl.msg('dev', ru_local.posMsg[data[pName]['pos']])

    # Function of rent payment.
    def propPayment():
        nonlocal streetsCombin
        nonlocal pName_
        nonlocal data
        nonlocal rentData
        nonlocal pName

        comb = 0

        # Checking for street combinations.
        for streetCombin in streetsCombin:
            if data[pName]['pos'] in streetCombin:
                if set(streetCombin).issubset(set(data[pName_]['prop'])):
                    comb = 1
                break

        # Reading decision.
        uiCtrl.msg('dev',
                   ru_local.PAYMENT(data[pName_]["name"],
                                    rentData[data[pName]["pos"]][comb]))
        decision = uiCtrl.readData(data[pName]['name'])

        # Confirming the action.
        while decision != 'p':
            uiCtrl.msg('dev', ru_local.FAILURE)
            decision = uiCtrl.readData(data[pName]['name'])

        # Transferring money from one balance to another.
        if decision == 'p':
            propSell(rentData[data[pName]['pos']][comb])
            if data[pName]['status'] != ru_local.LEFTGAME:
                uiCtrl.score.bs(pName,
                                data[pName]['bs'],
                                (data[pName]['bs'] -
                                 rentData[data[pName]['pos']][comb]))
                data[pName]['bs'] -= rentData[data[pName]['pos']][comb]

                uiCtrl.score.bs(pName_,
                                data[pName_]['bs'],
                                (data[pName_]['bs'] +
                                 rentData[data[pName]['pos']][comb]))
                data[pName_]['bs'] += rentData[data[pName]['pos']][comb]

    # If player is in NSU - loss stroke.
    def strokeLoss():
        nonlocal pName
        nonlocal data

        uiCtrl.msg('dev', ru_local.GRADUATUING(data[pName]['name']))
        data[pName]['countNSU'] -= 1

    # Main cycle
    startgame()

    while len(pNames) > 1:
        for pName in pNames:

            uiCtrl.msg('separator', None)

            # Cheking for studing
            if data[pName]['countNSU'] <= 0:
                uiCtrl.score.status(pName,
                                    data[pName]['status'],
                                    ru_local.INGAME)
                data[pName]['status'] = ru_local.INGAME

                # Mooving
                moveMechanism()
                if data[pName]['pos'] in [9, 20]:
                    eventHandler()

                elif data[pName]['pos'] in [0, 6, 12]:
                    pass

                elif data[pName]['pos'] == 18:
                    nsuAdmition()

                else:
                    used_flag = True
                    mine_flag = False

                    # Checking property eligibility
                    for pName_ in pNames:
                        if (pName_ == pName and

                            (data[pName]['pos'] in
                             data[pName_]['prop'])):

                            mine_flag = True
                            continue

                        if data[pName]['pos'] in data[pName_]['prop']:
                            used_flag = False
                            propPayment()
                            break

                    if used_flag:
                        if mine_flag:
                            uiCtrl.msg('dev',
                                       ru_local.YOURSPROP(data[pName]["name"]))
                            continue
                        else:
                            propPurch()

            else:
                strokeLoss()

    # Finally...
    uiCtrl.endImg()
    uiCtrl.msg('dev', ru_local.FINALLY(data[pNames[0]]['name']))


def start():
    global ex
    global dataReadyEvent

    app = QApplication(sys.argv)
    ex = ui()

    # Separation UI and backend by threads.
    dataReadyEvent = threading.Event()
    trd = threading.Thread(target=main)
    trd.start()

    app.exec_()


if __name__ == '__main__':
    start()
