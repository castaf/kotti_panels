# -*- coding: utf-8 -*-

"""
Interfaces.

.. inheritance-diagram:: kotti_panels.interfaces
"""

from zope.interface import Interface


class IPanel(Interface):
    """Marker interface to make something assignable as a panel in the UI"""
