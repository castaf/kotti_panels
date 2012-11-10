# -*- coding: utf-8 -*-

"""
kotti_panels
"""

from pyramid.i18n import TranslationStringFactory

from kotti_panels.registry import PanelRegistry

_ = TranslationStringFactory('kotti_panels')


def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_panels.views'
    settings['kotti.available_types'] += ' kotti_panels.resources.ContentType'
    settings['kotti.fanstatic.view_needed'] += ' kotti_panels.static.kotti_panels_group'
