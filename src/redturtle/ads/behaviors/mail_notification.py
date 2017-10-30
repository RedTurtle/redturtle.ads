# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from redturtle.ads import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IRecipientEmailBehavior(model.Schema):
    """Behavior interface to set a recipient email for notifications.
    """

    recipient_email = schema.TextLine(
        title=_(
            "recipient_email_label",
            default=u"Recipient email"),
        description=_(
            "recipient_email_help",
            default=u"Insert an email address that will be notified for every"
                    u" new advertisement."),
        default=u'',
        required=False,
        )
