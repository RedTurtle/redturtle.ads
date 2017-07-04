# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.dexterity.content import Container


class BulletinBoard(Container):
    """
    A bulletin board
    """

    def get_bullettin_board(self):
        return aq_inner(self)

    def get_ads_help_text(self):
        text = aq_inner(self).ads_help_text
        if text:
            return text.output

    def get_privacy_text(self):
        text = aq_inner(self).privacy_text
        if text:
            return text.output


class AdsCategory(Container):
    """
    An advertisement category
    """


class Advertisement(Container):
    """
    An advertisement
    """
