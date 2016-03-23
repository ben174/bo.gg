# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    weight = models.DecimalField(
        null=True,
        blank=True,
        verbose_name='Current weight.',
        name='Weight',
        decimal_places=2,
        max_digits=6,
    )

    calorie_allowance = models.IntegerField(
        default=2000,
        verbose_name='Daily calorie intake allowance.',
        name='Daily Calorie Allowance',
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
