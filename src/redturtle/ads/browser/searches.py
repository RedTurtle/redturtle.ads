# -*- coding: utf-8 -*-
# from Products.CMFPlone.resources import add_resource_on_request
# from Products.Five.browser import BrowserView
from plone import api
import json
from redturtle.ads.browser.helpers_view import HelpersView
from plone.app.contentlisting.interfaces import IContentListing
from Products.CMFPlone.PloneBatch import Batch
# from plone.app.uuid.utils import uuidToObject


class SearchCategories(HelpersView):
    '''
    view that return categories
    '''

    def __call__(self):
        '''
        return the categories list
        '''
        query = {
            'portal_type': 'AdsCategory',
            'sort_on': 'sortable_title',
        }
        results = api.content.find(**query)
        json_result = map(self.formatResponse, results)
        self.request.response.setHeader("Content-type", "application/json")
        self.request.response.setHeader("Access-Control-Allow-Origin", "*")
        json_result.insert(0, {'id': '',
                               'path': '',
                               'title': '-- select category --'})
        return json.dumps(json_result)

    def formatResponse(self, brain):
        """
        jsonify categories informations
        """
        return {
            'title': brain.Title,
            'id': brain.getId,
            'path': brain.getPath()
        }


class View(HelpersView):
    '''
    View for an Advertisement
    '''

    def __call__(self):
        b_size = self.request.form.get('b_size', 2)
        b_start = self.request.form.get('b_start', 0)
        if not isinstance(b_start, int):
            b_start = int(b_start)
        query = {
            'portal_type': 'Advertisement',
            'sort_on': self.request.form.get('sort_on', 'effective'),
            'sort_order': self.request.form.get('sort_order', 'reverse'),
        }

        searchableText = self.request.form.get('q')
        path = self.request.form.get('path')
        if searchableText:
            query['SearchableText'] = searchableText
        if path:
            query['path'] = path
        results = api.content.find(**query)
        results = IContentListing(results)

        results = Batch(results, b_size, b_start)

        json_result = self.formatResponse(results)
        self.request.response.setHeader("Content-type", "application/json")
        self.request.response.setHeader("Access-Control-Allow-Origin", "*")
        return json.dumps(json_result)

    def formatResponse(self, results):
        portal_url = api.portal.get().absolute_url()
        base_url = "{}/search_advertisements".format(portal_url)
        nexturls = results.has_next and results.nexturls({})[0] or []
        prevurls = results.has_previous and results.prevurls({})[0] or []
        return {
            'data': map(self.formatAnnouncement, results),
            'meta': {
                'hasPrevious': results.has_previous,
                'hasNext': results.has_next,
                'totalPages': results.numpages,
                'pageSize': results.pagesize,
                'pageNumber': results.pagenumber,
                'restultsLen': results.sequence_length
            },
            'links': {
                'self': '{}?{}'.format(base_url, results.pageurl({})),
                'first': '{}?b_start:int=0'.format(base_url),
                'next': nexturls and '{}?{}'.format(base_url,
                                                    nexturls[1]) or '',
                'prev': prevurls and '{}?{}'.format(base_url,
                                                    prevurls[1]) or '',
                'last': '{}?b_start:int={}'.format(base_url, results.last),
            }
        }

    def formatAnnouncement(self, brain):
        item = brain.getObject()
        res = {
            'title': item.Title(),
            'id': item.getId(),
            'description': item.Description(),
            'url': item.absolute_url(),
            'price': item.price,
            'category': self.getCategory(item),
            'date': self.getFormattedDate(item.Date())
        }
        if item.image and self.getImageScale(item):
            res['image_src'] = "{}/images/image/thumb".format(
                item.absolute_url())
        return res


class TranslateString(HelpersView):

    def __call__(self):
        """
        return translations
        """
        def translate(key):
            return self.context.translate(key,
                                          domain='redturtle.ads',
                                          context=self.context),
        return json.dumps({
            'search': translate('search'),
            'next': translate('next'),
            'prev': translate('prev'),
        })
