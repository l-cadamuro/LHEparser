import ROOT
from array import array

import argparse

parser = argparse.ArgumentParser(description='Command line parser of parser')
#string opts
parser.add_argument('--lheIn',   dest='lheIn',   help='lhe file name', default=None)
parser.add_argument('--rootOut', dest='rootOut', help='root out file name', default=None)
parser.add_argument('--vbf',     dest='vbf',     help='use if this a VBF sample (store in/out parton info)', action='store_true', default=False)
parser.add_argument('--saveTLV', dest='saveTLV', help='save TLorentzVector', action='store_true', default=False)

args = parser.parse_args()

############ with 10k events

# from heft, 1 diagram (only trilinear?)
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/HH_HEFT_GEN/Events/run_01/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree.root', 'recreate')

# ## from heavy scalar, SM
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_01/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_SM.root', 'recreate')

# ## from heavy scalar, kl = 5
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_02/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_5.root', 'recreate')

# ## from heavy scalar, kl = 20
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_03/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_20.root', 'recreate')

# ## from heavy scalar, kl = 2.45
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_04/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_2p45.root', 'recreate')

############ with 100k events, with heavy scalar

## from heavy scalar, kl = 2.45
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_05/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_2p45.root', 'recreate')

# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_11/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_2p45_2.root', 'recreate')


# # from heavy scalar, kl = 20
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_06/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_20.root', 'recreate')

# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_12/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_20_2.root', 'recreate')


# # from heavy scalar, kl = 5
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_07/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_5.root', 'recreate')

# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_13/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_5_2.root', 'recreate')


# # from heavy scalar, kl = 1 (SM)
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_08/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_1.root', 'recreate')

# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_14/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_1_2.root', 'recreate')


# from heavy scalar, kl = 0 (box)
# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_10/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_0.root', 'recreate')

# lheIn = open('/Users/Luca/Downloads/MG5_aMC_v2_6_0/models/HeavyScalarMG5/Events/run_15/unweighted_events.lhe')
# rootOut = ROOT.TFile.Open('lheTree_klambda_0_2.root', 'recreate')

###################### making interactive
lheIn = open(args.lheIn)
rootOut = ROOT.TFile.Open(args.rootOut, 'recreate')


#### vars
HH_mass = array( 'd', [ 0 ] ) ## one value

lheTree = ROOT.TTree('lheTree', 'lheTree')
lheTree.Branch( 'HH_mass', HH_mass, 'HH_mass/D' )

if args.saveTLV:
    lheTree.vH1 = ROOT.TLorentzVector(0., 0., 0., 0.)
    lheTree.vH2 = ROOT.TLorentzVector(0., 0., 0., 0.)
    lheTree.vSum = ROOT.TLorentzVector(0., 0., 0., 0.)
    lheTree.Branch( 'vH1', lheTree.vH1)
    lheTree.Branch( 'vH2', lheTree.vH2)
    lheTree.Branch( 'vSum', lheTree.vSum)
    
    if args.vbf:
            jj_mass = array( 'd', [ 0 ] ) ## one value
            lheTree.vq1in = ROOT.TLorentzVector(0., 0., 0., 0.)
            lheTree.vq2in = ROOT.TLorentzVector(0., 0., 0., 0.)
            lheTree.vq1out = ROOT.TLorentzVector(0., 0., 0., 0.)
            lheTree.vq2out = ROOT.TLorentzVector(0., 0., 0., 0.)
            lheTree.Branch( 'jj_mass', jj_mass, 'jj_mass/D' )
            lheTree.Branch( 'vq1in', lheTree.vq1in)
            lheTree.Branch( 'vq2in', lheTree.vq2in)
            lheTree.Branch( 'vq1out', lheTree.vq1out)
            lheTree.Branch( 'vq2out', lheTree.vq2out)

########################

H1 = (-999,-999,-999,-999) ## pt
H2 = (-999,-999,-999,-999)

if args.vbf:
    q1in  = (-999,-999,-999,-999) ## pt
    q2in  = (-999,-999,-999,-999) ## pt
    q1out = (-999,-999,-999,-999) ## pt
    q2out = (-999,-999,-999,-999) ## pt
    tlvSum_qout = ROOT.TLorentzVector(0,0,0,0)


tlv1 = ROOT.TLorentzVector(0,0,0,0)
tlv2 = ROOT.TLorentzVector(0,0,0,0)
tlvSum = ROOT.TLorentzVector(0,0,0,0)

#format
#       25  1    1    2    0    0 +3.2844847151e+01 -5.5017213033e+01 -3.5097027970e+02 3.7803546784e+02 1.2500000000e+02 0.0000e+00 0.0000e+00
## pdg ? ? ? ? ? px py pz e m ? ?

nev = 0
evtStart = False
for line in lheIn:
    # line = line.strip()
    if not evtStart:
        # an event will start from next line
        if '<event>' in line:
            evtStart = True
        continue
    else:
        ## event is finished
        if '</event>' in line:
            
            ## check it was filled
            if H1[0] == -999 and H1[1] == -999 and H1[2] == -999 and H1[3] == -999:
                print 'H1 invalid', H1
            if H2[0] == -999 and H2[1] == -999 and H2[2] == -999 and H2[3] == -999:
                print 'H2 invalid', H2

            if args.vbf:
                ## check it was filled
                if q1in[0] == -999 and q1in[1] == -999 and q1in[2] == -999 and q1in[3] == -999:
                    print 'q1in invalid', q1in
                if q2in[0] == -999 and q2in[1] == -999 and q2in[2] == -999 and q2in[3] == -999:
                    print 'q2in invalid', q2in
                if q1out[0] == -999 and q1out[1] == -999 and q1out[2] == -999 and q1out[3] == -999:
                    print 'q1out invalid', q1out
                if q2out[0] == -999 and q2out[1] == -999 and q2out[2] == -999 and q2out[3] == -999:
                    print 'q2out invalid', q2out


            ## compute mHH and fill tree
            # print "H1...", H1
            # print "H2...", H2
            # print ''

            tlv1.SetPxPyPzE(H1[0],H1[1],H1[2],H1[3])
            tlv2.SetPxPyPzE(H2[0],H2[1],H2[2],H2[3])

            tlvSum = tlv1 + tlv2
            # print tlvSum.Px(), tlvSum.Py(), tlvSum.Pz(), tlvSum.E()
            # print tlvSum.M()

            if tlvSum.M() < 250:
                print 'HH mass is smaller than 250!'
                print H1
                print H2
                print 'evt num', nev

            HH_mass[0] = tlvSum.M()

            if args.vbf:
                lheTree.vq1in.SetPxPyPzE(q1in[0],q1in[1],q1in[2],q1in[3])
                lheTree.vq2in.SetPxPyPzE(q2in[0],q2in[1],q2in[2],q2in[3])
                lheTree.vq1out.SetPxPyPzE(q1out[0],q1out[1],q1out[2],q1out[3])
                lheTree.vq2out.SetPxPyPzE(q2out[0],q2out[1],q2out[2],q2out[3])
                tlvSum_qout = lheTree.vq1out + lheTree.vq2out
                jj_mass[0] = tlvSum_qout.M()


            # print 'xxx', HH_mass
            nev += 1
            lheTree.Fill()

            # reset values
            evtStart = False
            H1 = (-999,-999,-999,-999)
            H2 = (-999,-999,-999,-999)
            if args.vbf:
                q1in  = (-999,-999,-999,-999) ## pt
                q2in  = (-999,-999,-999,-999) ## pt
                q1out = (-999,-999,-999,-999) ## pt
                q2out = (-999,-999,-999,-999) ## pt
            continue
        
        if '<' in line and '>' in line:
            continue ## metainfo I don't care about

        ## read the evts line
        line = line.strip()
        # print line
        tokens = line.split()
        pdg = int(tokens[0])
        
        ## let's decouple the parsing strategy - the one for ggF was already validated so let's not change it
        if not args.vbf:
            if pdg != 25:
                continue
            p4 = (float(tokens[6]),float(tokens[7]),float(tokens[8]),float(tokens[9]))

            if H1[0] == -999 and H1[1] == -999 and H1[2] == -999 and H1[3] == -999:
                H1 = p4
            elif H2[0] == -999 and H2[1] == -999 and H2[2] == -999 and H2[3] == -999:
                H2 = p4
            else:
                print "... too many Higgses!!" , H1, H2 

        if args.vbf:
            if len(tokens) != 13:
                continue ## there is a first line, I have no idea of what it is so let's skim
            
            p4 = (float(tokens[6]),float(tokens[7]),float(tokens[8]),float(tokens[9]))
            
            if pdg != 25: ## I assume these are only VBF partons: first two should be in (no higgs yet) and last two should be out (higgs found)
                if H1[0] == -999 and H1[1] == -999 and H1[2] == -999 and H1[3] == -999: ## no Higgs --> IN
                    if q1in[0] == -999 and q1in[1] == -999 and q1in[2] == -999 and q1in[3] == -999:
                        q1in = p4
                    elif q2in[0] == -999 and q2in[1] == -999 and q2in[2] == -999 and q2in[3] == -999:
                        q2in = p4
                    else:
                        print "... too many q in!!" , q1in, q2in
                else: ## Higgs already found --> OUT
                    if q1out[0] == -999 and q1out[1] == -999 and q1out[2] == -999 and q1out[3] == -999:
                        q1out = p4
                    elif q2out[0] == -999 and q2out[1] == -999 and q2out[2] == -999 and q2out[3] == -999:
                        q2out = p4
                    else:
                        print "... too many q out!!" , q1out, q2out

            else: ## the pdg 25 (Higgs)
                if H1[0] == -999 and H1[1] == -999 and H1[2] == -999 and H1[3] == -999:
                    H1 = p4
                elif H2[0] == -999 and H2[1] == -999 and H2[2] == -999 and H2[3] == -999:
                    H2 = p4
                else:
                    print "... too many Higgses!!" , H1, H2 


rootOut.cd()
lheTree.Write()
