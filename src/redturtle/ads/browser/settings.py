# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from redturtle.ads.interfaces import IRedturtleAdsAdvertisementSettings


class AdvertisementSettingsEditForm(RegistryEditForm):
    schema = IRedturtleAdsAdvertisementSettings
    label = u"Advertisement settings"


class AdvertisementSettingsView(ControlPanelFormWrapper):
    form = AdvertisementSettingsEditForm
