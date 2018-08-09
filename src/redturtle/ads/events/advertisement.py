# -*- coding: utf-8 -*-
from DateTime import DateTime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces.controlpanel import IMailSchema
from Products.CMFPlone.utils import safe_hasattr
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from redturtle.ads import _
from zope.component import getUtility
from zope.i18n import translate

import logging


logger = logging.getLogger(__name__)


def send_email(emails, message_text, subject, sender=None):

    if not sender:
        # get from the site
        registry = getUtility(IRegistry)
        mail_settings = registry.forInterface(IMailSchema, prefix='plone')
        sender = mail_settings.email_from_address

    if not sender:
        api.portal.show_message(
            translate(_('no_sender_mail',
                        default='No mail sender found;'
                                ' the mail will not be sent.')),
            type='warning',
            request=api.portal.get().REQUEST
        )
        return ''
    for email in emails:
        message = MIMEMultipart()
        message.attach(MIMEText(message_text, 'html', 'utf-8'))
        api.portal.send_email(
            recipient=email,
            sender=sender,
            subject=subject,
            body=message
        )


def send_email_on_publish(advertisement):
    creator = api.user.get(username=advertisement.Creator())
    creator_email = api.user.get(
        username=advertisement.Creator()).getProperty('email', None)
    if not creator_email:
        logger.warning(
            'Publish mail not send to {0}. The user has no email set.'.format(
                advertisement.Creator()
            )
        )
        return
    emails = [creator_email, ]
    options = {
        'msg1': translate(
            _(u'Dear ${fullname}',
                mapping={'fullname': creator.getProperty('fullname').decode('utf-8')}),  # noqa
                context=advertisement.REQUEST),
        'msg2': translate(_('Your advertisement ${adv_title} has been'
                            'published.',
                            mapping={'adv_title': advertisement.title}),
                          context=advertisement.REQUEST),
        'msg3': translate(_('You can see it here:'),
                          context=advertisement.REQUEST),
        'msg4': translate(
            _(
                u'According to actual site policy, the advertisement will be visible since ${expiration_date}',  # noqa
                mapping={'expiration_date': advertisement.expiration_date.strftime('%Y/%m/%d')},  # noqa
                default=u''
            ),
            context=advertisement.REQUEST),
        'msg5': translate(_('Best regards'), context=advertisement.REQUEST),
        'adv_url': advertisement.absolute_url(),
        'adv_title': advertisement.title,
        'expiration_date': advertisement.expiration_date
    }
    message_text = ViewPageTemplateFile('adv_published.pt')
    view = advertisement.restrictedTraverse('@@view')
    send_email(emails,
               message_text(view, **options),
               translate(_('subj_mail_published',
                           default=u'Advertisement published'),
                         context=advertisement.REQUEST))


def set_expiration_date(advertisement, event):
    portal_workflow = api.portal.get_tool('portal_workflow')
    adv_state = portal_workflow.getInfoFor(advertisement, 'review_state')

    if adv_state != 'published':
        return

    bullettin_board = advertisement.get_bullettin_board()

    expiration_days = safe_hasattr(bullettin_board, 'expiration_days') and\
        bullettin_board.expiration_days

    if not expiration_days:
        return

    advertisement.expiration_date = DateTime() + expiration_days
    advertisement.reindexObject()
    send_email_on_publish(advertisement)


def send_email_on_creation(advertisement, recipient):
    creator = api.user.get(username=advertisement.Creator())
    emails = [recipient, ]
    options = {
        'msg1': translate(
            _(
                u'The user ${fullname}',
                mapping={'fullname': u'{0} ({1})'.format(
                    creator.getProperty('fullname').decode('utf-8'),
                    creator.getProperty('email')
                )
            }),  # noqa
            context=advertisement.REQUEST),
        'msg2': translate(
            _('Has submitted a new advertisement. Please evaluate'
              ' his content and eventually publish it.'),
            context=advertisement.REQUEST),
        'msg3': translate(_('You can see it here:'),
                          context=advertisement.REQUEST),
        'adv_url': advertisement.absolute_url(),
        'adv_title': advertisement.title,
    }
    message_text = ViewPageTemplateFile('adv_created.pt')
    view = advertisement.restrictedTraverse('@@view')

    send_email(emails,
               message_text(view, **options),
               translate(_('subj_mail_created',
                           default=u'Advertisement created'),
                         context=advertisement.REQUEST))


def initialize_advertisement(advertisement, event):
    # portal_workflow = api.portal.get_tool('portal_workflow')
    # portal_workflow.doActionFor(advertisement, 'submit')
    bullettin_board = advertisement.get_bullettin_board()

    recipient = bullettin_board.recipient_email
    if not recipient:
        return

    send_email_on_creation(advertisement, recipient)
