# -*- coding: utf-8 -*-

"""
Registries contain information about available panel types and instances.
"""


class PanelTypeRegistry(object):
    """
    The PanelTypeRegistry can be used to obtain information on available panel
    types and to register new panel types that shall be available for
    assignment.
    """

    def available_types(self, context=None):
        """
        Return a list of classes that implement the
        :class:`kotti_panels.interfaces.IPanel` interface.

        :param context:

            If None
                return all panel types.

            If not None
                return only those panel types that can be assigned to the given
                context node item.

        :type context: :class:`kotti.resources.Content` or descendants

        :result: List of available panel types.
        :rtype: list
        """


class PanelRegistry(object):
    """
    The PanelRegistry can be used to obtain information on panel *instances*.
    """

    def assign_panel(self, panel, slot, context=None):
        """
        Assign a panel to a slot.

        :param panel:
            The panel to be assigned

        :type panel:
            kotti_panels.resources.Panel (or descendants)

        :param slot:
            Name of the slot the panel shall be assigned to.

        :type slot:
            str

        :param context:
            If None
                assign the panel "globally".
            If not None
                assign the panel "locally"

        :type context:
            kotti.resources.Content (or descendants) or None
        """

    def assigned_panels(self, context=None, slot=None):
        """
        Return a list of assigned panels.

        :param context:
            If None
                return all panels that are assigned anywhere in the resource
                tree.

            If not None
                return only those panels that are asigned to the given context
                node item.

        :type context:
            :class:`kotti.resources.Node` (or descendant)

        :param slot:
            If None
                return all panels that are assigned to any slot.
            If not None
                return only those panels that are assigned to the slot with this
                name.

        :type slot:
            str

        :result:
            List of :class:`kotti_panels.resources.Panel` (or descendants)
            instances

        :rtype:
            list
        """
        pass
