#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from caldav.lib.namespace import ns
from .base import BaseElement, ValuedBaseElement


## Operations
class Propfind(BaseElement):
    tag = ns("D", "propfind")


class PropertyUpdate(BaseElement):
    tag = ns("D", "propertyupdate")


class Mkcol(BaseElement):
    tag = ns("D", "mkcol")

## Filters

## Conditions

## Components / Data


class Prop(BaseElement):
    tag = ns("D", "prop")


class Collection(BaseElement):
    tag = ns("D", "collection")


class Set(BaseElement):
    tag = ns("D", "set")


## Properties
class ResourceType(BaseElement):
    tag = ns("D", "resourcetype")


class DisplayName(ValuedBaseElement):
    tag = ns("D", "displayname")


class Href(BaseElement):
    tag = ns("D", "href")


class Response(BaseElement):
    tag = ns("D", "response")


class Status(BaseElement):
    tag = ns("D", "status")


class Getetag(BaseElement):
    tag = ns("D", "getetag")


class CurrentUserPrincipal(BaseElement):
    tag = ns("D", "current-user-principal")


class Owner(BaseElement):
    tag = ns("D", "owner")


class PrincipalURL(BaseElement):
    tag = ns("D", "principal-URL")


class CurrentUserPrivilegeSet(BaseElement):
    tag = ns("D", "current-user-privilege-set")

    @staticmethod
    def convert(element):
        result = []
        for item in element.findall('a:privilege', namespaces={'a': 'DAV:'}):
            result.append(item.find('./*').tag)

        return result
