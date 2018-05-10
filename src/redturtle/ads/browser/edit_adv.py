# -*- coding: utf-8 -*-
from plone.dexterity.browser import edit
from redturtle.ads import _
from redturtle.ads.interfaces import IAdvertisement
from z3c.form.interfaces import HIDDEN_MODE
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile as Z3VPTF  # noqa


class EditAdv(edit.DefaultEditForm):

    label = _('edit_adv_label', default=u'Modifica un Adv')
    fields = IAdvertisement

    def updateWidgets(self):
        super(EditAdv, self).updateWidgets()
        self.fields['ILeadImage.image'].field.title = u'Foto'
        self.fields['ILeadImage.image'].field.description = u'foto/immagine dell\'annuncio'  # noqa

    def updateFields(self):
        super(EditAdv, self).updateFields()
        self.fields['ILeadImage.image_caption'].mode = HIDDEN_MODE


class EditView(edit.DefaultEditView):
    form = EditAdv
