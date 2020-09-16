import ROOT
from ROOT import TFile
import rootpy.io
from rootpy.io import root_open
from rootpy.tree import Tree, FloatCol, TreeModel
import sys
import pandas as pd
import math
import numpy as np
import root_numpy
from math import sqrt
from numpy import unwrap
from numpy import arange
from rootpy.vector import LorentzVector
import matplotlib.pyplot as plt                                                                                       
from array import array
from joblib import Parallel, delayed
import multiprocessing

inf = sys.argv[1]

def neutrinoPz(lepton_fourVector, neutrino_pt, neutrino_phi):
    """                                                                                                                                          
    Calculate the z-component of the nu momentum by using the W-boson mass as the constraint                               
               
    General idea:                                                                                                            
                   
    If the discriminant is less than zero, then force it to be zero.                                                         
                 
    You solve with the discriminant set to zero to get a scaled value                                                        
                   
    for the term "mu" and "pt". The neutrino Pt will be the                                                                  
             
    (lepton_pz*scaled_pt)/lepton_pt                                                                                          
                  
    """
    m_w = 80.4e3 # mass of the W boson                                                                                       
                   
    delta_phi = lepton_fourVector.Phi() - neutrino_phi

    # Simplifying term you get when solve for neutrino Pz using transverse mass of W boson                                   
                   
    mu   = (m_w)**2/2 + np.cos(delta_phi)*lepton_fourVector.Pt()*neutrino_pt
    pz_l = lepton_fourVector.Pz() # Lepton Pz                               
    pt_l = lepton_fourVector.Pt() # lepton Pt                                                                                
    e_l  = lepton_fourVector.E() # Lepton energy                                                                             
    p_l  = sqrt(pt_l**2 + pz_l**2)  # Lepton momentum                                                                        
                 
    
    el_px = lepton_fourVector.Px()
    el_py = lepton_fourVector.Py()
    nu_px = neutrino_pt*np.cos(neutrino_phi)
    nu_py = neutrino_pt*np.sin(neutrino_phi)
    
    if e_l == 0:
        nu = LorentzVector()
        return nu

    discriminant = ((mu**2*pz_l**2)/(e_l**2 - pz_l**2)**2) - ((e_l**2*neutrino_pt**2 - mu**2)/(e_l**2 - pz_l**2))
    if discriminant>0:
        pZ_nu_A = mu*lepton_fourVector.Pz()/(pt_l**2) + sqrt(discriminant)
        pZ_nu_B = mu*lepton_fourVector.Pz()/(pt_l**2) - sqrt(discriminant)

    elif discriminant<0:
        scaled_mu = sqrt(pt_l**2*e_l**2*neutrino_pt**2/(pz_l**2+pt_l**2))
        scaled_pt = m_w**2/(2*pt_l*(1-np.cos(delta_phi)))
        pZ_nu_A = pZ_nu_B = (pz_l*scaled_pt)/pt_l

    elif discriminant==0:
        pZ_nu_A = pZ_nu_B = mu*lepton_fourVector.Pz()/(pt_l**2)

    if abs(pZ_nu_A) < abs(pZ_nu_B):
        nu_pz = pZ_nu_A
    else:
        nu_pz = pZ_nu_B

    nu = LorentzVector()
    nu.SetPxPyPzE(nu_px, nu_py, nu_pz, neutrino_pt)

    return nu

def run_top_mass(inputPath):
    
    topMassesWZ = []
    topMassestZ = []
    topMassReco = []

    f = TFile(inputPath, "READ")
    dsid = inputPath.split('/')[-1]
    dsid = dsid.replace('.root', '')
    #print(inputPath)
    nom = f.Get('nominal')                                                                                           

    try:
        nom.GetEntries()
    except:
        print('failed for '+inputPath )
        return 0

    try:                                                                                                              
        nom.Mll01
    except:
        print('failed for '+inputPath)
        return 0

    if nom.GetEntries()==0:
        return 0

    if hasattr(nom, "topMassReco"):
        print('already there', inputPath)
        return 0

    nEntries = nom.GetEntries()
    for idx in range(nEntries):                                                                            
        if idx%10000==0:                                                                                           
            print(str(idx)+'/'+str(nEntries))
            
        nom.GetEntry(idx)

        lep = LorentzVector()
        
        if abs(nom.Mll02 - 91.2e3) < abs(nom.Mll01 - 91.2e3):
            lep.SetPtEtaPhiE( nom.lep_Pt_1, nom.lep_Eta_1, nom.lep_Phi_1, nom.lep_E_1 )
        else:
            lep.SetPtEtaPhiE( nom.lep_Pt_2, nom.lep_Eta_2, nom.lep_Phi_2, nom.lep_E_2 ) 
        
        met = neutrinoPz(lep, nom.met_met, nom.met_phi)
    
        w = lep+met
    
        jet = LorentzVector()
        jet.SetPtEtaPhiE( nom.jet_Pt_0, nom.jet_Eta_0, nom.jet_Phi_0, nom.jet_E_0 )
        
        top = LorentzVector()
        
        top = w+jet

        topMassReco.append(top.M())

    f.Close()

    with root_open(inputPath, mode='a') as myfile:
        topMassReco = np.asarray(topMassReco)
        topMassReco.dtype = [('topMassReco', 'float64')]
        topMassReco.dtype.names = ['topMassReco']
        root_numpy.array2tree(topMassReco, tree=myfile.nominal)
        myfile.write()
        myfile.Close()

linelist = [line.rstrip() for line in open(inf)]
Parallel(n_jobs=30)(delayed(run_top_mass)(inFile) for inFile in linelist)

#newNom.Write()    
#outFile.Write()
#outFile.Close()
#inFile.Close()
