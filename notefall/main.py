import os, sys, logging, argparse

import pygame
import thorpy

import notefall
import notefall.frontend
import notefall.vfs as vfs
import notefall.beatmap as beatmap
import notefall.game as game
import notefall.util

from notefall import _config as config

NAME = "notefall"
VERSION = "0.0.01-Alpha"

gamedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
userdir = os.path.abspath(os.path.join(os.path.expanduser("~"), ".notefall"))
globArgs = None
frontend = None
log = logging.getLogger(__name__)

def userDirInit():
    if not os.path.exists(userdir):
        os.makedirs(userdir)
        
def vfsInit():
    vfs.root.clear()
    
    if globArgs.no_vfs:
        return
        
    vfs.applySettings()
    
    def initroot(root=vfs.root):
        root.loadDataDirs(basedir, userdir, *globArgs.extradirs)
        
        for pack in globArgs.extrapacks:
            root.loadPack(pack)
            
        return root
        
    vfs.root = vfs.LazyNode(initroot)