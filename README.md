# Redis database practise and cache
## Task №2:
> Кеширование результатов выполнения функций

## Почему Redis?
Так как это база данных типа ключ-значение, которая позволяет хранить данные в оперативной памяти.
## Чем полезно кэширование?
Это метод оптимизации производительности приложений, который заключается в сохранении результатов выполнения функций в кеше, чтобы при повторном вызове функции с теми же входными параметрами не происходило повторного вычисления, а результат брался из кеша.
## Запуск
```shell
pip install sqlite3 socket
python server.py
```
затем открыть новый терминал
```shell
python сlient.py
```
