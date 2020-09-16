import ROOT
import numpy as np
#import rootpy.io
import sys
import math
from math import sqrt
from numpy import unwrap
from numpy import arange
from rootpy.vector import LorentzVector
import random
#import matplotlib.pyplot as plt

inf = sys.argv[1]
outDir = sys.argv[2]

year = ''

if 'mc16a' in inf:
    year='a'
elif 'mc16d' in inf:
    year='d'
elif 'mc16e' in inf:
    year='e'

f = ROOT.TFile.Open(inf)
dsid = inf.split('/')[-1]
dsid = dsid.replace('.root', '')
print(dsid)
nom = f.Get('nominal')

eventsFlat = []
current = 0

nEntries = nom.GetEntries()
for idx in range(nEntries):
    if idx%10000==0:
        print(str(idx)+'/'+str(nEntries))

    nom.GetEntry(idx)

    #if nom.trilep_type==0: continue
    if nom.nJets_OR!=1: continue
    if nom.nJets_OR_DL1_60==0: continue
    #if nom.total_charge!=3: continue
    #if nom.lep_Pt_0<10000: continue
    #if nom.lep_Pt_1<20000: continue
    #if nom.lep_Pt_2<20000: continue

    k = {}

    if nom.mcChannelNumber == 364253:
        k['signal'] = 1
    elif nom.mcChannelNumber == 410560:
        k['signal'] = 0
    elif sum([x for x in nom.hasTop]):
        k['signal'] = 0
    else:
        continue
        #k['signal'] = 1

    k["topMassReco"] = nom.topMassReco

    #k['best_Z_other_MtLepMet'] = nom.best_Z_other_MtLepMet
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

    k['jet_Pt_0'] = nom.jet_Pt_0
    #k['nJets_OR_DL1r_60'] = nom.nJets_OR_DL1r_60 

    k["DeltaR_min_lep_jet"] = nom.DeltaR_min_lep_jet
    k['minDeltaR_LJ_0'] = nom.minDeltaR_LJ_0
    k['minDeltaR_LJ_1'] = nom.minDeltaR_LJ_1 
    k['minDeltaR_LJ_2'] = nom.minDeltaR_LJ_2 
    k["MtLepMet"] = nom.MtLepMet

    #k['nJets_OR'] = nom.nJets_OR

    k['HT'] = nom.HT

    eventsFlat.append(k)

import pandas as pd

dfFlat = pd.DataFrame.from_dict(eventsFlat)

from sklearn.utils import shuffle
dfFlat = shuffle(dfFlat)

dfFlat.to_csv(outDir+'/'+dsid+year+'Flat.csv', index=False)
