# -*- coding: utf-8 -*-

# from plone.app.contenttypes.browser.collection import CollectionView
from collective.taxonomy.browser import TaxonomyCollectionView
from Products.CMFPlone.utils import safe_callable
from Products.CMFPlone.utils import safe_hasattr
from zope.interface import implementer
from zope.interface import Interface

import Missing


class ICollectionView(Interface):
    """Marker Interface for IFolderView"""


@implementer(ICollectionView)
class CollectionView(TaxonomyCollectionView):
    """ """

    def tabular_fielddata(self, item, fieldname):
        if fieldname in [
            "datum",
        ]:
            value = getattr(item, fieldname, "")
            if safe_callable(value):
                value = value()
                value = self.toLocalizedTime(value, long_format=1)
            if value == Missing.Value:
                value = ""
            return {
                "value": value,
            }
        else:
            return super().tabular_fielddata(item, fieldname)

    def tabular_field_label(self, field):
        """Look up label overrides, if no match then
        return the internationalized label (Message object) corresponding
        to the field (Plone default labels).
        """
        if safe_hasattr(self.context, "label_overrides"):
            if self.context.label_overrides:
                for loverride in self.context.label_overrides:
                    if not loverride:
                        continue
                    source_label, target_label = loverride.split("|")
                    if source_label != field:
                        continue
                    return target_label

        return super().tabular_field_label(field)
