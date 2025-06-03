from django.db import models
from django.utils.translation import gettext_lazy as _
from games.models.game_category import GameCategory
from games.models.game_platform import GamePlatform
from filer.fields.image import FilerImageField


class Game(models.Model):
    """
    docs/games.md
    """
    title = models.CharField(_('title'), max_length=200)
    description = models.TextField(_('description'), blank=True)
    category = models.ForeignKey(
        GameCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('category')
    )
    platform = models.ForeignKey(
        GamePlatform, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('platform')
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    # Campos para ROMs
    rom = models.FileField(_('ROM file'), upload_to='roms/', blank=True, null=True)

    # Imagen del juego
    image = FilerImageField(
        verbose_name=_('image'),
        on_delete=models.CASCADE,
        blank=True, null=True,
    )
    checksum = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = _('game')
        verbose_name_plural = _('games')

    def __str__(self):
        return self.title
