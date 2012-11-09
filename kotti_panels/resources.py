# -*- coding: utf-8 -*-

"""
.. inheritance-diagram:: kotti_panels.resources
"""

from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from zope.interface import implements

from kotti_panels import _
from kotti_panels.interfaces import IPanel


class Panel(object):
    """
    Base class for all panels.
    """

    implements(IPanel)


class ContentPanel(Content, Panel):
    """
    Panel content type.

    Instances of PanelContent are user editable through Kotti's UI and are
    persisted in the backend DB.
    """

    #: primary key column in the DB
    id = Column(
        Integer,
        ForeignKey('contents.id'),
        primary_key=True)
    #: an example column
    example_text = Column(
        'example_text',
        Unicode(256))

    #: type_info (see kotti.resources.TypeInfo)
    type_info = Content.type_info.copy(
        name=u'Panel',
        title=_(u'Panel'),
        add_view=u'add_panel',
        addable_to=[u'Document'])

    def __init__(self, example_text=u'', **kwargs):
        """
        :param example_text: example text
        :type example_text: unicode
        """

        Content.__init__(self, **kwargs)
        self.example_text = example_text
