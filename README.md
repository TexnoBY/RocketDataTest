***RocketDataTestApp***
-----------------------
# Что реализовал
## Часть 1
- База данных содержит требуемые сведения о сотрудниках
- У каждого сотрудника есть обязательное поле начальник
- База данных содержит 5 уровней иерархий, разделенных на 5 моделей сотрудников разных уровней, при созданни которых все инстансы создаются в базовом классе
- На странице Employers в админ-панели выводятся все необходимы данные о сотрудниках
- На странице Employers в админ-панели есть фильтры "Уровень", "Должность"
- На странице Employers в админ-панели есть action удаляющий выплаченную зп
- Используя DRF созданы необходимые представления
  <br/>
  Примерs
  <br/>
  
  |URL|Описание|
  |:---|:----|  
  |http://localhost/ |- Все данные о сотрудниках. |
  |http://localhost/levelusers/1|Все данные о сотрудниках одного уровня|
## Часть 2
- Заполнил бд при помощи django-seed
  <br/>
  Пример команды
  `python manage.py seed staff --number=2`
- Пользователь может получить информацию только о себе
  <br/>
  Пример
  http://localhost/me
- Проект разворачивается при помощи файла docker-compose

# Что не сделал
- Не получилось внятно реализовать иерархию сотрудников со всем необходимым функционалом, например, 
  пробовал наследование от абстрактного класса, но тогда пропадала возможность просматривать всех сотрудников в 1 модели.
  <br/> 
  Пробовал реализовать через атрибуты полей: limit_choices_to в ForeignKey, и choices в поле уровня, но не хватает опыта и знаний.
- Не получилось подключить Celery в Docker и соответственно все задания связанные с ним.

# C чем работал впервые
Это тз было не из простых, тк почти все я делал впервые, а именно:
- Создание иерархии
- В models class Meta использование атрибутов abstract, proxy
- В админ-панеле создание actions и изменение шаблона через fields
- DRF, permissions
- django-seed
- Docker



  
