# -*- coding: utf-8 -*-

"""
kotti_panels
"""

from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_panels')


def kotti_configure(settings):
    """
    This function is called on startup if you a line like this in your ini
    file::

        kotti.configurators = kotti_panels.kotti_configure

    It sets up the ``kotti_panels`` addon
    """

    settings['kotti.available_types'] += ' kotti_panels.resources.StaticPanel'
    settings['kotti.includes'] += ' kotti_panels.views'
    #settings['kotti.fanstatic.view_needed'] += ' kotti_panels.static.kotti_panels_css'
