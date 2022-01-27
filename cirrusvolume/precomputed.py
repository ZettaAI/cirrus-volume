'''
precomputed.py

A wrapper for CloudVolumePrecomputed
'''
from typing import Optional, List, TypeVar

from cloudvolume.frontends.precomputed import CloudVolumePrecomputed

from . import rules
from .volume import register_plugin


CloudVolume = TypeVar('CloudVolume')
Process = TypeVar('Process')


def register():
    register_plugin(CloudVolumePrecomputed, CirrusVolumePrecomputed)


class CirrusVolumePrecomputed(CloudVolumePrecomputed):

    def __init__(self,
                 cloudvolume: CloudVolume,
                 sources: Optional[List[str]] = None,
                 motivation: Optional[str] = None,
                 process: Optional[Process] = None
                 ):
        # Copying the CloudVolume attributes
        self.config = cloudvolume.config
        self.cache = cloudvolume.cache
        self.meta = cloudvolume.meta

        self.image = cloudvolume.image
        self.mesh = cloudvolume.mesh
        self.skeleton = cloudvolume.skeleton

        self.green_threads = cloudvolume.green_threads

        self.mip = cloudvolume.mip
        self.pid = cloudvolume.pid

        # CirrusVolume-specific atrributes
        self.sources = sources
        self.motivation = motivation
        self.process = process

    # Overriding all methods that allow writing to the image
    def __setitem__(self, slices, img):
        rules.check_writing_rules(self.sources, self.motivation, self.process)

        rules.documentvolume(self, self.sources,
                             self.motivation, self.process)

        super().__setitem__(self, slices, img)

    def upload_from_shared_memory(self,
                                  location,
                                  bbox,
                                  order='F',
                                  cutout_bbox=None) -> None:
        rules.check_writing_rules(self.sources, self.motivation, self.process)

        rules.documentvolume(self, self.sources,
                             self.motivation, self.process)

        super().upload_from_shared_memory(self, location, bbox,
                                          order=order, cutout_bbox=cutout_bbox)

    def upload_from_file(self,
                         location, bbox, order='F', cutout_bbox=None) -> None:
        rules.check_writing_rules(self.sources, self.motivation, self.process)

        rules.documentvolume(self, self.sources,
                             self.motivation, self.process)

        super().upload_from_file(self, location, bbox,
                                 order=order, cutout_bbox=cutout_bbox)
