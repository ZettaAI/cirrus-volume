'''
graphene.py

A wrapper for CloudVolumeGraphene
NOT IMPLEMENTED YET
'''
import warnings
from typing import Optional, List, TypeVar

from . import rules
from .volume import register_plugin

from cloudvolume.frontends.graphene import CloudVolumeGraphene


CloudVolume = TypeVar('CloudVolume')
Process = TypeVar('Process')


def register():
    register_plugin(CloudVolumeGraphene, CirrusVolumeGraphene)


class CirrusVolumeGraphene(CloudVolumeGraphene):

    def __new__(self,
                cloudvolume: CloudVolume,
                sources: Optional[List[str]] = None,
                motivation: Optional[str] = None,
                process: Optional[Process] = None
                ):
        warnings.warn("CirrusVolumeGraphene not implemented yet!"
                      " Passing you a normal CloudVolumeGraphene")
        return cloudvolume
