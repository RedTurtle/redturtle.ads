# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from redturtle.ads import _
from zope import schema
from zope.interface import provider, implementer, implements
from redturtle.ads.interfaces import IRedturtleAdvBehavior


@implementer(IRedturtleAdvBehavior)
@provider(IFormFieldProvider)
class IPriceBehavior(model.Schema):
    """Behavior interface to set a recipient email for notifications.
    """

    price = schema.TextLine(
        title=_(
            "price_label",
            default=u"Price"),
        description=_(
            "price_help",
            default=u"Insert the wanted price. Leave blank if the price is"
                    " already described above."),
        default=u'',
        required=False,
        )
