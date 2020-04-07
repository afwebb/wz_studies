import ROOT
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

topMassesWZ = []
topMassestZ = []

inName = sys.argv[1]
#inFile = root_open(inName)

sys_trees = ["EG_RESOLUTION_ALL__1down",
             "EG_RESOLUTION_ALL__1up",
             "EG_SCALE_AF2__1down",
             "EG_SCALE_AF2__1up",
             "EG_SCALE_ALL__1down",
             "EG_SCALE_ALL__1up",
             "JET_CategoryReduction_JET_BJES_Response__1down",
             "JET_CategoryReduction_JET_BJES_Response__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Detector1__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Detector1__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Mixed1__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Mixed1__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Mixed2__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Mixed2__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Mixed3__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Mixed3__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling1__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling1__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling2__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling2__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling3__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling3__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling4__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Modelling4__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical1__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical1__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical2__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical2__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical3__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical3__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical4__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical4__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical5__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical5__1up",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical6__1down",
             "JET_CategoryReduction_JET_EffectiveNP_Statistical6__1up",
             "JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1down",
             "JET_CategoryReduction_JET_EtaIntercalibration_Modelling__1up",
             "JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_highE__1down",
             "JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_highE__1up",
             "JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_negEta__1down",
             "JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_negEta__1up",
             "JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_posEta__1down",
             "JET_CategoryReduction_JET_EtaIntercalibration_NonClosure_posEta__1up",
             "JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1down",
             "JET_CategoryReduction_JET_EtaIntercalibration_TotalStat__1up",
             "JET_CategoryReduction_JET_Flavor_Composition__1down",
             "JET_CategoryReduction_JET_Flavor_Composition__1up",
             "JET_CategoryReduction_JET_Flavor_Response__1down",
             "JET_CategoryReduction_JET_Flavor_Response__1up",
             "JET_CategoryReduction_JET_Pileup_OffsetMu__1down",
             "JET_CategoryReduction_JET_Pileup_OffsetMu__1up",
             "JET_CategoryReduction_JET_Pileup_OffsetNPV__1down",
             "JET_CategoryReduction_JET_Pileup_OffsetNPV__1up",
             "JET_CategoryReduction_JET_Pileup_PtTerm__1down",
             "JET_CategoryReduction_JET_Pileup_PtTerm__1up",
             "JET_CategoryReduction_JET_Pileup_RhoTopology__1down",
             "JET_CategoryReduction_JET_Pileup_RhoTopology__1up",
             "JET_CategoryReduction_JET_PunchThrough_MC16__1down",
             "JET_CategoryReduction_JET_PunchThrough_MC16__1up",
             "JET_CategoryReduction_JET_SingleParticle_HighPt__1down",
             "JET_CategoryReduction_JET_SingleParticle_HighPt__1up",
             "JET_JER_SINGLE_NP__1up",
             "MET_SoftTrk_ResoPara",
             "MET_SoftTrk_ResoPerp",
             "MET_SoftTrk_ScaleDown",
             "MET_SoftTrk_ScaleUp",
             "MUON_ID__1down",
             "MUON_ID__1up",
             "MUON_MS__1down",
             "MUON_MS__1up",
             "MUON_SAGITTA_RESBIAS__1down",
             "MUON_SAGITTA_RESBIAS__1up",
             "MUON_SAGITTA_RHO__1down",
             "MUON_SAGITTA_RHO__1up",
             "MUON_SCALE__1down",
             "MUON_SCALE__1up",
             "TAUS_TRUEHADTAU_SME_TES_DETECTOR__1down",
             "TAUS_TRUEHADTAU_SME_TES_DETECTOR__1up",
             "TAUS_TRUEHADTAU_SME_TES_INSITU__1down",
             "TAUS_TRUEHADTAU_SME_TES_INSITU__1up",
             "TAUS_TRUEHADTAU_SME_TES_MODEL__1down",
             "TAUS_TRUEHADTAU_SME_TES_MODEL__1up"
         ]

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

for sys in sys_trees:

    inFile = root_open(inName)
    nom = inFile.get(sys)
    topMassReco = []

    current=0
    for e in nom:
        #newNom.GetEntry(current)
        current+=1
        if current%10000==0:
            print(current)
            #if current==200000:
            #    break
            
            #if e.nJets_OR_T!=1: 
            #    continue
            #if e.nJets_OR_T_MV2c10_70!=1:
            #    continue
            #if abs(e.Mll01 - 91.2e3) > 10e3 and abs(e.Mll02 - 91.2e3) > 10e3:
            #    continue
            #if e.trilep_type==0: continue

        lep = LorentzVector()
    
        if abs(e.Mll02 - 91.2e3) < abs(e.Mll01 - 91.2e3):
            lep.SetPtEtaPhiE( e.lep_Pt_1, e.lep_Eta_1, e.lep_Phi_1, e.lep_E_1 )
        else:
            lep.SetPtEtaPhiE( e.lep_Pt_2, e.lep_Eta_2, e.lep_Phi_2, e.lep_E_2 ) 
        
        met = neutrinoPz(lep, e.MET_RefFinal_et, e.MET_RefFinal_phi)
    
        w = lep+met
        
        jet = LorentzVector()
        jet.SetPtEtaPhiE( e.lead_jetPt, e.lead_jetEta, e.lead_jetPhi, e.lead_jetE )
        
        top = LorentzVector()
        
        top = w+jet
        
        topMassReco.append(top.M())

    #print(top.M())
    #topMassReco = top.M()
    #newNom.topMassReco = top.M()
    #newNom.Fill()
    inFile.Close()

    with root_open(inName, mode='a') as myfile:
        topMassReco = np.asarray(topMassReco)
        topMassReco.dtype = [('topMassReco', 'float64')]
        topMassReco.dtype.names = ['topMassReco']
        root_numpy.array2tree(topMassReco, tree=myfile.Get(sys))
        myfile.write()
        myfile.Close()

#newNom.Write()    
#outFile.Write()
#outFile.Close()
#inFile.Close()
