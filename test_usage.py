#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 14:40:42 2025

@author: Amit Jaiswal <amit.jaiswal@megin.fi>

Read the string type digitization points and extra headshape points
"""
try:
    from meginpy_lite_0425.digitization import string2extra
except ModuleNotFoundError:
    import sys
    sys.path.append('MyGitHubRepos/meginpy_lite_0425')
    from digitization import string2extra
import mne
print(__doc__)

#%% Provide the hostname, username and password if show_fiff is not available on this machine
ip_adr, uname, pswrd = 'xxx.xx.xx.xxx', 'xxxxxx', 'xxxxxxx'

#%%
fname = '....../rd/MEGflow_training_data/Training-004/scan1/raw_data_tsss_mc.fif'
fname_new = fname.replace('.fif', '-dense-hsp.fif')
info = mne.io.read_info(fname, verbose=False)
print(f"\n\nTotal detected points (default): {len(info['dig'])}")

#%% Use read_convert_string2extra instead of mne.io.read_raw_fif
raw = string2extra(fname, hostname=ip_adr, username=uname, password=pswrd, raw_new_fname=False)
print(f"\n\nTotal detected points (new): {len(raw.info['dig'])}")

