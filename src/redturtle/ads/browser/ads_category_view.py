# -*- coding: utf-8 -*-
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from plone import api
from plone.app.contenttypes.browser.folder import FolderView
from redturtle.ads.browser.helpers_view import HelpersView


class AdsCategoryView(FolderView, HelpersView):
    '''
    View for an Announcement
    '''

    def __call__(self):
        # utility function to add resource to rendered page
        add_resource_on_request(self.request, 'ads_layout')
        return super(AdsCategoryView, self).__call__()

    def getAdvertisementInfos(self, brain):
        item = brain.getObject()
        res = {
            'title': item.Title(),
            'description': item.Description(),
            'url': item.absolute_url(),
            'price': item.price,
        }
        if item.image:
            res['image'] = self.getImageScale(item)
        return res
