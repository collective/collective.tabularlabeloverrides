# -*- coding: utf-8 -*-

from plone.app.contenttypes.browser.collection import CollectionView
from zope.interface import implementer
from zope.interface import Interface


class IFolderView(Interface):
    """Marker Interface for IFolderView"""


@implementer(IFolderView)
class FolderView(CollectionView):
    def __call__(self):
        template = """<li class="heading" i18n:translate="">
          Sample View
        </li>"""
        return template
