from fobi.base import theme_registry

from fobi.contrib.themes.bootstrap3.fobi_themes import Bootstrap3Theme

__all__ = ('CustomFobiTheme',)


class CustomFobiTheme(Bootstrap3Theme):
  """Overriding the "bootstrap3Theme" theme."""
  html_classes = ['custom-fobi-theme', ]
  base_template = 'form_manager/custom_fobi_base.html'
  # See fobi.contrib.themes.bootstrap3.fobi_themes.Bootstrap3Theme for fields


# It's important to set the `force` argument to True, in
# order to override the original theme. Force can be applied
# only once.
theme_registry.register(CustomFobiTheme, force=True)
