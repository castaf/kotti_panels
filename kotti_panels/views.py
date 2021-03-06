# -*- coding: utf-8 -*-
"""
Every panel needs at least 2 views:

-   "view":
        display the panel as an ordinary content item

-   "inline":
        display the panel inline (in a slot it is assigned to)
"""

import colander
from kotti.resources import Content
from kotti.views.edit import AddFormView
from kotti.views.edit import DocumentSchema
from kotti.views.edit import EditFormView
from kotti.views.slots import assign_slot
from kotti.views.util import template_api
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_panels import _
from kotti_panels.resources import StaticPanel


class StaticPanelSchema(DocumentSchema):
    """
    Schema for UI forms to add / edit kotti_panel.resources.StaticPanel
    instances
    """


@view_config(name=StaticPanel.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class StaticPanelAddForm(AddFormView):
    """Add form for :class:`kotti_panel.resources.StaticPanel` instances"""

    schema_factory = StaticPanelSchema
    add = StaticPanel
    item_type = _(u"StaticPanel")


@view_config(context=StaticPanel, name='edit', permission='edit',
             renderer='kotti:templates/edit/node.pt')
class StaticPanelEditForm(EditFormView):
    """Edit form for :class:`kotti_panel.resources.StaticPanel` instances"""

    schema_factory = StaticPanelSchema


@view_defaults(context=StaticPanel, permission='view')
class StaticPanelViews(object):
    """
    View class for all views registered for the
    kotti_panel.resources.StaticPanel context (except add and edit views).
    """

    def __init__(self, context, request):
        """
        Constructor

        :param context:
        :type context: kotti_panels.resources.StaticPanel
        :param request:
        :type request: pyramid.request.Request
        """

        self.context = context
        self.request = request

    @view_config(name='view', renderer='templates/static-panel-view.pt')
    def view(self):
        """
        Default view for panels

        :return:
        :rtype: dict
        """

        return {
            'api': template_api(self.context, self.request),  # this bounds context and request variables to the api in the template
            'example_text': self.context.example_text,  # this can be called directly in the template as example_text
        }

    @view_config(name='inline', renderer='templates/static-panel-inline.pt')
    def inline(self):
        """
        Inline view for StaticPanel

        :return:
        :rtype: dict
        """

        return {
            'api': template_api(self.context, self.request),  # this bounds context and request variables to the api in the template
            'example_text': self.context.example_text,  # this can be called directly in the template as example_text
        }


@view_defaults(context=Content)
class GlobalSlotViews(object):
    """GlobalSlotViews provides a view for each of the global slots."""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name='left')
    def left(self):
        """Render all panels that are assigned to the ``left`` slot."""

    @view_config(name='right')
    def right(self):
        """Render all panels that are assigned to the ``right`` slot."""

    @view_config(name='abovecontent')
    def abovecontent(self):
        """Render all panels that are assigned to the ``abovecontent`` slot."""

    @view_config(name='belowcontent')
    def belowcontent(self):
        """Render all panels that are assigned to the ``belowcontent`` slot."""

    @view_config(name='beforebodyend')
    def beforebodyend(self):
        """Render all panels that are assigned to the ``beforebodyend`` slot."""


def includeme(config):

    config.scan(__name__)

    # Assign each view to the slot with the same name
    for name in ('left', 'right', 'abovecontent', 'belowcontent',
                 'beforebodyend', ):

        assign_slot(name, name, params=None)
