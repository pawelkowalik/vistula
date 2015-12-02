# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Protocol(models.Model):
    TYPE = (
        ('C','częściowy'),
        ('K','końcowy'),
    )
    type = models.CharField(max_length=1, choices=TYPE, verbose_name='Typ')
    slug = models.SlugField('Odnosnik', max_length=50)
    object = models.CharField('Obiekt:', max_length=100)
    contractor = models.CharField('Wykonany przez:', max_length=100)
    agreement = models.CharField('Na podstawie wyceny:', max_length=100)
    order = models.CharField('I zlecenie nr:', max_length=100, null=True, blank=True)
    agreement_day = models.CharField('z dnia:', max_length=100)
    inv1 = models.CharField('Komisja inwestor 1:', max_length=50)
    inv2 = models.CharField('Komisja inwestor 2:', max_length=50, null=True, blank=True)
    inv3 = models.CharField('Komisja inwestor 3:', max_length=50, null=True, blank=True)
    cont1 = models.CharField('Komisja wykonawca 1:', max_length=50)
    cont2 = models.CharField('Komisja wykonawca 2:', max_length=50, null=True, blank=True)
    date = models.DateField('Data protokołu')
    works = models.TextField(verbose_name='W dniu ... komisja dokonała odbioru niżej wymienionych robót:')
    works_quality = models.CharField('Roboty zostały wykonane:', max_length=100)
    mistakes = models.TextField(verbose_name='Usterki:')
    correct_mistakes_day = models.CharField('Komisja zobowiązuje wykonawcę do usunięcia usterek w terminie do dnia:', max_length=20)
    resolutions = models.TextField(verbose_name='Komisja postanawia:')

    class Meta:
        verbose_name = "Protokół odbioru robót"
        verbose_name_plural = "Protokoły odbioru robót"

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('protocol-detail', kwargs={'slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None):
        d = self.date
        dt = '{:%Y-%m-%d}'.format(d)
        self.slug = slugify("protokol " + str(self.contractor) + " " + str(dt))
        super(Protocol, self).save(force_insert, force_update, using)