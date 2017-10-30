# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from redturtle.ads import _
from redturtle.ads.interfaces import IRedturtleAdvBehavior
from zope import schema
from zope.interface import implementer
from zope.interface import provider


@implementer(IRedturtleAdvBehavior)
@provider(IFormFieldProvider)
class IExternalLinkBehavior(model.Schema):
    """Behavior interface to set a recipient email for notifications.
    """

    external_link = schema.URI(
        title=_(
            "external_link_label",
            default=u"External link"),
        description=_(
            "external_link_help",
            default=u"If this advertisement is already published on another"
                    " site, insert the link here."),
        required=False,
        )
