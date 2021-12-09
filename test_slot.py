# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:56:44 2021

@author: saria
"""

import skrf as rf
from skrf.data import ring_slot

ring_slot['80-90 ghz'].plot_s_db(m=0, n=1)
r1 = ring_slot.copy()
r2 = ring_slot.copy()
# (r1**r2).plot_s_db()
((r1*r2)/r2).plot_s_deg()

