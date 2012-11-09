from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

library = Library("kotti_panels", "static")
kotti_panels_css = Resource(library, "style.css")
kotti_panels_group = Group([kotti_panels_css])
