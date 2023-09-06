"""
attrdict contains several mapping objects that allow access to their
keys as attributes.
"""
from tronapi.attrdict.mapping import AttrMap
from tronapi.attrdict.dictionary import AttrDict
from tronapi.attrdict.default import AttrDefault


__all__ = ['AttrMap', 'AttrDict', 'AttrDefault']
