# -*- coding: utf-8 -*-
from plone.app.contenttypes import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IAdditionalImage(model.Schema):

    additionalimage = namedfile.NamedBlobImage(
        title=_(u'label_additionalimage',
                default=u'Additional image'),
        description=u'',
        required=False,
    )


@implementer(IAdditionalImage)
@adapter(IDexterityContent)
class AdditionalImage(object):

    def __init__(self, context):
        self.context = context
