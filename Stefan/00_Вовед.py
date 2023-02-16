"""
Добредојдовте,
Ова е воведната пајтон скрипта по предметот Машинско учење.

"""
import math
from time import sleep


# ова е коментар

# ова е променлива
welcome_message = 'Добредојдовте'
# која ја печатиме на стандарден излез
print(welcome_message)

# променливите можат да заземаат повеќе различни податоци
# ова е int
number = 123
print(type(number))
# а ова е float
number = 123.0
print(type(number))
# всуштност ова се броеви, не берете гајле за типот на променлива, вие само доделувајте вредности

# ова е string
word_1 = 'Здраво'
word_2 = "свету"
print(word_1 + ' ' + word_2 + "!")

# еве пример за поинтуитивно доделување вредности на променливи во пајтон светот
minutes, seconds = 25, 12
# вака се користи преформатирано печатење
print('Остануваат уште {} минути и {} секунди.'.format(minutes, seconds))
# а може и вака
print('Остануваат уште ', minutes, ' минути и ', seconds, ' секунди.')

# ова е празна листа
starks = []
print(starks)
# а ова пополнета однапред
starks = ['Eddard', 'Catelyn', 'Robb', 'Sansa', 'Arya', 'Bran', 'Rickon']
print(starks)

# до елементите на листата пристапуваме со индекс
"""
['Eddard', 'Catelyn', 'Robb', 'Sansa', 'Arya', 'Bran', 'Rickon']
_____0_________1_________2_______3________4_______5________6____
____-7________-6________-5______-4_______-3______-2_______-1____

"""
print('индекс 0 - ', starks[0])
print('индекс 5 - ', starks[5])
print('индекс -1 - ', starks[-1])
print('индекс -7 - ', starks[-7])
print('индекс 2 до 6 - ', starks[2:6])
# замислено грешно
print('индекс -2 до -6 - ', starks[-2:-6])
print('индекс -5 до -1 - ', starks[-5:-1])

# може да додаваме вредности во листа
starks.append('John')
print(starks)
# може и да вадиме од листа
starks.remove('Eddard')
starks.remove('Catelyn')
starks.remove('Robb')
starks.remove('Rickon')
print(starks)

# овоа е помеѓу 5_та и 6_та сезона :D
starks.remove('John')
starks.append('John')
print(starks)

# внимавајте на индентација (поместување на наредбите од јамка/гранење надесно (за 4 празни места) заради припадност)
# ова ви е for јамка
for index in range(7):
    print(index, end=' ')
print()

for index in range(3, 19, 2):
    print(index, end=' ')
print()

# немојте вака
for index in range(len(starks)):
    print(starks[index], end=' ')
print()

# вака е добро
for stark in starks:
    print(stark, end=' ')
print()

# а ако ви треба и индекс, ќе постапите вака
for index, stark in enumerate(starks):
    print(index, stark, ' ', end=' ')
print()

# ова е if гранење со in операторот
if 'Bran' in starks:
    print('Bran е веќе во семејството')
else:
    starks.append('Bran')
    print('Само што го додадов Bran во семејството')


def sum_two(arg1, arg2):
    return arg1 + arg2


print(sum_two(3, 4))
print(sum_two('3', '4'))


def my_function(arg1, arg2, arg3=45, arg4=.2, arg5='Abc'):
    print(arg1, arg2, arg3, arg4, arg5)


my_function(2, 3, arg5='abc')

for index in range(3):
    print(index)
    sleep(3)


# ова е речник, структура од соодветни парови на клуч и вредност
colors = {
   "Red": (1, 0, 0),
   "Green": (0, 1, 0),
   "Blue": (0, 0, 1),
   "Black": (0, 0, 0),
   "White": (1, 1, 1)
}
print(colors['Blue'])

# читаме од датотека
text = open('data/Colors.txt').read().strip()
print(text)
print()
# делиме на редови
lines = text.split('\n')
print('{} редови'.format(len(lines)), lines)
print()

# ги сместуваме во речник
# ова е празен речник
colors = {}
for line in lines:
    key, value = line.split(':')
    colors[key] = value.strip().split()

print(colors)


class OneWheelRobot:
    def __init__(self, heading, start_x, start_y):
        self.heading = heading
        self.x = start_x
        self.y = start_y

    def set_heading(self, new_heading):
        self.heading = new_heading

    def move(self, step):
        self.x += step * math.cos(self.heading)
        self.y += step * math.sin(self.heading)

    def __str__(self):
        return 'Роботот се наоѓа на координати ({}, {}) под агол {}'.format(self.x, self.y, self.heading)


robot = OneWheelRobot(math.pi, 3, 5)
print(robot)
print()
