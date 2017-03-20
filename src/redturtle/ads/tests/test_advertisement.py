# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from redturtle.ads.interfaces import IAdvertisement
from redturtle.ads.testing import REDTURTLE_ADS_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class AdvertisementIntegrationTest(unittest.TestCase):

    layer = REDTURTLE_ADS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Advertisement')
        schema = fti.lookupSchema()
        self.assertEqual(IAdvertisement, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Advertisement')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Advertisement')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IAdvertisement.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Advertisement',
            id='Advertisement',
        )
        self.assertTrue(IAdvertisement.providedBy(obj))
