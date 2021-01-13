# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory

import get_streams


ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()


@plugin.route('/')
def index():
    for stream in get_streams.get_all():
        addDirectoryItem(plugin.handle, stream["high"], ListItem(stream["name"]))
    endOfDirectory(plugin.handle)

def run():
    plugin.run()
