# -*- coding: utf-8 -*-

extensions = [
    'repoze.sphinx.autointerface',
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'kotti_panels'
copyright = u'2012, Andreas Kaiser and contributors'
version = '0.1'
release = version
today_fmt = '%Y-%m-%d'
exclude_patterns = ['_build', '_themes']
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------
html_theme_path = ['_themes']
html_theme = 'sphinx-bootstrap'
html_theme_options = {
    'github_user': 'disko',
    'github_repo': 'kotti_panels',
    'twitter_username': 'KottiCMS',
    'home_url': 'https://github.com/disko/kotti_panels',
}
html_static_path = ['_static']
html_last_updated_fmt = '%Y-%m-%d'
htmlhelp_basename = 'kottipanelsdoc'

# -- Options for inheritance diagrams -----------------------------------------
inheritance_graph_attrs = dict(
    rankdir='TB',
    nodesep=0.1,
    ratio='auto',
    size=11.0
)
inheritance_node_attrs = dict(
    height=0.7,
    margin='0.06, 0.03'
)

# -- Options for Intersphinx --------------------------------------------------
intersphinx_mapping = {
    'colander': ('http://colander.readthedocs.org/en/latest/', None),
    'deform': ('http://deform.readthedocs.org/en/latest/', None),
    'kotti': ('http://kotti.readthedocs.org/en/latest/', None),
    'pyramid': ('http://pyramid.readthedocs.org/en/latest/', None),
    'sqlalchemy': ('http://sqlalchemy.readthedocs.org/en/latest/', None),
}
