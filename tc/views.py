import re
import mapscript
import TileCache.Layers.MapServer as MS

from django.http import HttpResponse, Http404
from django.shortcuts import render
from TileCache.Service import Service, Request, TileCacheException
from TileCache.Caches.Disk import Disk
from tc.shortcuts import render_tile

import logging

from django.http import HttpResponse

class TileResponse(object):
    def __init__(self, tile_bytes):
        self.tile_bytes = tile_bytes
  
    def __call__(self, extension='png'):
        if self.tile_bytes:
            return HttpResponse(self.tile_bytes, content_type=('image/%s' % extension))
        else:
            raise Http404

def get_tile(request, version, layername, z, x, y, extension='png'):
    'Returns a map tile in the requested format'
    z, x, y = int(z), int(x), int(y)
    response = TileResponse(render_tile(layername, z, x, y, extension=extension))
    return response(extension)
    