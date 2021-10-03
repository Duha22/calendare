import calendar
import datetime
ch = ['Данилов Андрей',
      'Чипсанова Соня',
      'Потапова Таня',
      'Сухарев Кирилл',
      'Сухарев Никита',
      'Булышева Настя',
      'Терещенко Юра',
      'Быков Максим',
      'Федоченко Егор']

if __name__ == '__main__':
    ch.sort()
    c = calendar.Calendar(firstweekday=4)
    chech = 0
    today = str(datetime.date.today())
    for item in c.itermonthdates(2021, 10):
        data = str(item)
        y, m, d = data.split('-')
        # if calendar.weekday(int(y), int(m), int(d)) not in [6, 5]:
        if chech > len(ch)-1: chech=0
        date = '{}-{}-{}'.format(d, m, y)
        if data == today:
            print('\033[32m {}-{}-{}: {}'.format(d, m, y, ch[chech]))
        else: print('\033[37m {}-{}-{}: {}'.format(d, m, y, ch[chech]))
        chech += 1