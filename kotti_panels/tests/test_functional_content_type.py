from kotti.resources import get_root
from kotti.testing import DummyRequest
from kotti.testing import FunctionalTestBase
from kotti.testing import setUpFunctional

from kotti_panels.resources import ContentType
from kotti_panels.views import view_content_type


class TestContentView(FunctionalTestBase):

    def setUp(self, **kwargs):
        settings = {'kotti.configurators': 'kotti_panels.kotti_configure'}
        self.__dict__.update(setUpFunctional(**settings))

    def test_content_view(self):
        root = get_root()
        root['content-type'] = ContentType(title=u'New Content Type',
                                           example_text=u'some text')
        result = view_content_type(root['content-type'], DummyRequest())
        assert result[u'example_text'] == u'some text'

    def test_browser_call(self):
        browser = self.login_testbrowser()
        browser.open(self.BASE_URL + '/@@add_content_type')
        browser.getControl('Title').value = u'Content Type Title'
        browser.getControl('Example Text').value = u'some Text'
        browser.getControl('save').click()
        assert "Successfully added item" in browser.contents