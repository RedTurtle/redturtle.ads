# -*- coding: utf-8 -*-
from redturtle.ads import _
from zope.i18n import translate
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class CategoriesVocabulary(object):
    implements(IVocabularyFactory)

    # This vocabulary should be always called in the root of a board.
    # so categories should be directly his children

    def __call__(self, context):

        for el in context.aq_chain:
            if el.portal_type == 'BulletinBoard':
                context = el
                break

        categories = context.values()
        sorted(categories, key=lambda x: x.title)
        if not categories:
            return SimpleVocabulary([])
        terms = map(
            lambda x: SimpleVocabulary.createTerm(x.UID(), x.UID(), x.title),
            categories)
        no_value_label = translate(
            _('no_value_label', default=u"-- no value --"),
            context=context.REQUEST)
        terms.insert(0, SimpleVocabulary.createTerm('', '', no_value_label))
        return SimpleVocabulary(terms)


CategoriesVocabularyFactory = CategoriesVocabulary()
