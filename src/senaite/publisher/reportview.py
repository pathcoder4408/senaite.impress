# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.PUBLISHER
#
# Copyright 2018 by it's authors.

from senaite.publisher.interfaces import IReportView
from zope.interface import implements


class ReportView(object):
    """Generic Report View

    Note: This is also the base class for the Multi Report View
    """
    implements(IReportView)

    def __init__(self, model):
        self.model = model
        self.context = model.instance

    def render(self, template):
        raise NotImplemented("Must be implemented by subclass")
