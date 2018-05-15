# -*- coding: utf-8 -*-
from plone import api
from redturtle.ads import logger


default_profile = 'profile-redturtle.ads:default'


def migrate_to_1001(context):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(default_profile, 'plone.app.registry')
    logger.info(u'Updated to 1001')


def migrate_to_1002(context):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(default_profile, 'workflow')
    logger.info(u'Updated to 1002')
