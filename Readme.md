### Что это?

Учебный проект: реализация упрощенного рекламного сервера, а точнее часть, которая откручивает план.

### Как запустить?

```sh
$ pip3 install pyqt5 numpy matplotlib
$ python3 main.py
```

### Как использовать?

- На начальном экране необходимо указать пути к файлам описывающим функции
плана открутки, вероятностного распределения и трафика.
- Выбрать один из двух режимов ручной или автоматический
- Инициализировать начальные условия и ограничения
- Нажать 'OK'
- Сохранить табулированные функции как CSV-файлы
- Сохранить интерполированные функции в виде pickle файлов

### Детали реализации

Все численные методы вынесены в модуль num_methods и пока что представляют из себя заглушки (интерполяция прямыми, интеграл по двум точкам и т.д.).

Вся основная работа происходит с объектами класса *Interpolation* с перегруженными операторами скобки.

На данном этапе фунции можно задать только по сетке, но в `utils.py` можно найти все
необходимые методы для загрузки pickle и json.


