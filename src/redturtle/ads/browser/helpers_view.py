# -*- coding: utf-8 -*-
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from plone import api
from plone.app.contenttypes.browser.folder import FolderView
import pkg_resources
from plone.memoize import instance


class HelpersView(BrowserView):

    @instance.memoize
    def getAppVersion(self):
        """ used to invalidate the cache every new release """
        return pkg_resources.get_distribution("redturtle.ads").version

    def getImageScale(self, context, miniature="thumb"):
        scales = api.content.get_view(
            name="images", context=context, request=self.request)
        scale = scales.scale('image', miniature)
        if not scale:
            return ""
        return scale.tag()

    def getCategory(self, context=None):
        if not context:
            context = self.context
        category = context.aq_parent
        return {
            'title': category.Title(),
            'url': category.absolute_url()
        }

    def getFormattedDate(self, date):
        return api.portal.get_localized_time(datetime=date)
