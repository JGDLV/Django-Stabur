from django.db import models
from django.core.validators import FileExtensionValidator


class ContactForm(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    comment = models.TextField('Сообщение')
    create_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Задать вопрос'
        verbose_name_plural = 'Задать вопрос'

    def __str__(self):
        return self.name


class CallbackForm(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    comment = models.TextField('Сообщение')
    create_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратный звонок'

    def __str__(self):
        return self.name


class EquipmentForm(models.Model):
    equipment = models.CharField('Техника', max_length=200)
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    address = models.CharField('Адрес объекта', max_length=200)
    date = models.CharField('Дата', max_length=100)
    time = models.CharField('Время', max_length=100)
    comment = models.TextField('Сообщение')
    create_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ техники'
        verbose_name_plural = 'Заказ техники'

    def __str__(self):
        return self.name


class ServiceForm(models.Model):
    service = models.CharField('Услуга', max_length=200)
    address = models.CharField('Адрес объекта', max_length=200)
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    comment = models.TextField('Сообщение')
    # file = models.FileField('Проект', upload_to='uploads/', null=True, blank=True, validators=[FileExtensionValidator(['pdf', 'doc', 'pdf', 'jpg', 'png', 'bmp'])])
    create_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ услуги'
        verbose_name_plural = 'Заказ услуги'

    def __str__(self):
        return self.name


class TestFormModel(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    comment = models.TextField('Сообщение')
    create_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Тестовая форма'
        verbose_name_plural = 'Тестовая форма'

    def __str__(self):
        return self.name
