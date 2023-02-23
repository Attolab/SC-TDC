"""Useful functions to store data"""
import numpy as np

def open_output_file(filename,ext,index=0):
    import os,logging
    file_format = '{}_{:06d}.{}'           
    raw_filename = file_format.format(filename,index,ext)
    while os.path.isfile(raw_filename):
        index+=1 
        raw_filename = file_format.format(filename,index,ext)
    logging.info('Opening output file {}'.format(filename))

    return open(raw_filename,'wb')

def store_tof(f,data):
    # event['time']
    # trigger,tof = data
    np.save(f,data['ms_indices'])
    np.save(f,data['time'])
