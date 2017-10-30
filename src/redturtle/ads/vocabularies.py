# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class CategoriesVocabulary(object):
    implements(IVocabularyFactory)

    # This vocabulary should be always called in the root of a board.
    # so categories should be directly his children

    def __call__(self, context):
        categories = context.values()
        sorted(categories, key=lambda x: x.title)
        if not categories:
            return SimpleVocabulary([])
        terms = map(
            lambda x: SimpleVocabulary.createTerm(x.UID(), x.UID(), x.title),
            categories)
        terms.insert(0, SimpleVocabulary.createTerm('', '', '-- no value --'))
        return SimpleVocabulary(terms)


CategoriesVocabularyFactory = CategoriesVocabulary()
