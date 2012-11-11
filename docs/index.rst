.. _index:

==========================
Kotti Panels Documentation
==========================

``kotti_panels`` provides support for reusable units of content in Kotti that
can be defined by either

-   a content manager (via Kotti UI) for "static" content or

-   the developer (by subclassing a base class and using the new
    package's API) for "dynamic" content units - i.e. such that have
    some additional logic.  E.g.: tag cloud, navigation, etc.

Panels, Slots and Assignments
-----------------------------

Panel
    A panel is a piece of content or a rendered result of a function.

    StaticPanel
        A static panel is a content node that is creatable and editable by
        content managers via the Kotti UI.

    Dynamic Panel
        A dynamic panel is the result of a function that may (or not) have
        parameters that influence its result.  Dynamic panels are created by
        developers.  Content managers can assign them to slots and provide
        values for their parameters.

Slot
    A slot is a place in a template to which panels can be assigned for inline
    rendering.  Slots can either be defined on your ``main_template`` or in an
    arbitrary view template.

    Global Slot
        A slot defined in the master template.  Panels assigned to one of these
        slots are displayed in every view that uses the master template.

    Local Slot
        A slot defined in a view template.  Panels assigned to one of these
        slots are only displayed when the respective view is displayed.

Panel to slot assignment
    Panels can be locally assigned to slots for every node in your resource
    tree.  Assignments can optionally be inherted to the node's children.

Table of Contents
-----------------

.. toctree::
    :maxdepth: 1

    API <api>

    Roadmap <roadmap>

    View the original proposal <KLIP>

