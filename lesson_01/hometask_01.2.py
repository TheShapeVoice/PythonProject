# task 2
time = int(input("Введите время в секундах: "))
hour = time // 3600
minute = time % 3600 // 60
sec = time % 60
time_finish = f"{hour:02d}:{minute:02d}:{sec:02d}"
print("Результат конвертации времени: ", time_finish)


# Вопрос. Нашел вот такой способ перевода, но не понимаю, почему результаты отличаются
# import time
# n = 200000
# time_format = time.strftime("%H:%M:%S", time.gmtime(n))
# print("Time in preferred format : ",time_format)