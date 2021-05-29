# Tickets randomizer
## _ДЗ №4 - Симметричные криптосистемы_

Программа генерирует уникальные номера билетов для  перечисленных в файле лиц. Генератор детерминированных псевдослучайных чисел работает, хешируя(sha-256) ФИО и параметр распределения, если получено не уникальное значение - хешируется полученный на предыдущем шаге хеш
## Основные параметры программы
- написано на python 3.8.5
- в основе генератора случайных чисел лежит алгоритм хеширования sha-256
- программа генерирует исключение если число билетов меньше числа людей
- дополнительно программа оценивает качетсво алгоритма на 100.000 записей
## Вызов программы

### Парамаетры командной строки
- -n, --numbilets --- число билетов (будет сгенерирована выборка из [1..n])
- -f, --file --- файл с ФИО лиц участвующих в распределении
- -p, --parameter --- параметр распределения (аналог seed)
### Windows
Полная форма передачи параметров
```cmd
python randomizer.py --numbilets 8 --file list.txt --parameter 1232
```
Сокращенная форма передачи параметров
```cmd
python randomizer.py -n 8 -f list.txt -p 1232
```
### Ubuntu
*( Непосредственной проверки не проводилось, ожидаемый формат вызова приведен ниже )*

Полная форма передачи параметров
```sh
./randomizer.py --numbilets 8 --file list.txt --parameter 1232
```
Сокращенная форма передачи параметров
```sh
./randomizer.py -n 8 -f list.txt -p 1232
```
## Вывод консоли
Вызов (OS Windows):
```cmd
python randomizer.py --numbilets 15 --file list.txt --parameter 1232
```
Основной вывод:
```
=== WELCOME TO TICKETS RANDOMIZER ===

n=15 file=list.txt param=1232

Виталий Дмитриевич Бутерин:             3
Иван Иванович Иванов:                   15
Данила Алексеевич Поперечный:           5
Александр Степанович Попов:             11
Джон Федорович Доу:                     4
Олег Юрьевич Тиньков:                   9
Павел Валерьевич Дуров:                 12
Лев Давидович Ландау:                   7
```
Вывод при изменении порядка студентов:
```
=== WELCOME TO TICKETS RANDOMIZER ===

n=15 file=list.txt param=1232

Виталий Дмитриевич Бутерин:             3
Иван Иванович Иванов:                   15
Павел Валерьевич Дуров:                 12
Данила Алексеевич Поперечный:           5
Александр Степанович Попов:             11
Джон Федорович Доу:                     4
Лев Давидович Ландау:                   7
Олег Юрьевич Тиньков:                   9
```
Вывод оценки качества на 100k записей
- delta[ticketN] --- отклонение в % от теоретического числа билетов с данным номером
- avg delta --- среднее отклонение в % от теоретического числа билетов с каждым номером
- dispersion --- среднеквадратичное отклонение в % от теоретического числа билетов с каждым номером
```
=== BENCHMARKS(deltas of distribution for 100k records) ===

delta[ticket0]      0.016%
delta[ticket1]      0.037%
delta[ticket2]      0.029%
delta[ticket3]      0.034%
delta[ticket4]      0.067%
delta[ticket5]      0.162%
delta[ticket6]      0.194%
delta[ticket7]      0.019%
delta[ticket8]      0.047%
delta[ticket9]      0.069%
delta[ticket10]      0.029%
delta[ticket11]      0.125%
delta[ticket12]      0.140%
delta[ticket13]      0.020%
delta[ticket14]      0.041%

avg delta:          0.069%
dispersion:         0.008%
```
