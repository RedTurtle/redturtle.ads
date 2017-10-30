# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.app.textfield import RichText
from plone.supermodel import model
from redturtle.ads import _
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IRedturtleAdsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IBulletinBoard(model.Schema):

    presentation_text = RichText(
        title=_(
            'presentation_text_label',
            default=u'Presentation text'),
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html', 'text/plain',),
        default=u''
    )

    ads_help_text = RichText(
        title=_(
            'ads_help_text_label',
            default=u'Advertisement help text'),
        description=_(
            'ads_help_text_help',
            default=u'Insert some help text that will be rendered when an user'
                    ' creates a new advertisement.'),
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html', 'text/plain',),
        default=u''
    )

    privacy_text = RichText(
        title=_(
            'privacy_text_label',
            default=u'Privacy text'),
        description=_(
            'privacy_text_help',
            default=u'Insert a privacy policy text that will be rendered when'
                    ' an user creates a new advertisement.'),
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html', 'text/plain',),
        default=u''
    )


class IAdsCategory(model.Schema):
    """
    """


class IAdvertisement(model.Schema):
    """ """


class IRedturtleAdvBehavior(Interface):
    """
    Marker interface for redturtle adv behavior
    """
