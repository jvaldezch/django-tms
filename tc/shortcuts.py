from django.conf import settings
from TileCache.Service import Service
from TileCache.Layer import Tile
import TileCache.Layers.MapServer as MS
import TileCache.Layers.WMS as WMS
from TileCache.Caches.Disk import Disk
from django.contrib.gis.gdal import SpatialReference
  
def get_eb_layer(name):
    # svc = Service.load(settings.TILECACHE_CONFIG)
    mapfile = r"/data/oceancolor/terra/L3m/2017/001/T2017001_L3m_DAY_NSST_sst_4km.map"
    svc = Service(
        Disk('/tmp/somecache'),  # See "Cache Invalidation", below
        { 
            "raster": MS.MapServer("basic", mapfile, layers="raster", srs='EPSG:4326', debug=False),
        }
    ) 
    '''
    svc = Service(
        Disk('/tmp/somecache'),  # See "Cache Invalidation", below
        { 
            "raster": WMS.WMS("basic", r"http://localhost/cgi-bin/mapserv.cgi?map=/data/oceancolor/aqua/L3m/2017/001/A2017001.L3m_DAY_SST_sst_4km.map&mode=map&layer=raster", srs='EPSG:4326', width='256', height='256'),
        }
    )
    '''
    return svc.layers[name]
  
def render_tile(name, z, x, y, extension='png', source_srs=None, dest_srs=None, bbox=None, scales=None, units=None):
    """
    A shortcut for rendering a map tile using the EveryBlock settings.
  
    Useful for views and for rendering scripts. Main config options can be
    overriden.
    """
    layer = get_eb_layer(name)
    if source_srs is not None:
        layer.source_srs = source_srs
    if dest_srs is not None:
        layer.dest_srs = dest_srs
    if bbox is not None:
        layer.set_bbox(bbox)
    if scales is not None:
        layer.set_resolutions(scales, units)
    layer.extension = extension
    tile = Tile(layer, x, y, z)
    return layer.renderTile(tile)
  