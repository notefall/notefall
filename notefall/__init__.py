import os, logging

def configureLogger(log):
    logging.captureWarnings(True)
    log.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(muz.util.COloredFormatter("%(levelname)18s %(name)s: %(message)s"))
    
    log.addHandler(ch)
    
log = logging.getLogger(__name__)

import notefall.config

_config = notefall.config.get(__name__, {
    "log": {
        "level": "warning",
    },
})

from . import main, util, config, assets, console, beatmap, vfs
configureLogger(log)

from notefall.main import NAME, VERSION, vfsInit, run, runUI, init, bareInit