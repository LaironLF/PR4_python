from datetime import datetime
from multiprocessing import Process, Queue
from typing import List

#| Процесс возведения в степень:
def powerNumb(inp_mas :Queue):
    while True:                                             # Создаём бесконечный цикл
        if(not inp_mas.empty()):                            # Проверяем очередь, если не пустая, то круто
            numbers :List[int] = inp_mas.get()              # достаём цифры из очереди
            result = int(numbers[0]) ** int(numbers[1])     # перемножаем эти циферки
            
            num_sum : int = 0                               # создаём переменную суммы
            for i in range(result):                         # хз зачем это нужно,
                num_sum+=i                                  # но мы суммируем число от 0, до числа результата
            
            
            with open('./files/log.txt', 'a+') as file:     # Открываем соединение
                current_time = datetime.now()               # Сохраняем дату записи
                file.write(f'{current_time.date()} {current_time.hour}:{current_time.minute}:{current_time.second} >>> {numbers[0]}^{numbers[1]}={result}\n') #записываем


if __name__ == "__main__":
    
    inp_mas = Queue()                                                           # Очередь :)
    
    read_process = Process(target=powerNumb, args=(inp_mas,), daemon=True)      # Создаём процесс, отдаём очередь в качестве аргументов
    read_process.start()                                                        # Запускаем процесс, урааааа
    while True:                                                                 
        inp = input('Введите число и степень: ')                                # но тут всё понятно.
        inp = inp.split()
        inp_mas.put(inp)
        
        
            
