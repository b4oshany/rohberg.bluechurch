# coding: utf-8

from zope.component import getUtility
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer


# def BluchurchTagsVocabularyFactory(context=None):
#     terms = []
#     terms.append(SimpleVocabulary.createTerm("kinder", "kinder", u"Kinder"))
#     terms.append(SimpleVocabulary.createTerm("madchen", "madchen", u"Mädchen"))
#     terms.append(SimpleVocabulary.createTerm("senioren", "senioren", u"Senioren"))
#     return SimpleVocabulary(terms)

def BluchurchTagsVocabularyFactory(context=None):
    normalizer = getUtility(IIDNormalizer)
    
    terms = []
    tags = api.portal.get_registry_record('bluechurch.bluechurchtags')
    # json.dumps(channels)
    for tag in tags:
        tag_lower = normalizer.normalize(tag)
        terms.append(SimpleVocabulary.createTerm(tag_lower, tag_lower, tag))
    return SimpleVocabulary(terms)
