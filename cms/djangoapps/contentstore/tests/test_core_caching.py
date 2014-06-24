from cache_toolbox.core import get_cached_content, set_cached_content, del_cached_content
from opaque_keys.edx.locator import AssetLocator
from xmodule.contentstore.content import StaticContent
from django.test import TestCase


class Content:
    def __init__(self, location, content):
        self.location = location
        self.content = content

    def get_id(self):
        return self.location.to_deprecated_son()


class CachingTestCase(TestCase):
    course = CourseLocator(u'mitX', u'800', u'run')
#   Tests for https://edx.lighthouseapp.com/projects/102637/tickets/112-updating-asset-does-not-refresh-the-cached-copy
    unicodeLocation = AssetLocator(course, u'thumbnail', u'monsters.jpg')
    # Note that some of the parts are strings instead of unicode strings
    nonUnicodeLocation = AssetLocator(course, 'thumbnail', 'monsters.jpg')
    mockAsset = Content(unicodeLocation, 'my content')

    def test_put_and_get(self):
        set_cached_content(self.mockAsset)
        self.assertEqual(self.mockAsset.content, get_cached_content(self.unicodeLocation).content,
                         'should be stored in cache with unicodeLocation')
        self.assertEqual(self.mockAsset.content, get_cached_content(self.nonUnicodeLocation).content,
                         'should be stored in cache with nonUnicodeLocation')

    def test_delete(self):
        set_cached_content(self.mockAsset)
        del_cached_content(self.nonUnicodeLocation)
        self.assertEqual(None, get_cached_content(self.unicodeLocation),
                         'should not be stored in cache with unicodeLocation')
        self.assertEqual(None, get_cached_content(self.nonUnicodeLocation),
                         'should not be stored in cache with nonUnicodeLocation')
