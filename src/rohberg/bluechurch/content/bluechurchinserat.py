# coding: utf-8
from zope import schema
from zope.interface import implements
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform.directives import widget
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.interface import implementer

from rohberg.bluechurch.content.interfaces import IBluechurchMemberContent

import logging
logger = logging.getLogger(__name__)

from rohberg.bluechurch import _

class IBluechurchinserat(model.Schema):
    """ Marker interface for Bluechurchinserat
    """
        
    model.load('bluechurchinserat.xml')

@implementer(IBluechurchinserat)
class Bluechurchinserat(Item):
    """
    """
    implements(IBluechurchMemberContent)