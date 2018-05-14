# -*- coding: utf-8 -*-
from plone.dexterity.browser import edit
from redturtle.ads import _
from redturtle.ads.interfaces import IAdvertisement
from redturtle.ads.interfaces import IRedturtleAdvBehavior
from z3c.form.field import Fields
from zope import schema
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile as Z3VPTF  # noqa
from zope.dottedname.resolve import resolve
from zope.schema import getFieldsInOrder


class EditAdv(edit.DefaultEditForm):

    label = _('edit_adv_label', default=u'Modifica un Adv')
    fields = IAdvertisement

    # def getFields(self):
    #     """
    #     Advertisement schema is based on IAdvertisement
    #     and different plone behavior.
    #     Base schema class right now it's empty. We want to return base behavior
    #     and variuos specific ones.
    #     Base ones are:
    #         * plone.app.dexterity.behaviors.metadata.IDublinCore
    #         * plone.app.contenttypes.behaviors.richtext.IRichText
    #         * plone.app.contenttypes.behaviors.leadimage.ILeadImage
    #     Specific ones are:
    #         * redturtle.ads.behaviors.price.IPriceBehavior
    #         * redturtle.ads.behaviors.external_link.IExternalLinkBehavior
    #     we try to take directly specific ones and filter other ones by a marker
    #     interface
    #     """
    #     # these are the wanted behavior
    #     wanted = [
    #         'plone.app.dexterity.behaviors.metadata.IDublinCore',
    #         'plone.app.contenttypes.behaviors.richtext.IRichText',
    #         'plone.app.contenttypes.behaviors.leadimage.ILeadImage',
    #     ]
    #     # these are the fields we want to ignore in the add popup form per
    #     # behavior
    #     blacklisted_fields = {
    #         'plone.app.dexterity.behaviors.metadata.IDublinCore': ['subjects',
    #                                                                'language',
    #                                                                'effective',
    #                                                                'expires',
    #                                                                'creators',
    #                                                                'contributors',  # noqa
    #                                                                'rights'],
    #     }
    #
    #     # this will contain the list of all the field we want
    #
    #     ads_category = schema.Choice(
    #         __name__='ads_category',
    #         title=_(u'ads_category_title', default=u'Category'),
    #         vocabulary='redturtle.ads.vocabularies.categories',
    #         required=True,
    #         missing_value='',
    #     )
    #
    #     help_text = self.context.get_ads_help_text().decode('utf-8')
    #     ads_help_text = schema.Text(
    #         __name__='helptext',
    #         title=u'',
    #         required=False,
    #         default=help_text
    #     )
    #     privacy_text = self.context.get_privacy_text().decode('utf-8')
    #     ads_privacy_text = schema.Text(
    #         __name__='privacytext',
    #         title=u'',
    #         required=False,
    #         default=privacy_text
    #     )
    #
    #     fields_list = [ads_help_text, ads_category]
    #
    #     for behavior in self.context.portal_types[self.portal_type].behaviors:
    #
    #         # add at the list all the fields taken from the base behavior
    #         iface = resolve(behavior)
    #         if behavior in wanted:
    #             for b_field_name, b_fieldobj in getFieldsInOrder(iface):
    #                 if behavior not in blacklisted_fields or\
    #                         b_field_name not in blacklisted_fields[behavior]:
    #                     fields_list.append(b_fieldobj)
    #
    #         elif IRedturtleAdvBehavior.implementedBy(iface):
    #             for b_field_name, b_fieldobj in getFieldsInOrder(iface):
    #                 fields_list.append(b_fieldobj)
    #
    #         else:
    #             continue
    #
    #     # add at the list all the fields taken from the base schema
    #     for field_name, fieldobj in getFieldsInOrder(self.iface):
    #         fields_list.append(fieldobj)
    #
    #     fields_list.append(ads_privacy_text)
    #
    #     fields_list = filter(lambda x: self.filter_fields(x), fields_list)
    #     return fields_list
    #
    # def filter_fields(self, field):
    #     if field.__doc__ == u'label_leadimage_caption':
    #         return False
    #     return True
    #
    # @property
    # def iface(self):
    #     bb = self.context.get_bullettin_board()
    #     return resolve(self.context.portal_types[bb.select_type].schema)
    #
    # @property
    # def fields(self):
    #     fields_list = self.getFields()
    #     return Fields(*fields_list)

    def updateWidgets(self):
        super(EditAdv, self).updateWidgets()
        self.fields['ILeadImage.image'].field.title = u'Foto'
        self.fields['ILeadImage.image'].field.description = u'foto/immagine dell\'annuncio'  # noqa

    def updateFields(self):
        super(EditAdv, self).updateFields()


class EditView(edit.DefaultEditView):
    form = EditAdv
