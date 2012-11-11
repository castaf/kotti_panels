# -*- coding: utf-8 -*-

"""

"""

from kotti import Base
from kotti.resources import Content
from kotti.sqla import JsonType
from kotti.sqla import MutationDict
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UnicodeText
from sqlalchemy import UniqueConstraint
from zope.interface import implements

from kotti_panels import _
from kotti_panels.interfaces import IPanel


class Panel(Content):
    """
    Base class for all panels.  Inherit from this class when implementing
    custom panels in an add-on product.
    """

    id = Column(
        Integer,
        ForeignKey('contents.id'),
        primary_key=True)

    implements(IPanel)


class StaticPanel(Panel):
    """
    Panel content type.

    Instances of StaticPanel are user editable through Kotti's UI and are
    persisted in the backend DB.  Although panels have the same attributes
    as kotti.resources.Document they are not subclassed from that class to
    prevent them showing up as discrete items in the search results.
    """

    #: primary key column in the DB
    id = Column(
        Integer,
        ForeignKey('panels.id'),
        primary_key=True)
    #: content of the panel (Unicode)
    body = Column(UnicodeText())
    #: MIME type of the Document (String)
    mime_type = Column(String(30))

    #: type_info (see kotti.resources.TypeInfo)
    type_info = Content.type_info.copy(
        name=u'Panel',
        title=_(u'Panel'),
        add_view=u'add_panel',
        addable_to=[u'Document'])

    def __init__(self, body=u"", mime_type='text/html', **kwargs):

        super(StaticPanel, self).__init__(**kwargs)

        self.body = body
        self.mime_type = mime_type


class PanelAssignment(Base):

    __tablename__ = 'panel_assigments'
    __table_args__ = (
        UniqueConstraint('node_id', 'panel_id', 'slot', 'position'),
    )

    #: primary key column in the DB
    id = Column(Integer(), primary_key=True)
    #: id of the node where the panel is assigned
    node_id = Column(ForeignKey('nodes.id'))
    #: id of the panel that is assigned
    panel_id = Column(ForeignKey('panels.id'))
    #: name of the slot the panel is assigned to
    slot = Column(String(100))
    #: position of the panel within the slot
    position = Column(Integer)
    #: is the assignment inherited to the node's children?
    inherit = Column(Boolean)
    #: values for the panel's paramters
    params = Column(MutationDict.as_mutable(JsonType))
