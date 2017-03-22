# -*- coding: utf-8 -*-
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from plone import api
from redturtle.ads.browser.helpers_view import HelpersView

class AdvertisementView(HelpersView):
    '''
    View for an Announcement
    '''

    def __call__(self):
        # utility function to add resource to rendered page
        add_resource_on_request(self.request, 'ads_layout')
        return super(AdvertisementView, self).__call__()

    def getPrincipalImage(self):
        image = self.context.image
        if not image:
            return ""
        return self.getImageScale(self.context, miniature="mini")

    def getAdditionalImages(self):
        images = self.context.listFolderContents(
            contentFilter={"portal_type": "Image"})
        return map(self.getImageScale, images)

    def extractAdsCategories(self, ads):
        results = []
        for brain in ads:
            advertisement = brain.getObject()
            category = self.getCategory(advertisement)
            if category not in results:
                results.append(category)
        return results

    def getAuthorInfos(self):
        creator_id = self.context.Creator()
        creator = api.user.get(username=creator_id)
        other_advertisements = api.content.find(
            portal_type="Advertisement",
            Creator=creator_id
        )
        return {
            "creator": {
                'id': creator_id,
                'fullname': creator.getProperty('fullname') or creator_id
            },
            "advertisements": other_advertisements.actual_result_count,
            "categories": self.extractAdsCategories(other_advertisements)
        }
