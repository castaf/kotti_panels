import colander
from kotti.views.edit import AddFormView
from kotti.views.edit import ContentSchema
from kotti.views.edit import EditFormView
from kotti.views.util import template_api

from kotti_panels import _
from kotti_panels.resources import ContentType


class ContentTypeSchema(ContentSchema):
    example_text = colander.SchemaNode(colander.String())


class ContentTypeAddForm(AddFormView):
    schema_factory = ContentTypeSchema
    add = ContentType
    item_type = _(u"ContentType")


class ContentTypeEditForm(EditFormView):
    schema_factory = ContentTypeSchema


def view_content_type(context, request):
    return {
        'api': template_api(context, request),  # this bounds context and request variables to the api in the template
        'example_text': context.example_text,  # this can be called directly in the template as example_text
        }


def includeme_edit(config):

    config.add_view(
        ContentTypeEditForm,
        context=ContentType,
        name='edit',
        permission='edit',
        renderer='kotti:templates/edit/node.pt',
        )

    config.add_view(
        ContentTypeAddForm,
        name=ContentType.type_info.add_view,
        permission='add',
        renderer='kotti:templates/edit/node.pt',
        )


def includeme_view(config):

    config.add_view(
        view_content_type,
        context=ContentType,
        name='view',
        permission='view',
        renderer='templates/view.pt',
        )

    config.add_static_view('static-kotti_panels', 'kotti_panels:static')


def includeme(config):
    includeme_edit(config)
    includeme_view(config)
