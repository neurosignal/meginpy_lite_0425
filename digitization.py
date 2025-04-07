#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:37:14 2023

@author: Amit Jaiswal <amit.jaiswal@megin.fi>
"""
import mne
import numpy as np
from copy import deepcopy
from paramiko import SSHClient, AutoAddPolicy
from datetime import datetime
import shutil

#%% read and convert string to extra
def string2extra(raw_fname, showfiff_fname=None, raw_new_fname=None, 
                 overwrite=False, hostname="xxxxx.xxxxx.local", port=22, 
                 username='xxxx', password='xxxxxxxx'):
    """
    Parameters
    ----------
    raw_fname : FIFF file name
        DESCRIPTION.
    showfiff_fname : name of a text (.txt) file to write showfiff info., optional
        DESCRIPTION. The default is None.
    raw_new_fname : New FIFF file name to write with extra points, optional
        DESCRIPTION. The default is None.
    overwrite : TYPE, optional
        DESCRIPTION. The default is False.
    hostname : hostname or IP address of a system which has show_fiff installed as 
                /neuro/bin/util/show_fiff
        DESCRIPTION. The default is "xxxxx.xxxxx.local".
    port : TYPE, optional
        DESCRIPTION. The default is 22.
    username : TYPE, optional
        DESCRIPTION. The default is 'xxxx'.
    password : TYPE, optional
        DESCRIPTION. The default is 'xxxxxxxx'.
    Returns
    -------
    raw : TYPE
        DESCRIPTION.
    """
    n_orig = len(mne.io.read_info(raw_fname, verbose=False)['dig'])
    if showfiff_fname is None:
        showfiff_fname = raw_fname.replace('.fif', '_show_fiff%s.txt'\
                                           %datetime.now().strftime("-%Y%m%d%H%M"))
    # Run MEGIN's show_fiff
    bin_name = '/neuro/bin/util/show_fiff'
    command     = f'{bin_name} -vt234 %s > %s'%(raw_fname, showfiff_fname)
    
    if shutil.which(bin_name):
        print(f"{bin_name} is installed.")
        mne.utils.run_subprocess(command)
    else:
        print(f"{bin_name} is NOT installed on this machine; connecting to {hostname}...")
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)
    
    fileID = open(showfiff_fname)
    all_lines = fileID.readlines()
    fileID.close()

    all_digs = np.empty((0,3), dtype="float64")
    for ii in range(len(all_lines)):
        if '(' in all_lines[ii] and ')' in all_lines[ii]:
            point_ = (all_lines[ii].split('('))[1].split(')')[0]
            point  = np.array(tuple(map(float, point_.split(', '))))
            all_digs = np.vstack( (all_digs, point))
            
    raw = mne.io.read_raw_fif(raw_fname, preload=True)
    print('\n\nOriginal: ', raw)
    new_dig = raw.info['dig']
    cnt = 1 if raw.info['dig'][-1]['kind']!=mne.io.constants.FIFF.FIFFV_POINT_EXTRA \
        else raw.info['dig'][-1]['ident']
    for ii in range(len(raw.info['dig']), all_digs.shape[0]):
        cnt += 1
        tmp_extra               = deepcopy(raw.info['dig'][-1])
        tmp_extra['kind']       = mne.io.constants.FIFF.FIFFV_POINT_EXTRA
        tmp_extra['r']          = np.float64(all_digs[ii]/1000)
        tmp_extra['ident']      = cnt
        tmp_extra['coord_frame']= mne.io.constants.FIFF.FIFFV_COORD_HEAD
        new_dig.append(tmp_extra)
    print('Modified: ', raw)
    print(f"Original # dig. points = {n_orig}")
    print(f"Modified # dig. points = {len(raw.info['dig'])}\n")
    if raw_new_fname is not False:
        if raw_new_fname is None:
            raw_new_fname = raw_fname.replace('.fif', '-dense-hsp.fif')
        raw.save(raw_new_fname, overwrite=overwrite)
        print('Raw file with dense extra points was written at %s'%raw_new_fname)
    return raw


    