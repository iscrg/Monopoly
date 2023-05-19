KAPY = 'Капибара'
DOG = 'Опухший пес'
GAZMANOV = 'Олег Газманов'
PARROT = 'Попуг'

INGAME = 'В игре'
LEFTGAME = 'Не в игре'
INNSU = 'В НГУ'

PROPPURCH = 'Если хотите купить этот объект - введите "y". В противном случае "n"'
CONGRATULATION = 'Поздравляем с покупкой!'
NOMONEY = 'Недостаточно денег!'

def DROPDICE(playerName):
    msg = f'{playerName}, чтобы кинуть кубик - введите "y"'
    return msg

def OWNERSHIP(playerName, valueMoney):
    msg = f'Этот объект пренадлежит игроку "{playerName}". Заплатите ему {valueMoney}₽, для этого введите - "p"'
    return msg

def SKIPMOVE(playerName):
    msg = f"{playerName} пропускает ход, так как он учится"
    return msg

if __name__ == '__main__':
    DROPDICE()
    OWNERSHIP()
    SKIPMOVE()