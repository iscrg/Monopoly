INITPROPADD = '</p></body></html>'

KAPY = 'Капибара'
DOG = 'Опухший пес'
GAZMANOV = 'Олег Газманов'
PARROT = 'Попуг'

PLAYER_NUM = 'Введите количество игроков от 2 до 4.'
PLAYER = 'Игрок'
Y = "'Введите 'y'"

INGAME = 'В игре'
LEFTGAME = 'Не в игре'
INNSU = 'В НГУ'

PROPPURCH = 'Если хотите купить этот объект - введите "b". В противном случае "n"'
CONGRATULATION = 'Поздравляем с покупкой!'
NOMONEY = 'Недостаточно денег!'
CIRCLE = 'Вы прошли круг, получите 100₽'
FAILURE = "Вы промазали по клавиатуре, введите - 'p'"

posMsg = ['Гимназия, мы все нашли друзеееей... Вы попали в Гимназию №3. Получите 100₽.',
          'Вы попали на улицу Ученых. Остерегайтесь мажориков из стотридцатки. [45₽ | 90₽]',
          'Вы попали на Ж/Д станцию "Бердск". Чаще оглядывайтесь по сторонам! [150₽ | 300₽]',
          'Вы попали на Жемчужную улицу. Никому не известно, почему остановка на ней называется "Цветной проезд". [50₽ | 100₽]',
          'Вы попали в БУНКЕР. Не забудьте потанцевать на шесте и подружиться с барменом, а также выяснить, что вчера было. [120₽ | 360₽]',
          'Вы попали на улицу Демакова. Опасайтесь сумасшедшего на белой Мазде 3! [90₽ | 180₽]',
          'Вы попали в НГУ. Как любой уважающий себя студент, сфотографируйтесь возле логотипа ЭФ.',
          'Вы попали на улицу Кутателадзе. Будьте бдительны, на ней находится ТРК Эдем, в котором голодные школьники жадно раздирают айтвистер на шестерых. [100₽ | 200₽]',
          'Вы попали на улицу Ильича. Не забудьте купить книжку у местного кришнаита. [110₽ | 220₽]',
          'Шанс! Чтобы вытянуть карточку - введите "y".',
          'Вы попали на улицу Терешковой. Вытащите погулять одного из разработчиков. [130₽ | 260₽]',
          'Вы попали на Ж/Д станцию "Сеятель". Там можно посетить железнодорожный музей - любимое место одного из разработчиков. [150₽ | 300₽]',
          'Вы попали на парковку ЭФ. Найти тут свободное место после второй пары - та еще задачка...',
          'Вы попали на Детский проезд. Даже для разработчиков загадка, почему он находится на противоположном конце карты от Гимназии №3. [140₽ | 280₽]',
          'Вы попали на улицу Правды. Теперь вы знаете, что значит действительно нечищеная дорога. [150₽ | 300₽]',
          'Вы попали в торговый центр. Не забудьте покормить голубей возле фонтана, а так же остерегайтесь тараканов из "Вилки-Ложки" [120₽ | 360₽]',
          'Вы попали на Весенний проезд. Большое количество студентов мечтают снять тут квартиру, но далеко не многим это удается... [170₽ | 340₽]',
          'Вы попали на улицу Пирогова. Остерегайтесь любого, кто будет кричать "ГЭ-ГЭ-ЭФ", эти существа непредсказуемы... [180₽ | 360₽]',
          'Поступайте в НГУ и проучитесь там 2 хода. Но помните: далеко не все доживают до конца...',
          'Вы попали на проспект Лаврентьева, здесь люди становятся умнее... [190₽ | 380₽]',
          'Шанс! Чтобы вытянуть карточку - введите "y".', 
          'Вы попали на Морской проспект. Тут вообще есть хоть что-нибудь кроме кофеен и аптек? [240₽ | 480₽]',
          'Нету в мире лучше дома, чем общага Эконома! Вы попали в общежитие №4. [120₽ | 360₽]',
          'Вы попали на проспект Коптюга. Тут даже собачьи отходы жизнедеятельности деньгами пахнут... [290₽ | 580₽]']

diceMsg = ['Ритмические танцы чисел показали 1.',
           'Магия кубиков! Выпало число 2.',
           'Чудеса теории вероятности! Наталья Исааковна сказала 3.',
           'Бросок вдохновения! Кости показали 4.',
           'Летящие числа летели-летели, да прилетели на число 5.',
           'Жребий фортуны показал 6.']

evnData = ['Вы поступаете в НГУ. Заплатите 195₽ и отучитесь там 2 хода.',
           'Отправляйтесь на проспект Коптюга.',
           'Отправляйтесь на Ж/Д станцию Бердск. Бог вам в помощь. Если вы проходите поле "Старт", получите 100₽.',
           'Вам пришла стипендия. Получите 50₽.',
           'Отправляйтесь на проспект Лаврентьева. Если вы проходите поле "Старт", получите 100₽.',
           'Отправляйтесь в торговый центр. Не забудьте поболтать с бабушкой с балалайкой. Если вы проходите поле "Старт", получите 100₽.',
           'Отправляйтесь на поле "Старт", получите 100₽.',
           'Вы неправильно перешли дорогу возле "Ярче!". Заплатите штраф 70₽.',
           'Отправляйтесь в "Бункер". Заплатите 50₽ рублей за вход. Если вы проходите поле "Старт", получите 100₽.',
           'Вы попали на капустник Максимина. Заплатите 70₽ и приходите еще :)']

points = ['Старт',
          'ул. Ученых',
          'Ж/Д станция Бердск',
          'ул. Жемчужная',
          'БУНКЕР',
          'ул. Демакова',
          'НГУ',
          'ул. Кутателадзе',
          'ул. Ильича',
          'Шанс',
          'ул. Терешковой',
          'Ж/Д станция Сеятель',
          'Парковка ЭФ',
          'Десткий проезд',
          'ул. Правды',
          'Торговый центр',
          'Весенний проезд',
          'ул. Пирогова',
          'Поступайте в НГУ',
          'проспект Лаврентьева',
          'Шанс',
          'Морской проспект',
          'Общежитие №4',
          'проспект Коптюга']

rentScore = [' [0 0]',
                ' [45₽ | 90₽]',
                ' [150₽ | 300₽]',
                ' [50₽ | 100₽]',
                ' [120₽ | 360₽]',
                ' [90₽ | 180₽]',
                ' [0₽ | 0₽]',
                ' [100₽ | 200₽]',
                ' [110₽ | 220₽]',
                ' [0₽ | 0₽]',
                ' [130₽ | 260₽]',
                ' [150₽ | 300₽]',
                ' [0₽ | 0₽]',
                ' [140₽ | 280₽]',
                ' [150₽ | 300₽]',
                ' [120₽ | 360₽]',
                ' [170₽ | 340₽]',
                ' [180₽ | 360₽]',
                ' [0₽ | 0₽]',
                ' [190₽ | 380₽]',
                ' [0₽ | 0₽]',
                ' [240₽ | 480₽]',
                ' [120₽ | 360₽]',
                ' [290₽ | 580₽]'
                ]


def DROPDICE(pName):
    txt = f'{pName}, чтобы кинуть кубик - введите "k"'
    return txt


def OWNERSHIP(pName, valueMoney):
    txt = f'Этот объект пренадлежит игроку "{pName}". Заплатите ему {valueMoney}₽, для этого введите - "p"'
    return txt


def SKIPMOVE(pName):
    txt = f"{pName} пропускает ход, так как он учится"
    return txt


def YOURSPROP(pName):
    txt = f'{pName}, этот объект принадлежит вам!'
    return txt


def MSGCONSOLE(msg):
    txt = f'<span style=" font-size:12pt;">{msg}</span></body></html>'
    return txt


def READCONSOLE(pName, msg):
    txt = f'<span style="font-weight:600;font-size:12pt;">[{pName}]</span> <span style="font-size:12pt;">{msg}</span>'
    return txt


def FINALPROPADD(value):
    txt = f'<br /><span style="font-size:10pt;">{value}</span></p></body></html>'
    return txt


def INITPROPREMOVE(value):
    txt = f'<br /><span style=" font-size:10pt;">{value}</span>'
    return txt


def DEVELOPERSMSG(msg):
    txt = f'<span style="font-weight:600;font-size:12pt;">[Сказочные разработчики]</span> <span style="font-size:12pt;">{msg}</span>'
    return txt


def BANKRUPT(pName):
    txt = f'{pName}, на вашем счёте недостаточно средств. У вас отсутствует недвижимость для продажи - вы банкрот! Вы покидаете Академгородок!'
    return txt


def PROPSELL(pName):
    txt = f'{pName}, на вашем счёте недостаточно средств. У вас есть недвижимость для продажи. Введите название объекта, который хотите продать!'
    return txt


def CORRECTPROP(pName):
    txt = f'{pName}, введите корректное название объекта.'
    return txt


def SUCCESSSELL(pName, prop, cost):
    txt = f'{pName}, вы успешно продали {prop} по цене {cost}₽.'
    return txt


def DICEDROP(pName):
    txt = f'{pName}, чтобы кинуть кубик - введите "k"'
    return txt


def PAYMENT(pName, rentData):
    txt = f'Этот объект пренадлежит игроку "{pName}". Заплатите ему {rentData}₽, для этого введите - "p"'
    return txt


def GRADUATUING(pName):
    txt = f"{pName} пропускает ход, так как он учится"
    return txt


def FINALLY(pName):
    txt = f'{pName}, поздравляем, ты победил, возьми с полки пирожок и возвращайся за новым! Андрей Геннадьевич, проверьте досрок, пожалуйста :)'
    return txt


if __name__ == '__main__':
    DROPDICE()
    OWNERSHIP()
    SKIPMOVE()
    YOURSPROP()
    MSGCONSOLE()
    READCONSOLE()
    FINALPROPADD()
    DEVELOPERSMSG()
    BANKRUPT()
    PROPSELL()
    CORRECTPROP()
    SUCCESSSELL()
    DICEDROP()
    PAYMENT()
    GRADUATUING()
    FINALLY()
