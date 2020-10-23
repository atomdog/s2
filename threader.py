import os
from distutils.dir_util import copy_tree
import threading
import UDPPipe
import concurrent.futures
from multiprocessing.pool import ThreadPool

def mpf(fil):
    return_value= UDPPipe.run(fil)
    return(return_value)

def threadWalk(direct):
    rl = []
    directory = str(direct)
    for entry in os.scandir(directory):
        c = mpf(entry)
        rl.append(c)
    return(rl)
