# Generated by the windmill services transformer
from windmill.authoring import WindmillTestClient

def test_foreign_open():
    client = WindmillTestClient(__name__)

    client.open(url=u'http://www.asdf.com')
    client.waits.forPageLoad(timeout=u'2000')
    client.asserts.assertJS(js=u"windmill.testWin().document.title == 'asdf'")
    