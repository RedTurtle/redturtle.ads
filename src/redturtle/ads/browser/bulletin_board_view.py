# -*- coding: utf-8 -*-
from Products.CMFPlone.resources import add_resource_on_request
from redturtle.ads.browser.helpers_view import HelpersView


class BulletinBoardView(HelpersView):
    '''
    View for a Bulletin Board
    '''

    def __call__(self):
        # utility function to add resource to rendered page
        add_resource_on_request(self.request, 'ads_layout')
        return super(BulletinBoardView, self).__call__()
