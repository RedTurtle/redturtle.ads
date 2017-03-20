# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from redturtle.ads.testing import REDTURTLE_ADS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that redturtle.ads is properly installed."""

    layer = REDTURTLE_ADS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if redturtle.ads is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'redturtle.ads'))

    def test_browserlayer(self):
        """Test that IRedturtleAdsLayer is registered."""
        from redturtle.ads.interfaces import (
            IRedturtleAdsLayer)
        from plone.browserlayer import utils
        self.assertIn(IRedturtleAdsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = REDTURTLE_ADS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['redturtle.ads'])

    def test_product_uninstalled(self):
        """Test if redturtle.ads is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'redturtle.ads'))

    def test_browserlayer_removed(self):
        """Test that IRedturtleAdsLayer is removed."""
        from redturtle.ads.interfaces import \
            IRedturtleAdsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IRedturtleAdsLayer, utils.registered_layers())
