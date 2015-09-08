# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 17:47:05 2015

@author: Bas des Tombe, bdestombe@gmail.com
"""

import init
reload(init)
from os.path import dirname


#c = [ 'ml', 'bas6', 'nwt', 'pks', 'riv', 'sw', 'uzf', 'pval', 'sor', 'btn', 'swi2', 'adv', 'sip', 'chd', 'zone', 'rct', 'gmg', 'dsp', 'wel', 'rch', 'tob', 'pcg', 'phc', 'vdf', 'pcgn', 'upw', 'hfb6', 'mult', 'ssm', 'gcg', 'ml', 'oc', 'mt', 'vsc', 'ghb', 'drn', 'lpf', 'evt', 'dis']

c=['ml', 'dis', 'bas6', 'lpf', 'wel', 'riv', 'oc', 'pcg', 'mt', 'btn',  'adv', 'dsp', 'ssm', 'rct', 'gcg', 'sw', 'vdf', 'vsc']

ws = r'C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\'
filename = 'test.py'
nampath = 'C:\\Users\\Bas\\Google Drive\\CiTG MSc\\Artesia\\mflab\\run\\swt_v4.NAM'
dirname(nampath)

init.flopyinit(c=c, ws=ws, filename=filename, comment=False, unit=False, load=nampath, verbose=False)