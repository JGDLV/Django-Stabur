from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


class Service(models.Model):
    ''' Модель услуги '''

    slug = models.SlugField('Слаг')
    title = models.CharField('Название', max_length=200)
    title_full = models.CharField(
        'Название полное', max_length=250, blank=True)
    description = HTMLField('Описание')
    description_full = HTMLField('Описание полное', blank=True)
    image_preview = models.ImageField('Превью')
    image_detail = models.ImageField('Детальная картинка')
    types_header = models.CharField(
        'Заголовок для дополнительных услуг', max_length=200, blank=True)
    types_text = HTMLField('Текст для дополнительных услуг', blank=True)
    projects_header = models.CharField(
        'Заголовок для проектов', max_length=200, blank=True)
    projects_text = HTMLField('Текст для проектов', blank=True)
    projects = models.ManyToManyField(
        'Project', related_name='projects', blank=True, verbose_name='Проекты')
    equipment_header = models.CharField(
        'Заголовок для техники', max_length=200, blank=True)
    equipment_text = HTMLField('Текст для техники', blank=True)
    equipment = models.ManyToManyField(
        'Equipment',
        related_name='equipment',
        blank=True,
        verbose_name='Техника')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Scheme(models.Model):
    ''' Модель схемы '''

    scheme = models.OneToOneField(
        'Service', null=True, on_delete=models.CASCADE, verbose_name='Схема', related_name="scheme")
    header = models.CharField('Заголовок', max_length=200)
    text_top = HTMLField('Текст вверху')
    text_bottom = HTMLField('Текст внизу')

    class Meta:
        verbose_name = 'Схема работы'
        verbose_name_plural = 'Схемы работы'

    def __str__(self):
        return self.scheme.title


class SchemeItem(models.Model):
    ''' Модель пункта схемы '''

    scheme = models.ForeignKey('Scheme', null=True, on_delete=models.CASCADE,
                               verbose_name='Пункт схемы', related_name="items")
    title = models.CharField('Заголовок', max_length=100)
    value = HTMLField('Текст')

    class Meta:
        verbose_name = 'Пункт схемы'
        verbose_name_plural = 'Пункты схемы'

    def __str__(self):
        return self.title


class Type(models.Model):
    ''' Модель дополнительной услуги '''

    service = models.ForeignKey('Service', null=True, on_delete=models.CASCADE,
                                verbose_name='Дополнительная услуга', related_name="types")
    title = models.CharField('Название', max_length=200)
    description = HTMLField('Описание')
    image = models.ImageField('Картинка')

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'

    def __str__(self):
        return self.title


class Project(models.Model):
    ''' Модель проекта '''

    title = models.CharField('Название', max_length=200)
    description = HTMLField('Описание')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    ''' Модель картинки проекта '''

    project = models.ForeignKey(
        'Project', null=True, on_delete=models.CASCADE, related_name='images', verbose_name='Проект')
    image = models.ImageField('Картинка')

    class Meta:
        verbose_name = 'Картинка проекта'
        verbose_name_plural = 'Картинки проекта'

    def __str__(self):
        return ''


class ProjectProperty(models.Model):
    ''' Модель свойства проекта '''

    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE,
                                verbose_name='Проект', related_name="properties")
    title = models.ForeignKey('ProjectPropertyName', null=True,
                              on_delete=models.SET_NULL, verbose_name='Свойство')
    value = models.CharField('Значение', max_length=100)

    class Meta:
        verbose_name = 'Свойство проекта'
        verbose_name_plural = 'Свойства проекта'

    def __str__(self):
        return ''


class ProjectPropertyName(models.Model):
    ''' Модель названия свойства проекта '''

    title = models.CharField('Название', max_length=200)

    class Meta:
        verbose_name = 'Свойство проекта'
        verbose_name_plural = 'Свойства проекта'

    def __str__(self):
        return self.title


class Equipment(models.Model):
    ''' Модель техники '''

    title = models.CharField('Название', max_length=200)
    price = models.PositiveIntegerField('Цена')
    price_type = models.ForeignKey(
        'EquipmentPrice', null=True, on_delete=models.SET_NULL, verbose_name='Тип цены')
    image = models.ImageField('Картинка')

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return self.title


class EquipmentPrice(models.Model):
    ''' Модель типа цен техники '''

    title = models.CharField('Название', max_length=10)

    class Meta:
        verbose_name = 'Тип цены'
        verbose_name_plural = 'Типы цены'

    def __str__(self):
        return self.title


class EquipmentProperty(models.Model):
    ''' Модель свойства техники '''

    equipment = models.ForeignKey('Equipment', null=True, on_delete=models.CASCADE,
                                  verbose_name='Техника', related_name="properties")
    title = models.ForeignKey('EquipmentPropertyName', null=True,
                              on_delete=models.SET_NULL, verbose_name='Свойство')
    value = models.CharField('Значение', max_length=100)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'

    def __str__(self):
        return ''


class EquipmentPropertyName(models.Model):
    ''' Модель названия свойства техники '''

    title = models.CharField('Название', max_length=200)

    class Meta:
        verbose_name = 'Свойство техники'
        verbose_name_plural = 'Свойства техники'

    def __str__(self):
        return self.title


class Document(models.Model):
    ''' Модель документа '''

    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Картинка')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title


class Contact(models.Model):
    ''' Контакты '''

    ceo = models.CharField('Директор', max_length=100)
    full_name = models.CharField(
        'Полное наименование организации', max_length=250)
    left = HTMLField('Левая колонка')
    right = HTMLField('Правая колонка')
    email = models.CharField('E-mail', max_length=100)
    phone = models.CharField('Номер тел./факс', max_length=20)
    address = models.CharField('Юридический и почтовый адрес', max_length=200)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True, null=True)


    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.full_name
