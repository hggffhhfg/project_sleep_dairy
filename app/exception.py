class NonUniqueNotationDate(Exception):
    """Ошибка возникающая, если при импортировании файла с записями находится запись с датой,
    которая уже существует в дневнике сна/базе данных"""
    pass


Errors = {
    'add': 'При добавлении записи в дневник произошла ошибка',
    'update': 'При обновлении записи в дневнике произошла ошибка',
    'value': 'Неподходящее значение',
    'syntax': 'Неподходящий формат',
    'type': 'Неподходящий тип данных',
    'database': 'При обращении к базе данных произошла ошибка',
    'file': 'Файл не был найден',
    'import': 'При импортировании произошла ошибка',
    'other': 'Прочая ошибка'
}
