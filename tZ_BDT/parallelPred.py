import xgboost as xgb
import ROOT
from ROOT import TFile
from rootpy.tree import Tree
from rootpy.vector import LorentzVector
from rootpy.io import root_open
from rootpy.tree import Tree, FloatCol, TreeModel
import root_numpy
import sys
import pickle
import math
import numpy as np
import torch
from torch import nn, optim
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim
from joblib import Parallel, delayed
import multiprocessing
import pandas as pd
#from rootpy.io import root_open

#Read in list of files
inf = sys.argv[1]

modelPath = 'models/xgb_signal.dat'
xgbModel = pickle.load(open(modelPath, "rb"))

def calc_phi(phi_0, new_phi):
    new_phi = new_phi-phi_0
    if new_phi>math.pi:
        new_phi = new_phi - 2*math.pi
    if new_phi<-math.pi:
        new_phi = new_phi + 2*math.pi
    return new_phi

#create pt prediction dicts
def create_dict(nom):
    current = 0

    events = []
    
    nEntries = nom.GetEntries()
    print(nEntries)
    for idx in range(nEntries):
        if idx%10000==0:
            print(str(idx)+'/'+str(nEntries))

        nom.GetEntry(idx)

        k = {}

        k["topMassReco"] = nom.topMassReco

        k['best_Z_other_MtLepMet'] = nom.best_Z_other_MtLepMet
        k['MET'] = nom.met_met
                         
        k['lep_Pt_0'] = nom.lep_Pt_0
        k['lep_Pt_1'] = nom.lep_Pt_1
        k['lep_Pt_2'] = nom.lep_Pt_2
        
        k['DRll01'] = nom.DRll01
        k['DRll02'] = nom.DRll02
        k['DRll12'] = nom.DRll12

        k['Mll01'] = nom.Mll01
        k['Mll02'] = nom.Mll02
        k['Mll12'] = nom.Mll12
        
        k['jets_Pt_0'] = nom.jets_Pt_0                                                               
        k['nJets_OR_DL1r_60'] = nom.nJets_OR_DL1r_60
        k['nJets_OR'] = nom.nJets_OR

        k['HT'] = nom.HT
        
        events.append(k)

    return events

#loop over file list, add prediction branches
def run_pred(inputPath):
    f = TFile.Open(inputPath, "READ")
    try:
        nom = f.Get("nominal")
    except:
        print('cant open '+inputPath)
        return 0
    dsid = inputPath.split('/')[-1]
    dsid = dsid.replace('.root', '')
    print(dsid)
    
    try:
        nom.GetEntries()                                                                                                     
    except:
        print("failed to open")
        return 0

    if nom.GetEntries() == 0:
        print("no entries")
        return 0
    if hasattr(nom, "tZ_score"):                                                                           
        print('alredy there')
        return 0  
    
    event_dict = create_dict(nom)
    
    inDF = pd.DataFrame(event_dict)
    
    xgbMat = xgb.DMatrix(inDF, feature_names=list(inDF))
    tZ_score = xgbModel.predict(xgbMat)
    
    with root_open(inputPath, mode='a') as myfile:
        tZ_score = np.asarray(tZ_score)
        tZ_score.dtype = [('tZ_score', 'float32')]
        tZ_score.dtype.names = ['tZ_score']
        root_numpy.array2tree(tZ_score, tree=myfile.nominal)
        
        myfile.write()
        myfile.Close()
        
linelist = [line.rstrip() for line in open(inf)]
Parallel(n_jobs=30)(delayed(run_pred)(inFile) for inFile in linelist)

