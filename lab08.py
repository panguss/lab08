import random
import logging

logging.basicConfig(filename='py.log', level=logging.INFO)

while True:
    try:
        a = int(input("Введите число бочонков: "))
        assert a > 0
    except AssertionError:
        print("Число должно быть больше нуля\n Попробуйте еще раз")
        logging.warning("not correct number")
    except ValueError:
        print('Необходимо ввести положительное число \n Попробуйте еще раз')
        logging.exception('not correct input')
    else:
        logging.info('correct number')
        break
list = [i for i in range(1, a + 1)]
random.shuffle(list)
print('Чтобы вывести число, необходимо нажать Enter', end='')
for e in list:
    v = input()
    print(e, end='')
