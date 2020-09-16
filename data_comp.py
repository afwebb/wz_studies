import ROOT
#import '/u6/afwebb/script/plotting/AtlasStyle.C'

texfile = open("data_plots/badAB106/plots.tex", "w")

print >>texfile, ('\\documentclass[hyperref={pdfpagelayout=SinglePage}]{beamer}\\usetheme{Warsaw}\\usepackage{euler}\\usepackage{pgf}\\usecolortheme{crane}\\usefonttheme{serif}\\useoutertheme{infolines}\\usepackage{epstopdf}\\usepackage{xcolor}\\usepackage{multicol}\\title{Plots}')
print >>texfile, ('\\begin{document}')

class Variable:
    def __init__(self, name, nameOld, nbins, nmin, nmax, logy = True):
        self.name = name
        self.nameOld = nameOld
        self.nbins = nbins
        self.nmin = nmin
        self.nmax = nmax
        self.logy = logy

def plot(i):

    #newFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/ab106_WZ/cern_ttW/v3/data/topo_comb.root")
    newFileA = ROOT.TFile.Open("/data/afwebb/datasets/WZ_ab127/Data/data_comb.root")
    #newFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/ab106_WZ/Data/small_cern_ttW/data_comb.root")
    nomNewA = newFileA.Get("nominal")

    #newFileD = ROOT.TFile.Open("/data_ceph/afwebb/datasets/v7_WZ/GN2/Nominal/mc16d/361601.root")
    #nomNewD = newFileD.Get("nominal")
    
    oldFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/remove_duplicates_v8_CB/Sys/test_comb.root")
    #oldFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/remove_duplicates_v8_CB/Sys/test18_HIGG8D1.root")
    nomOldA = oldFileA.Get("nominal")

    oldFileD = ROOT.TFile.Open("/data_ceph/afwebb/datasets/remove_duplicates_v8_CB/Sys/test18_HIGG8D1.root")
    nomOldD = oldFileD.Get("nominal")

    wNew = 1 #newFile.Get("sumWeights").Get("Count").Integral()
    wOld = 1 #oldFile.Get("sumWeights").Get("Count").Integral()
    
    sr = "trilep_type&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&abs(total_charge)==1&&(((lep_ID_0==-lep_ID_1 && ((lep_ID_0==-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0==-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))&&nJets_OR>0&&abs(Mlll012-91.2e3)>10e3"# && nJets_OR<3"
    #sr = "trilep_type>0"
    #sr+="&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)"
    #sr+="&&(lep_Pt_0>100e3&&(lep_Pt_1>100e3||lep_Pt_2>100e3))"
    sr+="&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2)"
    #sr+="&&abs(total_charge)==1&&(((lep_ID_0==-lep_ID_1 && ((lep_ID_0==-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0==-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))"
    #sr+="&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))"
    #sr+="&&nJets_OR>0&&abs(Mlll012-91.2e3)>10e3&&nJets_OR<3"
    #sr+="&&trilep_type=="+i
    iso106 = "&&( (abs(lep_ID_0)==11 && lep_isolationFCLoose_0&& lep_promptLeptonImprovedVeto_TagWeight_0<-0.3 &&lep_ambiguityType_0==0) || (abs(lep_ID_0)==13 && lep_isMedium_0 && lep_isolationFCLoose_0 && lep_promptLeptonImprovedVeto_TagWeight_0<-0.3 && lep_ambiguityType_0 == 0) )&&( (abs(lep_ID_1)==11 && lep_isolationFCLoose_1&& lep_promptLeptonImprovedVeto_TagWeight_1<-0.3 &&lep_ambiguityType_1==0) || (abs(lep_ID_1)==13 && lep_isMedium_1 && lep_isolationFCLoose_1 && lep_promptLeptonImprovedVeto_TagWeight_1<-0.3 && lep_ambiguityType_1 == 0) )&&( (abs(lep_ID_2)==11 && lep_isolationFCLoose_2&& lep_promptLeptonImprovedVeto_TagWeight_2<-0.3 &&lep_ambiguityType_2==0) || (abs(lep_ID_2)==13 && lep_isMedium_2 && lep_isolationFCLoose_2 && lep_promptLeptonImprovedVeto_TagWeight_2<-0.3 && lep_ambiguityType_2 == 0) )&&met_met>20e3"
    #iso36 = "&&((abs(lep_ID_0)==11 && lep_isolationFixedCutLoose_0 && lep_isTightLH_0 && lep_promptLeptonVeto_TagWeight_0<-0.7 && lep_ambiguityType_0 == 0)||(abs(lep_ID_0)==13 && lep_isolationFixedCutLoose_0 && lep_isMedium_0 && lep_promptLeptonVeto_TagWeight_0<-0.5 && lep_ambiguityType_0 == 0))&&((abs(lep_ID_1)==11 && lep_isolationFixedCutLoose_1 && lep_isTightLH_1 && lep_promptLeptonVeto_TagWeight_1<-0.7 && lep_ambiguityType_1 == 0)||(abs(lep_ID_1)==13 && lep_isolationFixedCutLoose_1 && lep_isMedium_1 && lep_promptLeptonVeto_TagWeight_1<-0.5&& lep_ambiguityType_1 == 0))&&((abs(lep_ID_2)==11 && lep_isolationFixedCutLoose_2 && lep_isTightLH_2 && lep_promptLeptonVeto_TagWeight_2<-0.7 && lep_ambiguityType_2 == 0)||(abs(lep_ID_2)==13 && lep_isolationFixedCutLoose_2 && lep_isMedium_2 && lep_promptLeptonVeto_TagWeight_2<-0.5 && lep_ambiguityType_2 == 0))"
    #iso106 = "&&((abs(lep_ID_0)==11 && lep_isolationFCLoose_0 && lep_isTightLH_0 && lep_promptLeptonVeto_TagWeight_0<0.0 && lep_ambiguityType_0 == 0)||(abs(lep_ID_0)==13 && lep_isolationFCLoose_0 ))&&((abs(lep_ID_1)==11 && lep_isolationFCLoose_1 && lep_isTightLH_1 && lep_promptLeptonVeto_TagWeight_1<0.0 && lep_ambiguityType_1 == 0)||(abs(lep_ID_1)==13 && lep_isolationFCLoose_1))&&((abs(lep_ID_2)==11 && lep_isolationFCLoose_2 && lep_isTightLH_2 && lep_promptLeptonVeto_TagWeight_2<0.0 && lep_ambiguityType_2 == 0)||(abs(lep_ID_2)==13 && lep_isolationFCLoose_2))"
    electronCut = ""#&&(lep_isolationFCLoose_0 && lep_isolationFCLoose_1 && lep_isolationFCLoose_2 )&&(lep_promptLeptonVeto_TagWeight_0<0.7 && lep_promptLeptonVeto_TagWeight_1<0.7 && lep_promptLeptonVeto_TagWeight_2<0.7)&&(lep_ambiguityType_0==0 && lep_ambiguityType_1==0 && lep_ambiguityType_2 == 0)"
    iso36 = ''
    iso36+='&&MET_RefFinal_et>20e3'
    #iso36 += "&&((abs(lep_ID_0)==11 && lep_isolationFixedCutLoose_0 && lep_isTightLH_0 && lep_promptLeptonVeto_TagWeight_0<-0.7 && lep_ambiguityType_0 == 0)||(abs(lep_ID_0)==13 && lep_isolationFixedCutLoose_0 && lep_isMedium_0 && lep_promptLeptonVeto_TagWeight_0<-0.5 && lep_ambiguityType_0 == 0))&&((abs(lep_ID_1)==11 && lep_isolationFixedCutLoose_1 && lep_isTightLH_1 && lep_promptLeptonVeto_TagWeight_1<-0.7 && lep_ambiguityType_1 == 0)||(abs(lep_ID_1)==13 && lep_isolationFixedCutLoose_1 && lep_isMedium_1 && lep_promptLeptonVeto_TagWeight_1<-0.5&& lep_ambiguityType_1 == 0))&&((abs(lep_ID_2)==11 && lep_isolationFixedCutLoose_2 && lep_isTightLH_2 && lep_promptLeptonVeto_TagWeight_2<-0.7 && lep_ambiguityType_2 == 0)||(abs(lep_ID_2)==13 && lep_isolationFixedCutLoose_2 && lep_isMedium_2 && lep_promptLeptonVeto_TagWeight_2<-0.5 && lep_ambiguityType_2 == 0))"



    varList = []
    varList.append(Variable("nJets_OR_DL1r_70","nJets_OR_T_MV2c10_70",3,0,3))
    #varList.append(Variable("nJets_OR_MV2c10_70","nJets_OR_T_MV2c10_70",3,0,3))
    #varList.append(Variable("jets_Pt_0","lead_jetPt",30,0,300000))
    #varList.append(Variable("nJets_OR","nJets_OR",8,0,8))

    varList.append(Variable("trilep_type","trilep_type",5,0,5))
    varList.append(Variable("RunYear","newRunYear",4,2015,2019))

    varList.append(Variable("passTrigger","passTrigger",2,0,2))
    varList.append(Variable("Mll01","Mll01",30,0,150000))
    varList.append(Variable("Mll02","Mll02",30,0,150000))

    #varList.append(Variable("Mll12",30,0,150000))
    #varList.append(Variable("Mlll012",30,0,500000))
    varList.append(Variable("met_met","MET_RefFinal_et",30,0,200000))
    varList.append(Variable("lep_Pt_0","lep_Pt_0",30,0,200000))

    varList.append(Variable("lep_Pt_1","lep_Pt_1",30,0,200000))                                                                  
    varList.append(Variable("lep_Pt_2","lep_Pt_2",30,0,200000))
    
    varList.append(Variable("best_Z_other_MtLepMet","best_Z_other_MtLepMet",30,0,300000))
    
    varList.append(Variable("lep_ID_0","lep_ID_0",30,-15,15))
    varList.append(Variable("lep_ID_1","lep_ID_1",30,-15,15))
    varList.append(Variable("lep_ID_2","lep_ID_2",30,-15,15))
    varList.append(Variable("lep_isTrigMatch_0","lep_isTrigMatch_0",2,0,2))
    varList.append(Variable("lep_isTrigMatch_1","lep_isTrigMatch_1",2,0,2))
    varList.append(Variable("lep_isTrigMatch_2","lep_isTrigMatch_2",2,0,2))
    varList.append(Variable("lep_isTrigMatchDLT_0","lep_isTrigMatchDLT_0",2,0,2))
    varList.append(Variable("lep_isTrigMatchDLT_1","lep_isTrigMatchDLT_1",2,0,2))
    varList.append(Variable("lep_isTrigMatchDLT_2","lep_isTrigMatchDLT_2",2,0,2))
    
    #varList.append(Variable("lep_isMedium_1",2,0,2))
    #varList.append(Variable("lep_isTight_1",2,0,2))                                                                     
    #varList.append(Variable("lep_isolationFCTight_1",2,0,2))                                                  
    #varList.append(Variable("lep_isolationLoose_1",2,0,2))
    #varList.append(Variable("lep_isolationLooseTrackOnly_1",2,0,2))
    #varList.append(Variable("lep_isolationGradient_1",2,0,2))
    #varList.append(Variable("lep_isolationTightTrackOnly_1",2,0,2))
    #varList.append(Variable("lep_isolationFCLoose_1",2,0,2))

    #varList.append(Variable("(10*nJets_OR_T_MV2c10_70+((nJets_OR_T)*(nJets_OR_T<9)+9*(nJets_OR_T>=9)))",30,0,30))
    #varList.append(Variable("Mll03",30,0,150000))
    #varList.append(Variable("Mll13",30,0,150000))
    #varList.append(Variable("Mll23",30,0,150000))
    #varList.append(Variable('minOSMll',30,0,150000))
    #varList.append(Variable('DEtall01', 30, 0, 5))
    #varList.append(Variable('DEtall02', 30, 0, 5))
    #varList.append(Variable('DEtall03', 30, 0, 5))
    #varList.append(Variable('DEtall12', 30, 0, 5))
    #varList.append(Variable('DEtall13', 30, 0, 5))
    #varList.append(Variable('DEtall23', 30, 0, 5))

    icount = 1
    for var in varList:#, nbins, nmin, nmax in zip(varList, binList, minList, maxList):
        c1 = ROOT.TCanvas();
        c1.cd();
        pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
        pad2 = ROOT.TPad("pad2", "pad2", 0, 0.05, 1, 0.3);
        pad1.SetBottomMargin(0);
        pad1.Draw();
        pad1.cd();
        pad1.SetLogy()
        #ROOT.gStyle.SetOptStat(0);
        newHist = ROOT.TH1F('newHist', 'newHist', var.nbins,var.nmin, var.nmax)
        #newHistD = ROOT.TH1F('newHistD', 'newHistD', var.nbins,var.nmin, var.nmax)
        #nomNewA.Draw(var.name+">>newHist", sr);
        nomNewA.Draw(var.name+">>newHist", sr+iso106);
        #newHist.Add(newHistD)
        newHist.SetLineColor(2)
        
        oldHist = ROOT.TH1F('oldHist', 'oldHist', var.nbins,var.nmin, var.nmax)
        oldHistD = ROOT.TH1F('oldHistD', 'oldHistD', var.nbins,var.nmin, var.nmax)

        #nomOldA.Draw(var.nameOld+">>oldHist", sr)
        #nomOldD.Draw(var.nameOld+">>oldHistD", sr);
        nomOldA.Draw(var.nameOld+">>oldHist", sr+iso36)
        nomOldD.Draw(var.nameOld+">>oldHistD", sr+iso36);
        oldHist.Add(oldHistD)
        oldHist.SetLineColor(4)

        print "New yield: "+str(newHist.Integral())
        print "Old yield: "+str(oldHist.Integral())
        
        #title = oldHist.GetTitle()
        oldHist.GetXaxis().SetTitle(var.name+'/'+var.nameOld)
        newHist.GetXaxis().SetTitle(var.name+'/'+var.nameOld)
        
        oldHist.SetTitle("")
        newHist.SetTitle("")

        #oldHist.Rebin(2)
        #newHist.Rebin(2)

        hist_stack = ROOT.THStack("hist_stack", "")
        hist_stack.Add(oldHist)
        hist_stack.Add(newHist)
        
        leg = ROOT.TLegend (0.7,0.7,0.89,0.85);
        leg.SetFillStyle(0)
        leg.SetBorderSize(0)
        leg.AddEntry(newHist, 'AB 106', 'l')
        leg.AddEntry(oldHist, 'AT 36', 'l')

        hist_stack.Draw("nostack, e")
        hist_stack.GetXaxis().SetTitle(var.name)
        c1.Modified()
        leg.Draw()

        c1.cd();
        pad2.SetTopMargin(0);
        pad2.SetBottomMargin(0.2);
        pad2.Draw();
        pad2.cd();

        h3 = newHist.Clone("h3");
        h3.SetLineColor(1);
        h3.SetMinimum(0.25);
        h3.SetMaximum(2.0); 
        h3.Sumw2();
        h3.SetStats(0);    
        h3.SetTitle("");
        h3.Divide(oldHist);
        h3.SetMarkerStyle(21);
        
        h3.GetXaxis().SetTitleOffset(0.6);
        h3.GetXaxis().SetTitleSize(0.15);
        h3.GetXaxis().SetLabelSize(0.1);
        h3.GetYaxis().SetTitle("Ratio");
        h3.GetYaxis().SetTitleOffset(0.3);
        h3.GetYaxis().SetTitleSize(0.139);
        h3.GetYaxis().SetLabelSize(0.1);

        h3.Draw("ep");

        line = ROOT.TLine(var.nmin, 1, var.nmax, 1)
        line.Draw()

        #c1.SaveAs('data_plots/trilep/'+var.name+'Trilep'+i+'.pdf')
        c1.SaveAs('data_plots/'+var.name+'.pdf')

        if icount % 4 == 1:
            print >>texfile, ('\\frame{')

        print >>texfile, (r'\includegraphics[width=.47\linewidth]{%s}' % (var.name+'.pdf') + ('%'if (icount % 2 == 1) else r'\\'))

        if icount % 4 == 0:
            print >>texfile, '}\n'

        icount += 1
        

    if icount %4 != 1:
        print >>texfile, '}\n'

#for level in ["reco", "truth"]:

#for i in ['1','2','3','4']:
#    plot(i)

plot('4')

print >>texfile, '\end{document}'
texfile.close()
