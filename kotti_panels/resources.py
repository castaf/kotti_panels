# -*- coding: utf-8 -*-

"""

"""

from kotti import Base
from kotti.resources import Document
from kotti.sqla import JsonType
from kotti.sqla import MutationDict
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from zope.interface import implements

from kotti_panels import _
from kotti_panels.interfaces import IPanel


class Panel(object):
    """
    Base class for all panels.
    """

    implements(IPanel)


class StaticPanel(Document, Panel):
    """
    Panel content type.

    Instances of StaticPanel are user editable through Kotti's UI and are
    persisted in the backend DB.
    """

    #: primary key column in the DB
    id = Column(
        Integer,
        ForeignKey('documents.id'),
        primary_key=True)

    #: type_info (see kotti.resources.TypeInfo)
    type_info = Document.type_info.copy(
        name=u'Panel',
        title=_(u'Panel'),
        add_view=u'add_panel',
        addable_to=[u'Document'])


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
