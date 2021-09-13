from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# статусы: (открытый, закрытый, черновик)
STATUS_CHOICES = (
    ('open', 'открытое'),
    ('closed', 'закрытое'),
    ('draft', 'черновик')
)


class Publication(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Текст")
    status = models.CharField("Статус", max_length=10, choices=STATUS_CHOICES)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='pubs',
                             verbose_name='Пользователь')
    created_at = models.DateField("Дата создания", auto_now_add=True)
    updated_at = models.DateField("Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = 'Обьъявления'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comment(models.Model):
    publication = models.ForeignKey(Publication,
                                    on_delete=models.CASCADE,
                                    related_name='reviews',
                                    verbose_name='Объявление')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Автор')
    text = models.TextField("Текст")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.publication} --> {self.user}'


# INSERT
# Publication.objects.create(title='...', text='...', ...)
# INSERT INTO publication (title, text, ...) VALUES (...);
# pub = Publication(title=..., text="...", ...)
# pub.save()

# Publication.objects.bulk_create([
#     Publication(...),
#     Publication(...),
#     Publication(...)
# ])

# SELECT
# SELECT * FROM publication;
# Publication.objects.all()

# SELECT title FROM publication;
# Publication.objects.only('title')

# SELECT title, text, status FROM publication;
# Publication.objects.only('title', 'text', 'status')
# Publication.objects.defer('user', 'created_at', 'updated_at')

# фильтрация
# SELECT * FROM publication WHERE ...;
# Publication.objects.filter(...)

# Операции:
# SELECT * FROM publication WHERE id = 1;
# Publication.object.filter(id=1)


# SELECT * FROM publication WHERE created_at '...';
# Publication.objects.filter(created_at__gt=current)
# current = datetime.datetime.strptime('09-09-2021 12:52:46', '%d-%m-%Y-%M-%S')

# ">" -> gt
# ">" -> lt
# >= -> gte
# <= -> lte
# "=" -> =
# "=" -> exact/iexact
# "IN" -> in
# "BETWEEN" -> range

# сорторовка
# SELECT * FROM publication ORDER BY created_at ASC;
# Publication.object.order_by('created_at')
# Publication.object.order_by('-created_at')

# SELECT * FROM publication WHERE ... ORDER BY created_at
# Publication.object.filter(...).order_by('created_at')

# LIMIT
# SELECT * FROM publication LIMIT 10;
# Publication.object.all()[10]

# SELECT * FROM publication LIMIT 10 OFFSET 10;
# Publication.object.all()[10:20]

# SELECT * FROM publication WHERE id=1;
# Publication.object.filter(id=1)
# [pub1]

# получение одной записи
# SELECT * FROM publication WHERE id=1 LIMIT 1;
# Publication.object.get(id=1)
# Publication.object.filter(id=1).first()


# LIKE, ILIKE
# LIKE/ILIKE 'Samsung%' -> startswith/istartswith

# LIKE/ILIKE '%11' -> endswith/iendswith

# LIKE/ILIKE '%something%' -> contains/icontains


# UPDATE
# обновление всех записей
# UPDATE publication SET status='closed';
# Publication.object.update(status='closed')


# обновление частей записей
# UPDATE publication SET status='closed' WHERE status='draft'
# Publication.object.filter(status='draft').update(status='closed')

# обновление одной записи


# База данных — определение

# База данных — это упорядоченный набор структурированной информации или данных, которые обычно хранятся в электронном
# виде в компьютерной системе. База данных обычно управляется системой управления базами данных (СУБД).


#
# ORM (англ. Object-Relational Mapping, рус. объектно-реляционное отображение, или преобразование) — технология
# программирования, которая связывает базы данных с концепциями объектно-ориентированных языков программирования,
# создавая «виртуальную объектную базу данных».


# Система управления базами данных (СУБД) – это комплекс программно-языковых средств, позволяющих создать базы
# данных  и управлять данными.


# Git — система управления версиями с распределенной архитектурой. В отличие от некогда популярных систем вроде CVS и
# Subversion (SVN), где полная история версий проекта доступна лишь в одном месте, в Git каждая рабочая копия кода сама
# по себе является репозиторием.


# Screaming Frog – это софт для сканирования сайта, ключевыми функциями которого являются: поиск битых ссылок; ...
# извлечение элементов со страниц сайта; поиск пустых страниц или неинформативных страниц, где крайне мало контента.


# Парсинг – это процесс сбора данных с последующей их обработкой и анализом. К этому способу прибегают, когда предстоит
# обработать большой массив информации, с которым сложно справиться вручную. Программа, которая производит сбор и
# синтаксический анализ, – это парсер (определение «Википедии»).


# HTML (Hypertext Markup Language) - это код, который используется для структурирования и отображения веб-страницы
# и её контента.


# Cascading Style Sheets «каскадные таблицы стилей») — формальный язык описания внешнего вида документа (веб-страницы),
# написанного с использованием языка разметки (чаще всего HTML или XHTML).


# DELETE

# удаление записей
# DELETE FROM publication
# Publication.object.delete()

# удаление части записей
# DELETE FROM publication WHERE status='closed';
# Publication.object.filter(status='closed').delete()

# удаление одной записи
# DELETE FROM publication WHERE id=1;
# 1. Publication.object.filter(id=1).delete()
# 2. pub = Publication.
