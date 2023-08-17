# -*- coding: utf-8 -*-
from collective.tabularlabeloverrides.testing import (
    COLLECTIVE_TABULARLABELOVERRIDES_FUNCTIONAL_TESTING,
)
from collective.tabularlabeloverrides.testing import (
    COLLECTIVE_TABULARLABELOVERRIDES_INTEGRATION_TESTING,
)
from collective.tabularlabeloverrides.views.folder_view import ICollectionView
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_TABULARLABELOVERRIDES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "folder1")
        api.content.create(self.portal, "Collection", "collection1")

    def test_tabular_label_overrides_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal["collection1"], self.portal.REQUEST),
            name="tabular_label_override_view",
        )
        self.assertTrue(ICollectionView.providedBy(view))

    def test_tabular_label_overrides_view_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal["folder1"], self.portal.REQUEST),
                name="tabular_label_override_view",
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = ICollectionView.providedBy(view)
        self.assertFalse(view_found)

    def test_tabular_label_overrides_view_rendering(self):
        view = getMultiAdapter(
            (self.portal["collection1"], self.portal.REQUEST),
            name="tabular_label_override_view",
        )
        view()


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_TABULARLABELOVERRIDES_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
