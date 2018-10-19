import ROOT
from array import array

import argparse

def copy_tlv(copy_from, copy_to):
    copy_to.SetPxPyPzE(
        copy_from.Px(),
        copy_from.Py(),
        copy_from.Pz(),
        copy_from.E(),
    )

def is_uninit(p4):
    if p4[0] == -999 and p4[1] == -999 and p4[2] == -999 and p4[3] == -999:
        return True
    else:
        return False

def set_tlv_from_p4(tlv, p4):
    tlv.SetPxPyPzE(p4[0], p4[1], p4[2], p4[3])

def order_by_pt(p4_1, p4_2):
    v1 = ROOT.TLorentzVector()
    v2 = ROOT.TLorentzVector()
    set_tlv_from_p4(v1, p4_1)
    set_tlv_from_p4(v2, p4_2)
    if v1.Pt() > v2.Pt():
        return (p4_1, p4_2)
    else:
        return (p4_2, p4_1)

parser = argparse.ArgumentParser(description='Command line parser of parser')
#string opts
parser.add_argument('--lheIn',   dest='lheIn',   help='lhe file name', default=None)
parser.add_argument('--rootOut', dest='rootOut', help='root out file name', default=None)
parser.add_argument('--saveTLV', dest='saveTLV', help='save TLorentzVector', action='store_true', default=False)

args = parser.parse_args()

###################### making interactive
lheIn = open(args.lheIn)
rootOut = ROOT.TFile.Open(args.rootOut, 'recreate')
rootOut.cd()

#### vars
#### X(45) -> Y(35) H(35)

lheTree = ROOT.TTree('lheTree', 'lheTree')

lheTree.X_mass = array( 'd', [ 0 ] ) ## one value
lheTree.Y_mass = array( 'd', [ 0 ] ) ## one value
lheTree.H_mass = array( 'd', [ 0 ] ) ## one value

lheTree.vX  = ROOT.TLorentzVector(0., 0., 0., 0.)
lheTree.vY  = ROOT.TLorentzVector(0., 0., 0., 0.)
lheTree.vH  = ROOT.TLorentzVector(0., 0., 0., 0.)
lheTree.vYH = ROOT.TLorentzVector(0., 0., 0., 0.)

lheTree.vY_b1 = ROOT.TLorentzVector(0., 0., 0., 0.)
lheTree.vY_b2 = ROOT.TLorentzVector(0., 0., 0., 0.)
lheTree.vH_b1 = ROOT.TLorentzVector(0., 0., 0., 0.)
lheTree.vH_b2 = ROOT.TLorentzVector(0., 0., 0., 0.)

# make branches

lheTree.Branch( 'X_mass', lheTree.X_mass, 'X_mass/D')
lheTree.Branch( 'Y_mass', lheTree.Y_mass, 'Y_mass/D')
lheTree.Branch( 'H_mass', lheTree.H_mass, 'H_mass/D')

if args.saveTLV:
    lheTree.Branch( 'vX',  lheTree.vX)
    lheTree.Branch( 'vY',  lheTree.vY)
    lheTree.Branch( 'vH',  lheTree.vH)
    lheTree.Branch( 'vYH', lheTree.vYH)
    ## the decay b
    lheTree.Branch( 'vY_b1', lheTree.vY_b1)
    lheTree.Branch( 'vY_b2', lheTree.vY_b2)
    lheTree.Branch( 'vH_b1', lheTree.vH_b1)
    lheTree.Branch( 'vH_b2', lheTree.vH_b2)

#########################################

X_p4 = (-999,-999,-999,-999)
Y_p4 = (-999,-999,-999,-999)
H_p4 = (-999,-999,-999,-999)

X_idx = -1
Y_idx = -1
H_idx = -1

Y_b1_p4 = (-999,-999,-999,-999)
Y_b2_p4 = (-999,-999,-999,-999)
H_b1_p4 = (-999,-999,-999,-999)
H_b2_p4 = (-999,-999,-999,-999)



nev = 0
evtStart = False
ipart = 0
for line in lheIn:
    # line = line.strip()
    if not evtStart:
        # an event will start from next line
        if '<event>' in line:
            evtStart = True
            ipart    = -1
        continue
    else:
        ## event is finished
        if '</event>' in line:
            
            ## check it was filled
            if is_uninit(X_p4):
                print 'X invalid', X_p4
            if is_uninit(Y_p4):
                print 'Y invalid', Y_p4
            if is_uninit(H_p4):
                print 'H invalid', H_p4

            set_tlv_from_p4(lheTree.vX, X_p4)
            set_tlv_from_p4(lheTree.vY, Y_p4)
            set_tlv_from_p4(lheTree.vH, H_p4)
            copy_tlv(lheTree.vY + lheTree.vH, lheTree.vYH);

            Y_b1_p4, Y_b2_p4 = order_by_pt(Y_b1_p4, Y_b2_p4)
            H_b1_p4, H_b2_p4 = order_by_pt(H_b1_p4, H_b2_p4)

            set_tlv_from_p4(lheTree.vY_b1, Y_b1_p4)
            set_tlv_from_p4(lheTree.vY_b2, Y_b2_p4)
            set_tlv_from_p4(lheTree.vH_b1, H_b1_p4)
            set_tlv_from_p4(lheTree.vH_b2, H_b2_p4)

            lheTree.X_mass[0] = lheTree.vX.M()
            lheTree.Y_mass[0] = lheTree.vY.M()
            lheTree.H_mass[0] = lheTree.vH.M()

            # print 'xxx', HH_mass
            nev += 1
            lheTree.Fill()

            # reset values
            evtStart = False
            X_p4 = (-999,-999,-999,-999)
            Y_p4 = (-999,-999,-999,-999)
            H_p4 = (-999,-999,-999,-999)

            X_idx = -1
            Y_idx = -1
            H_idx = -1

            Y_b1_p4 = (-999,-999,-999,-999)
            Y_b2_p4 = (-999,-999,-999,-999)
            H_b1_p4 = (-999,-999,-999,-999)
            H_b2_p4 = (-999,-999,-999,-999)

            continue
        
        if '<' in line and '>' in line:
            continue ## metainfo I don't care about

        ipart += 1 ### update particle index

        ## read the evts line
        line = line.strip()
        # print line
        tokens = line.split()
        pdg = int(tokens[0])

        good = [25, 35, 45, 5]
        if (abs(pdg) not in good):
            continue
        p4  = (float(tokens[6]),float(tokens[7]),float(tokens[8]),float(tokens[9]))
        thisidx = ipart
        imother = int(tokens[2])

        if pdg == 45:
            X_p4 = p4
            X_idx = thisidx     
        elif pdg == 35:
            Y_p4 = p4     
            Y_idx = thisidx     
        elif pdg == 25:
            H_p4 = p4
            H_idx = thisidx     
        elif abs(pdg) == 5:
            if imother == Y_idx:
                if is_uninit(Y_b1_p4):
                    Y_b1_p4 = p4
                elif is_uninit(Y_b2_p4):
                    Y_b2_p4 = p4
                else:
                    print "... Y has too many b daughters?"
            elif imother == H_idx:
                if is_uninit(H_b1_p4):
                    H_b1_p4 = p4
                elif is_uninit(H_b2_p4):
                    H_b2_p4 = p4
                else:
                    print "... H has too many b daughters?"
            else:
                print "... cannot understand b mother?"

        else:
            print "... strangely a particle I was not expecting?", pdg

rootOut.cd()
lheTree.Write()
