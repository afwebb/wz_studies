import ROOT
#import '/u6/afwebb/script/plotting/AtlasStyle.C'

texfile = open("mc16d_plots/plots.tex", "w")

print >>texfile, ('\\documentclass[hyperref={pdfpagelayout=SinglePage}]{beamer}\\usetheme{Warsaw}\\usepackage{euler}\\usepackage{pgf}\\usecolortheme{crane}\\usefonttheme{serif}\\useoutertheme{infolines}\\usepackage{epstopdf}\\usepackage{xcolor}\\usepackage{multicol}\\title{Plots}')
print >>texfile, ('\\begin{document}')

class Variable:
    def __init__(self, name, nbins, nmin, nmax, logy = True):
        self.name = name
        #self.nameOld = nameOld
        self.nbins = nbins
        self.nmin = nmin
        self.nmax = nmax
        self.logy = logy

def plot():

    #newFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/v7_WZ/GN2/Nominal/mc16d/364253.root")
    newFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/ab106_WZ/cern_ttW/Nominal/mc16e/364253.root")
    #newFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/ab106_WZ/test/mc16d/brokenMuons364253.root") 
    #newFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/ab106_WZ/Data/data15.root")
    nomNewA = newFileA.Get("nominal")

    #oldFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/v7_WZ/GN2/Sys/mc16d/364253.root")
    oldFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/remove_duplicates_v8_CB/Sys/test_mc16e/364253.root")
    #oldFileA = ROOT.TFile.Open("/data_ceph/afwebb/datasets/ab106_WZ/test/mc16d/brokenMuons364253.root")
    nomOldA = oldFileA.Get("nominal")

    wOld = 1 #oldFile.Get("sumWeights").Get("Count").Integral()

    sr = "60000*scale_nom*pileupEventWeight_090*MV2c10_Continuous_EventWeight*(trilep_type>0&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2||matchDLTll01||matchDLTll02||matchDLTll12)&&abs(total_charge)==1&&(((lep_ID_0!=-lep_ID_1 && ((lep_ID_0!=-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0!=-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))&&nJets_OR_T>0&&abs(Mlll012-91.2e3)>10e3)"#&&best_Z_other_MtLepMet>30e3&&MET_RefFinal_et>20e3)"

    sr = "60000*scale_nom*pileupEventWeight_090*MV2c10_Continuous_EventWeight*(trilep_type>0&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2)&&abs(total_charge)==1&&(((lep_ID_0!=-lep_ID_1 && ((lep_ID_0!=-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0!=-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))&&abs(Mlll012-91.2e3)>10e3 && (lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2))"#

    iso106 = "60000*scale_nom*pileupEventWeight_090*MV2c10_Continuous_EventWeight*(trilep_type>0&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2)&&abs(total_charge)==1&&(((lep_ID_0!=-lep_ID_1 && ((lep_ID_0!=-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0!=-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))&&abs(Mlll012-91.2e3)>10e3 && (lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2)&&((abs(lep_ID_0)==11 && lep_isolationFCLoose_0 && lep_isTightLH_0 && lep_promptLeptonVeto_TagWeight_0<0.0 && lep_ambiguityType_0 == 0)||(abs(lep_ID_0)==13 && lep_isolationFCLoose_0 ))&&((abs(lep_ID_1)==11 && lep_isolationFCLoose_1 && lep_isTightLH_1 && lep_promptLeptonVeto_TagWeight_1<0.0 && lep_ambiguityType_1 == 0)||(abs(lep_ID_1)==13 && lep_isolationFCLoose_1))&&((abs(lep_ID_2)==11 && lep_isolationFCLoose_2 && lep_isTightLH_2 && lep_promptLeptonVeto_TagWeight_2<0.0 && lep_ambiguityType_2 == 0)||(abs(lep_ID_2)==13 && lep_isolationFCLoose_2)))"

    #sr = "(trilep_type>0&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2)&&abs(total_charge)==1&&(((lep_ID_0!=-lep_ID_1 && ((lep_ID_0!=-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0!=-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))&&nJets_OR_T>0&&abs(Mlll012-91.2e3)>10e3 && RunYear==2015 && (lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2))"

    srGN1 = "140000*pileupEventWeight_090*MV2c10_Continuous_EventWeight*(trilep_type>0&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2)&&abs(total_charge)==1&&(((lep_ID_0!=-lep_ID_1 && ((lep_ID_0!=-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0!=-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))&&nJets_OR_T>0&&abs(Mlll012-91.2e3)>10e3)"

    #sr = "pileupEventWeight_090*scale_nom*JVT_EventWeight*SherpaNJetWeight*lepSFObjTight*lepSFTrigTight*( 36074.6*(RunYear <2016.5) + 43813.7*(RunYear > 2016.5) )*(passEventCleaning&&trilep_type>0&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2||matchDLTll01||matchDLTll02||matchDLTll12)&&abs(total_charge)==1&&(((lep_ID_0==-lep_ID_1 && ((lep_ID_0==-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0==-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&(lep_ID_0!=-lep_ID_1||(Mll01>12e3))&&(lep_ID_0!=-lep_ID_2||(Mll02>12e3))&&( ( (abs(lep_ID_0) == 13 &&lep_isMedium_0) ||( abs( lep_ID_0 ) == 11&&abs( lep_Eta_0 ) <2.0)) && ((abs( lep_ID_1 ) == 11&&abs( lep_Eta_1 ) <2.0)|| (abs(lep_ID_1) == 13 && lep_isMedium_1) ) && ((abs( lep_ID_2 ) == 11&&abs( lep_Eta_2 ) <2.0)||(abs( lep_ID_2 ) == 13 && lep_isMedium_2)))&&nJets_OR_T>0&&abs(Mlll012-91.2e3)>10e3&&best_Z_other_MtLepMet>30e3&&MET_RefFinal_et>20e3)"
#"36000*scale_nom*pileupEventWeight_090*bTagSF_weight_Continuous*lepSFObjTight*(passEventCleaning&&trilep_type>0&&(lep_Pt_0>10e3&&lep_Pt_1>20e3&&lep_Pt_2>20e3)&&(lep_isTrigMatch_0||lep_isTrigMatch_1||lep_isTrigMatch_2||matchDLTll01||matchDLTll02||matchDLTll12)&&abs(total_charge)==1&&(((lep_ID_0==-lep_ID_1 && ((lep_ID_0==-lep_ID_1&&abs(Mll01-91.2e3)<10e3)))||(lep_ID_0==-lep_ID_2&&abs(Mll02-91.2e3)<10e3)))&&lep_isolationLoose_1&&lep_isolationLoose_2&&lep_promptLeptonIso_TagWeight_1<-0.5&&lep_promptLeptonIso_TagWeight_2<-0.5&&(abs(lep_ID_1)==13||lep_isTightLH_1&&lep_chargeIDBDTTight_1>0.0670415)&&(abs(lep_ID_2)==13||lep_isTightLH_2&&lep_chargeIDBDTTight_2>0.0670415)&&lep_isolationLoose_0&&(lep_ID_0!=-lep_ID_1||Mll01>12e3)&&(lep_ID_0!=-lep_ID_2||Mll02>12e3)&&abs(Mlll012-91.2e3)>10e3&&best_Z_other_MtLepMet>30e3&&nJets_OR_T<3"

    varList = []
    varList.append(Variable("nJets_OR_T_MV2c10_70",5,0,5))
    varList.append(Variable("nJets_OR_T",10,0,10))
    varList.append(Variable("Mll01",30,0,150000))
    varList.append(Variable("Mll02",30,0,150000))
    varList.append(Variable("Mll12",30,0,150000))
    varList.append(Variable("Mlll012",30,0,500000))
    varList.append(Variable("MET_RefFinal_et",30,0,200000))
    varList.append(Variable("best_Z_Mll",30,0,150000))
    varList.append(Variable("lead_jetPt",30,0,300000))
    varList.append(Variable("lep_Pt_0",30,0,200000))
    varList.append(Variable("lep_Pt_1",30,0,200000))
    varList.append(Variable("lep_Pt_2",30,0,200000))
    varList.append(Variable("best_Z_other_MtLepMet",30,0,300000))
    varList.append(Variable("lep_ID_0",30,-15,15))
    varList.append(Variable("lep_ID_1",30,-15,15))
    varList.append(Variable("lep_ID_2",30,-15,15))
    varList.append(Variable("lep_isTrigMatch_0",2,0,2))
    varList.append(Variable("lep_isTrigMatch_1",2,0,2))
    varList.append(Variable("lep_isTrigMatch_2",2,0,2))
    varList.append(Variable("lep_isTrigMatchDLT_0",2,0,2))
    varList.append(Variable("lep_isTrigMatchDLT_1",2,0,2))
    varList.append(Variable("lep_isTrigMatchDLT_2",2,0,2))
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
        ROOT.gStyle.SetOptStat(0);

        newHist = ROOT.TH1F('newHist', 'newHist', var.nbins,var.nmin, var.nmax)
        nomNewA.Draw(var.name+">>newHist", iso106);
        #print(newHist.Integral(), wNew)
        #newHist.Scale(newHist.Integral()/wNew)
        #newHist.Scale(1/wNew)
        newHist.SetLineColor(2)
        
        oldHist = ROOT.TH1F('oldHist', 'oldHist', var.nbins,var.nmin, var.nmax)
        nomOldA.Draw(var.name+">>oldHist", sr);
        oldHist.SetLineColor(4)

        print "Nom: "+str(newHist.Integral())+ " "+str(newHist.GetEntries())
        print "Sys: "+str(oldHist.Integral())+ " "+str(oldHist.GetEntries())

        #title = oldHist.GetTitle()
        oldHist.GetXaxis().SetTitle(var.name)
        newHist.GetXaxis().SetTitle(var.name)

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

        hist_stack.Draw("nostack")
        hist_stack.GetXaxis().SetTitle(var.name)
        c1.Modified()
        leg.Draw()

        c1.cd();
        pad2.SetTopMargin(0);
        pad2.SetBottomMargin(0.2);
        pad2.Draw();
        pad2.cd();

        h3 = newHist.Clone("h3");
        h3.SetLineColor(4);
        h3.SetMinimum(0.25);
        h3.SetMaximum(4.0); 
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
        
        c1.SaveAs('mc16d_plots/'+var.name+'.pdf')

        if icount % 4 == 1:
            print >>texfile, ('\\frame{\\frametitle{WZ Preselection - Muons}')

        print >>texfile, (r'\includegraphics[width=.47\linewidth]{%s}' % (var.name+'.pdf') + ('%'if (icount % 2 == 1) else r'\\'))

        if icount % 4 == 0:
            print >>texfile, '}\n'

        icount += 1

    if icount %4 != 1:
        print >>texfile, '}\n'

#for level in ["reco", "truth"]:

plot()

print >>texfile, '\end{document}'
texfile.close()
