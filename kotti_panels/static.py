# -*- coding: utf-8 -*-

"""

"""

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

#: see fanstatic.Library
library = Library("kotti_panels", "static")

#: see fanstatic.Resource
kotti_panels_css = Resource(library, "style.css")

#: see fanstatic.Group
kotti_panels_group = Group([kotti_panels_css])
