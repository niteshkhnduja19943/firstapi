from django.utils.translation import gettext_lazy as _

from django.db import models

class TestTable(models.Model):
    name = models.CharField(_('First Name'), max_length=150, null=False, blank=False)
    password = models.IntegerField(_('password'), null=False, blank=False)

    def __str__(self):
        return self.name, self.password



