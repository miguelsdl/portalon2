from django.db import models
from django.utils.translation import gettext_lazy as _


class GameCategory(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('game category')
        verbose_name_plural = _('game categories')

    def __str__(self):
        return self.name
