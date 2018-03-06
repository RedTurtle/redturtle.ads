# -*- coding: utf-8 -*-
from Acquisition import aq_base
from Acquisition.interfaces import IAcquirer
from plone.app.uuid.utils import uuidToObject
from plone.dexterity.interfaces import IDexterityFTI
from plone.dexterity.utils import addContentToContainer
from redturtle.ads import _
from redturtle.ads.interfaces import IAdvertisement
from redturtle.ads.interfaces import IRedturtleAdvBehavior
from z3c.form import button
from z3c.form import form
from z3c.form.field import Fields
from zope import schema
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile as Z3VPTF  # noqa
from zope.component import createObject
from zope.component import getUtility
from zope.dottedname.resolve import resolve
from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent
from zope.schema import getFieldsInOrder


class CreateAdv(form.AddForm):

    ignoreContext = True
    label = _("add_adv_label", default=u"Create a new Adv")
    portal_type = 'Advertisement'
    iface = IAdvertisement

    @property
    def fields(self):
        """
        Advertisement schema is based on IAdvertisement
        and different plone behavior.
        Base schema class right now it's empty. We want to return base behavior
        and variuos specific ones.
        Base ones are:
            * plone.app.dexterity.behaviors.metadata.IDublinCore
            * plone.app.contenttypes.behaviors.richtext.IRichText
            * plone.app.contenttypes.behaviors.leadimage.ILeadImage
        Specific ones are:
            * redturtle.ads.behaviors.price.IPriceBehavior
            * redturtle.ads.behaviors.external_link.IExternalLinkBehavior
        we try to take directly specific ones and filter other ones by a marker
        interface
        """
        # these are the wanted behavior
        wanted = [
            'plone.app.dexterity.behaviors.metadata.IDublinCore',
            'plone.app.contenttypes.behaviors.richtext.IRichText',
            'plone.app.contenttypes.behaviors.leadimage.ILeadImage',
        ]
        # these are the fields we want to ignore in the add popup form per
        # behavior
        blacklisted_fields = {
            'plone.app.dexterity.behaviors.metadata.IDublinCore': ['subjects',
                                                                   'language',
                                                                   'effective',
                                                                   'expires',
                                                                   'creators',
                                                                   'contributors',  # noqa
                                                                   'rights'],
        }

        # this will contain the list of all the field we want

        ads_category = schema.Choice(
            __name__='ads_category',
            title=_(u'ads_category_title', default=u'Category'),
            vocabulary='redturtle.ads.vocabularies.categories',
            required=True,
            missing_value='',
        )

        help_text = self.context.get_ads_help_text().decode('utf-8')
        ads_help_text = schema.Text(
            __name__='helptext',
            title=u'',
            required=False,
            default=help_text
        )
        privacy_text = self.context.get_privacy_text().decode('utf-8')
        ads_privacy_text = schema.Text(
            __name__='privacytext',
            title=u'',
            required=False,
            default=privacy_text
        )

        fields_list = [ads_help_text, ads_category]

        for behavior in self.context.portal_types[self.portal_type].behaviors:

            # add at the list all the fields taken from the base behavior
            iface = resolve(behavior)
            if behavior in wanted:
                for b_field_name, b_fieldobj in getFieldsInOrder(iface):
                    if behavior not in blacklisted_fields or\
                            b_field_name not in blacklisted_fields[behavior]:
                        fields_list.append(b_fieldobj)

            elif IRedturtleAdvBehavior.implementedBy(iface):
                for b_field_name, b_fieldobj in getFieldsInOrder(iface):
                    fields_list.append(b_fieldobj)

            else:
                continue

        # add at the list all the fields taken from the base schema
        for field_name, fieldobj in getFieldsInOrder(self.iface):
            fields_list.append(fieldobj)

        fields_list.append(ads_privacy_text)
        return Fields(*fields_list)

        # fields['ads_category'].widgetFactory = SelectFieldWidget  # noqa

    def updateWidgets(self):
        super(CreateAdv, self).updateWidgets()
        self.widgets['helptext'].template = Z3VPTF('templates/customtext.pt')  # noqa
        self.widgets['privacytext'].template = Z3VPTF('templates/customtext.pt')  # noqa



    @button.buttonAndHandler(_('Add'), name='add')
    def handleAdd(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True

    def createAndAdd(self, data):
        obj = self.create(data)
        notify(ObjectCreatedEvent(obj))
        self.add(obj, data)
        return obj

    def create(self, data):
        fti = getUtility(IDexterityFTI, name=self.portal_type)

        container = uuidToObject(data['ads_category'])
        content = createObject(fti.factory)

        # Note: The factory may have done this already, but we want to be sure
        # that the created type has the right portal type. It is possible
        # to re-define a type through the web that uses the factory from an
        # existing type, but wants a unique portal_type!

        if hasattr(content, '_setPortalTypeName'):
            content._setPortalTypeName(fti.getId())

        # Acquisition wrap temporarily to satisfy things like vocabularies
        # depending on tools
        if IAcquirer.providedBy(content):
            content = content.__of__(container)

        form.applyChanges(self, content, data)
        # useless
        # for group in self.groups:
        #     form.applyChanges(group, content, data)

        return aq_base(content)

    def add(self, object, data):
        fti = getUtility(IDexterityFTI, name=self.portal_type)
        container = uuidToObject(data['ads_category'])
        new_object = addContentToContainer(container, object)

        if fti.immediate_view:
            self.immediate_view = "/".join(
                [container.absolute_url(), new_object.id, fti.immediate_view]
            )
        else:
            self.immediate_view = "/".join(
                [container.absolute_url(), new_object.id]
            )

    def nextURL(self):
        if self.immediate_view is not None:
            return self.immediate_view
        else:
            return self.context.absolute_url()
