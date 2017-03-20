# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import redturtle.ads


class RedturtleAdsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=redturtle.ads)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.ads:default')


REDTURTLE_ADS_FIXTURE = RedturtleAdsLayer()


REDTURTLE_ADS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_ADS_FIXTURE,),
    name='RedturtleAdsLayer:IntegrationTesting'
)


REDTURTLE_ADS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_ADS_FIXTURE,),
    name='RedturtleAdsLayer:FunctionalTesting'
)


REDTURTLE_ADS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_ADS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RedturtleAdsLayer:AcceptanceTesting'
)
