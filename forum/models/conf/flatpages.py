"""
Q&A forum flatpages (about, etc.)
"""
from forum.conf.settings_wrapper import settings
from livesettings import ConfigurationGroup, LongStringValue
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

FLATPAGES = ConfigurationGroup(
                'FLATPAGES',
                _('Flatpages - about, privacy policy, etc.')
            )

settings.register(
    LongStringValue(
        FLATPAGES,
        'FORUM_ABOUT',
        description=_('Text the Q&A forum About page (html format)'),
        help_text=\
        _(
            'Save, then <a href="http://validator.w3.org/check?uri=%(url)s">'
            'validate HTML</a>'
        ) % {'url':reverse('about')}
    )
)

settings.register(
    LongStringValue(
        FLATPAGES,
        'FORUM_PRIVACY',
        description=_('Text the Q&A forum Privacy Policy (html format)'),
        help_text=\
        _(
            'Save, then <a href="http://validator.w3.org/check?uri=%(url)s">'
            'validate HTML</a>'
        ) % {'url':reverse('privacy')}
    )
)
