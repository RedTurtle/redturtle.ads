# -*- coding: utf-8 -*-
from Products.CMFPlone.resources import add_resource_on_request
from plone import api
from redturtle.ads.browser.helpers_view import HelpersView
from plone.dexterity.browser.edit import DefaultEditForm as BaseEdit
from plone.dexterity.browser.add import DefaultAddForm as BaseAddForm
from plone.dexterity.browser.add import DefaultAddView as BaseAddView

from zope.interface import classImplements
from plone.dexterity.interfaces import IDexterityEditForm
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile as Z3VPTF
from plone.z3cform import layout
from z3c.form.field import Fields
import zope


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


class BaseAdvertisementForm(object):

    def add_fields(self):
        help_text = self.context.get_ads_help_text().decode('utf-8')
        ads_help_text = zope.schema.Text(
            __name__='helptext',
            title=u'',
            required=False,
            default=help_text
        )
        privacy_text = self.context.get_privacy_text().decode('utf-8')
        ads_privacy_text = zope.schema.Text(
            __name__='privacytext',
            title=u'',
            required=False,
            default=privacy_text
        )
        self.fields += Fields(ads_privacy_text)
        self.fields += Fields(ads_help_text)
        self.fields._data_values.insert(0, self.fields._data_values.pop())

    def change_widget(self):
        template = 'templates/customtext.pt'
        self.widgets['helptext'].template = Z3VPTF(template)
        self.widgets['privacytext'].template = Z3VPTF(template)


class DefaultEditForm(BaseEdit, BaseAdvertisementForm):
    """
    """
    def updateWidgets(self):
        self.add_fields()
        super(DefaultEditForm, self).updateWidgets()
        self.change_widget()


DefaultEditView = layout.wrap_form(DefaultEditForm)
classImplements(DefaultEditView, IDexterityEditForm)


class DefaultAddForm(BaseAddForm, BaseAdvertisementForm):
    """
    """
    def updateWidgets(self):
        self.add_fields()
        super(DefaultAddForm, self).updateWidgets()
        self.change_widget()


class DefaultAddView(BaseAddView):

    form = DefaultAddForm
