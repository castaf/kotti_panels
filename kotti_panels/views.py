# -*- coding: utf-8 -*-
"""
.. inheritance-diagram:: kotti_panels.views
"""

import colander
from kotti.views.edit import AddFormView
from kotti.views.edit import ContentSchema
from kotti.views.edit import EditFormView
from kotti.views.util import template_api
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_panels import _
from kotti_panels.resources import ContentPanel


class ContentPanelSchema(ContentSchema):
    """
    Schema for UI forms to add / edit kotti_panel.resources.ContentPanel
    instances
    """

    example_text = colander.SchemaNode(colander.String())


@view_config(name=ContentPanel.type_info.add_view, permission='add',
             renderer='kotti:templates/edit/node.pt')
class ContentPanelAddForm(AddFormView):
    """Add form for kotti_panel.resources.ContentPanel instances"""

    schema_factory = ContentPanelSchema
    add = ContentPanel
    item_type = _(u"ContentPanel")


@view_config(context=ContentPanel, name='edit', permission='edit',
             renderer='kotti:templates/edit/node.pt')
class ContentPanelEditForm(EditFormView):
    """Edit form for kotti_panel.resources.ContentPanel instances"""

    schema_factory = ContentPanelSchema


@view_defaults(context=ContentPanel, permission='view')
class ContentPanelViews(object):
    """
    View class for all views registered for the
    kotti_panel.resources.ContentPanel context (except add and edit views).
    """

    def __init__(self, context, request):
        """
        Constructor

        :param context:
        :type context: kotti_panels.resources.ContentPanel
        :param request:
        :type request: pyramid.request.Request
        """

        self.context = context
        self.request = request

    @view_config(name='view', renderer='templates/view.pt')
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


def includeme(config):
    config.scan(__name__)
