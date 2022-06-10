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


def migrate_to_1003(context):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(default_profile, 'plone.app.registry')
    setup_tool.runImportStepFromProfile(default_profile, 'controlpanel')
    logger.info(u'Updated to 1003')


def migrate_to_1004(context):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(default_profile, 'plone.app.registry')


def migrate_to_1005(context):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(default_profile, 'rolemap')
    logger.info(u'Updated to 1005')


def remove_css(context):
    'Import the removecss profile'
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(
        'profile-redturtle.ads:removecss',
        'plone.app.registry',
        run_dependencies=False
    )
