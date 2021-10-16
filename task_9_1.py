"""
Создать класс TrafficLight (светофор):
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep


class TrafficLight:
    __color = {
        0: 'Красный',
        1: 'Желтый',
        2: 'Зеленый'
    }

    def running(self, *args):
        """Функция принимает три аргумента продолжительности времени в секундах"""
        for key, val in TrafficLight.__color.items():
            try:
                print(val)
                sleep(args[key])
            except IndexError as e:
                print(f'Ошибка {e}')


time = TrafficLight()
time.running(7, 2, 7)
# time.running(7, 2) #Выдаст ошибку
