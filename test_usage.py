#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 14:40:42 2025

@author: Amit Jaiswal <amit.jaiswal@megin.fi>
USAGE: Read the string type digitization points and extra headshape points
"""
import sys
string2extra_points_dir = '/home/amit3/pCloudDrive/Scripts/MyGitHubRepos/string2extra_points'
sys.path.append(string2extra_points_dir)
from digitization import read_convert_string2extra
import mne
print(__doc__)

# ip_adr, uname, pswrd = 'xxx.xx.xx.xxx', 'xxxxxx', 'xxxxxxx'
ip_adr, uname, pswrd = '172.16.51.210', 'meguser', 'meg306'

#%%
fname = '/net/qnap/data/rd/MEGflow_training_data/Training-004/scan1/raw_data_tsss_mc.fif'
fname_new = fname.replace('.fif', '-dense-hsp.fif')
info = mne.io.read_info(fname, verbose=False)
print(f"\n\nTotal detected points (default): {len(info['dig'])}")
# raw0 = mne.io.read_raw_fif(fname, verbose=True)

#%% Use read_convert_string2extra instead of mne.io.read_raw_fif
raw = read_convert_string2extra(fname, hostname=ip_adr, username=uname, password=pswrd, raw_new_fname=False)
print(f"\n\nTotal detected points (new): {len(raw.info['dig'])}")

#%%