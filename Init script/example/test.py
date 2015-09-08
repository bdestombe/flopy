# Written by flopy init script

import numpy as np
import flopy

# In[Configure packages]

##############################################################################
# ml
modelname = 'modflowtest'
namefile_ext = 'nam'
version = 'mf2005'
exe_name = 'mf2005.exe'
structured = True
listunit = 2
model_ws = '.'
external_path = None
verbose = False
load = True
silent = 0

# Write package: ml
ml = flopy.modflow.mf.Modflow(modelname=modelname, namefile_ext=namefile_ext, version=version, exe_name=exe_name, structured=structured, listunit=listunit, model_ws=model_ws, external_path=external_path, verbose=verbose, load=load, silent=silent)


##############################################################################
# dis
model = ml
nlay = 41
nrow = 1
ncol = 88
nper = 730
delr = 1.0
delc = 10.0
laycbd = 0
top = 3.0
botm = np.load('C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\dis_botm.npy')
perlen = 1.0
nstp = 8
tsmult = 1.0
steady = False
itmuni = 4
lenuni = 2
extension = ['dis']
unitnumber = 11
xul = None
yul = None
rotation = 0.0

# Write package: dis
dis = flopy.modflow.mfdis.ModflowDis(model=ml, nlay=nlay, nrow=nrow, ncol=ncol, nper=nper, delr=delr, delc=delc, laycbd=laycbd, top=top, botm=botm, perlen=perlen, nstp=nstp, tsmult=tsmult, steady=steady, itmuni=itmuni, lenuni=lenuni, extension=extension, unitnumber=unitnumber, xul=xul, yul=yul, rotation=rotation)


##############################################################################
# bas6
model = ml
ibound = np.load('C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\bas6_ibound.npy')
strt = 0.0
ifrefm = False
ixsec = False
ichflg = False
stoper = None
hnoflo = 1e+30
extension = ['bas']
unitnumber = 13

# Write package: bas6
bas6 = flopy.modflow.mfbas.ModflowBas(model=ml, ibound=ibound, strt=strt, ifrefm=ifrefm, ixsec=ixsec, ichflg=ichflg, stoper=stoper, hnoflo=hnoflo, extension=extension, unitnumber=unitnumber)


##############################################################################
# lpf
model = ml
laytyp = 0
layavg = 0
chani = 1.0
layvka = 0
laywet = 0
ilpfcb = 53
hdry = 1e+20
iwdflg = 0
wetfct = None
iwetit = None
ihdwet = None
hk = np.load('C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\lpf_hk.npy')
hani = 0.0
vka = np.load('C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\lpf_vka.npy')
ss = 1e-05
sy = 0.0
vkcb = 0.0
wetdry = 0.0
storagecoefficient = False
constantcv = False
thickstrt = False
nocvcorrection = False
novfc = False
extension = ['lpf']
unitnumber = 15

# Write package: lpf
lpf = flopy.modflow.mflpf.ModflowLpf(model=ml, laytyp=laytyp, layavg=layavg, chani=chani, layvka=layvka, laywet=laywet, ilpfcb=ilpfcb, hdry=hdry, iwdflg=iwdflg, wetfct=wetfct, iwetit=iwetit, ihdwet=ihdwet, hk=hk, hani=hani, vka=vka, ss=ss, sy=sy, vkcb=vkcb, wetdry=wetdry, storagecoefficient=storagecoefficient, constantcv=constantcv, thickstrt=thickstrt, nocvcorrection=nocvcorrection, novfc=novfc, extension=extension, unitnumber=unitnumber)


##############################################################################
# wel
model = ml
ipakcb = 53
stress_period_data = np.load('C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\wel_stress_period_data.npy').all()
dtype = np.dtype([('k', '<i4'), ('i', '<i4'), ('j', '<i4'), ('flux', '<f4')])
extension = ['wel']
unitnumber = 20
options = []

# Write package: wel
wel = flopy.modflow.mfwel.ModflowWel(model=ml, ipakcb=ipakcb, stress_period_data=stress_period_data, dtype=dtype, extension=extension, unitnumber=unitnumber, options=options)


##############################################################################
# riv
model = ml
ipakcb = 53
stress_period_data = np.load('C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\riv_stress_period_data.npy').all()
dtype = np.dtype([('k', '<i4'), ('i', '<i4'), ('j', '<i4'), ('stage', '<f4'), ('cond', '<f4'), ('rbot', '<f4')])
extension = ['riv']
unitnumber = 18
options = []

# Write package: riv
riv = flopy.modflow.mfriv.ModflowRiv(model=ml, ipakcb=ipakcb, stress_period_data=stress_period_data, dtype=dtype, extension=extension, unitnumber=unitnumber, options=options)


##############################################################################
# oc
model = ml
ihedfm = 12
iddnfm = 12
chedfm = None
cddnfm = None
cboufm = None
compact = False
stress_period_data = np.load('C:\\Users\\Bas\\Google Drive\\CiTG MSc\\CIE5060 - Thesis\\scripts\\oc_stress_period_data.npy').all()
extension = ['oc', 'hds', 'ddn', 'cbc']
unitnumber = [14, 51, 52, 53]

# Write package: oc
oc = flopy.modflow.mfoc.ModflowOc(model=ml, ihedfm=ihedfm, iddnfm=iddnfm, chedfm=chedfm, cddnfm=cddnfm, cboufm=cboufm, compact=compact, stress_period_data=stress_period_data, extension=extension, unitnumber=unitnumber)


##############################################################################
# pcg
model = ml
mxiter = 200
iter1 = 200
npcond = 1
hclose = 0.0001
rclose = 0.0001
relax = 1.0
nbpol = 0
iprpcg = 5
mutpcg = 1
damp = 1.0
dampt = 0.0
ihcofadd = 0
extension = ['pcg']
unitnumber = 27

# Write package: pcg
pcg = flopy.modflow.mfpcg.ModflowPcg(model=ml, mxiter=mxiter, iter1=iter1, npcond=npcond, hclose=hclose, rclose=rclose, relax=relax, nbpol=nbpol, iprpcg=iprpcg, mutpcg=mutpcg, damp=damp, dampt=dampt, ihcofadd=ihcofadd, extension=extension, unitnumber=unitnumber)


##############################################################################
# mt
modelname = 'mt3dmstest'
namefile_ext = 'nam'
modflowmodel = None
ftlfilename = None
model_ws = None
external_path = None
verbose = False
load = True
listunit = 7
exe_name = 'mt3dms.exe'

# Write package: mt
mt = flopy.mt3d.mt.Mt3dms(modelname=modelname, namefile_ext=namefile_ext, modflowmodel=modflowmodel, ftlfilename=ftlfilename, model_ws=model_ws, external_path=external_path, verbose=verbose, load=load, listunit=listunit, exe_name=exe_name)


##############################################################################
# btn
model = mt
ncomp = 1
mcomp = 1
tunit = 'D'
lunit = 'M'
munit = 'KG'
prsity = 0.3
icbund = 1
sconc = 0.0
cinact = 1e+30
thkmin = 0.01
ifmtcn = 0
ifmtnp = 0
ifmtrf = 0
ifmtdp = 0
savucn = True
nprs = 0
timprs = None
obs = None
nprobs = 1
chkmas = True
nprmas = 1
dt0 = 0
mxstrn = 50000
ttsmult = 1.0
ttsmax = 0
species_names = []
extension = 'btn'

# Write package: btn
btn = flopy.mt3d.mtbtn.Mt3dBtn(model=mt, ncomp=ncomp, mcomp=mcomp, tunit=tunit, lunit=lunit, munit=munit, prsity=prsity, icbund=icbund, sconc=sconc, cinact=cinact, thkmin=thkmin, ifmtcn=ifmtcn, ifmtnp=ifmtnp, ifmtrf=ifmtrf, ifmtdp=ifmtdp, savucn=savucn, nprs=nprs, timprs=timprs, obs=obs, nprobs=nprobs, chkmas=chkmas, nprmas=nprmas, dt0=dt0, mxstrn=mxstrn, ttsmult=ttsmult, ttsmax=ttsmax, species_names=species_names, extension=extension)


##############################################################################
# adv
mixelm = 3
percel = 0.75
mxpart = 800000
nadvfd = 1
itrack = 3
wd = 0.5
dceps = 1e-05
nplane = 2
npl = 10
nph = 40
npmin = 5
npmax = 80
nlsink = 0
npsink = 15
dchmoc = 0.0001
extension = 'adv'

# Write package: adv
adv = flopy.mt3d.mtadv.Mt3dAdv(model=mt, mixelm=mixelm, percel=percel, mxpart=mxpart, nadvfd=nadvfd, itrack=itrack, wd=wd, dceps=dceps, nplane=nplane, npl=npl, nph=nph, npmin=npmin, npmax=npmax, nlsink=nlsink, npsink=npsink, dchmoc=dchmoc, extension=extension)


##############################################################################
# dsp
al = 0.01
trpt = 0.1
trpv = 0.01
dmcoef = 1e-09
extension = 'dsp'
multiDiff = False

# Write package: dsp
dsp = flopy.mt3d.mtdsp.Mt3dDsp(model=mt, al=al, trpt=trpt, trpv=trpv, dmcoef=dmcoef, extension=extension, multiDiff=multiDiff)


##############################################################################
# ssm
crch = None
cevt = None
stress_period_data = None
dtype = None
extension = 'ssm'

# Write package: ssm
ssm = flopy.mt3d.mtssm.Mt3dSsm(model=mt, crch=crch, cevt=cevt, stress_period_data=stress_period_data, dtype=dtype, extension=extension)


##############################################################################
# rct
isothm = 0
ireact = 0
igetsc = 1
rhob = 1800.0
prsity2 = 0.1
srconc = 0.0
sp1 = 0.0
sp2 = 0.0
rc1 = 0.0
rc2 = 0.0
extension = 'rct'

# Write package: rct
rct = flopy.mt3d.mtrct.Mt3dRct(model=mt, isothm=isothm, ireact=ireact, igetsc=igetsc, rhob=rhob, prsity2=prsity2, srconc=srconc, sp1=sp1, sp2=sp2, rc1=rc1, rc2=rc2, extension=extension)


##############################################################################
# gcg
mxiter = 1
iter1 = 50
isolve = 3
ncrs = 0
accl = 1
cclose = 1e-05
iprgcg = 0
extension = 'gcg'

# Write package: gcg
gcg = flopy.mt3d.mtgcg.Mt3dGcg(model=mt, mxiter=mxiter, iter1=iter1, isolve=isolve, ncrs=ncrs, accl=accl, cclose=cclose, iprgcg=iprgcg, extension=extension)


##############################################################################
# sw
modelname = 'mt3dmstest'
namefile_ext = 'nam'
modflowmodel = None
mt3dmsmodel = None
exe_name = 'swt_v4.exe'
model_ws = None
verbose = False
external_path = None

# Write package: sw
sw = flopy.seawat.swt.Seawat(modelname=modelname, namefile_ext=namefile_ext, modflowmodel=modflowmodel, mt3dmsmodel=mt3dmsmodel, exe_name=exe_name, model_ws=model_ws, verbose=verbose, external_path=external_path)


##############################################################################
# vdf
mtdnconc = 1
mfnadvfd = 1
nswtcpl = 1
iwtable = 1
densemin = 1.0
densemax = 1.025
dnscrit = 0.01
denseref = 1.0
denseslp = 0.025
firstdt = 0.001
indense = 0
dense = 1.0
extension = 'vdf'

# Write package: vdf
vdf = flopy.seawat.swtvdf.SeawatVdf(model=sw, mtdnconc=mtdnconc, mfnadvfd=mfnadvfd, nswtcpl=nswtcpl, iwtable=iwtable, densemin=densemin, densemax=densemax, dnscrit=dnscrit, denseref=denseref, denseslp=denseslp, firstdt=firstdt, indense=indense, dense=dense, extension=extension)


##############################################################################
# vsc
mt3dmuflg = -1
viscmin = 0
viscmax = 0
viscref = 0.0008904
nsmueos = 0
mutempopt = 2
mtmuspec = 1
dmudc = 1.923e-06
cmuref = 0
mtmutempspec = 1
amucoeff = [0.001, 1, 0.015512, -20, -1.572]
invisc = -1
visc = -1
extension = 'vsc'

# Write package: vsc
vsc = flopy.seawat.swtvsc.SeawatVsc(model=sw, mt3dmuflg=mt3dmuflg, viscmin=viscmin, viscmax=viscmax, viscref=viscref, nsmueos=nsmueos, mutempopt=mutempopt, mtmuspec=mtmuspec, dmudc=dmudc, cmuref=cmuref, mtmutempspec=mtmutempspec, amucoeff=amucoeff, invisc=invisc, visc=visc, extension=extension)


# In[Write input files]
ml.write_input()
mt.write_input()
sw.write_input()

# In[Run model]
success, buff = sw.run_model(silent=False)
