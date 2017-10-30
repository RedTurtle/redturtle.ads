# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from redturtle.ads import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IExpirationDaysBehavior(model.Schema):
    """Behavior interface to set expiration days for advertisements.
    """

    expiration_days = schema.Int(
        title=_(
            "expiration_days_label",
            default=u"Advertisements expiration days"),
        description=_(
            "expiration_days_help",
            default=u"Set how many days the ads should be visible before"
                    u" expire. Set 0 to keep them always visible."),
        default=30,
        required=False,
        )
