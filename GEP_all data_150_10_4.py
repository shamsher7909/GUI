#------------------------------------------------------------------------
# Regression model generated by GeneXproTools 5.0 on 6/10/2023 6:32:24 PM
# GEP File: D:\Shamsher\Final_manscripts\02_GEP Predictive Model\Empirical\Final\GEP_all data_150_10_4.gep
# Training Records:  521
# Fitness  Function: RMSE
# Training Fitness:  7.5721083736664
# Training R-square: 0.412640005060632
#------------------------------------------------------------------------

from math import *

def gepModelqu(d):

	G1C2 = -3.48844627213141
	G1C5 = -6.20175817133091
	G2C6 = 5.49893271745485
	G2C5 = -4.29113855828654
	G2C9 = -3.95507070751173
	G2C2 = 3.49594053665271
	G3C0 = -7.14015242255928
	G3C7 = -9.77987402445779
	G4C2 = 7.15933713797418
	G4C8 = -6.18209711691404
	G4C9 = 4.90646790649796
	G4C7 = 3.12698433622949
	G4C0 = -5.74391414499274

	L = 0
	DD = 1
	i = 2
	sigma_v = 3
	c = 4
	phi = 5

	y = 0.0

	y = ((d[L]+(((d[phi]-d[i])+(d[sigma_v]+d[phi]))/2.0))+(G1C2/(((d[phi]/d[L])+G1C5)/2.0)))
	y = y + ((G2C6*((G2C9-G2C6)+(G2C2/d[DD])))+(((d[phi]+d[phi])-d[i])-(G2C5*d[c])))
	y = y + ((((d[L]/d[DD])-(G3C0*d[L]))-d[phi])/(((((G3C7+G3C7)+d[phi])/2.0)+(d[i]-d[phi]))/2.0))
	y = y + (((((G4C7*G4C7)/((d[c]+G4C0)/2.0))+((d[L]-d[DD])*d[i]))/2.0)-(((G4C2+G4C8)+(G4C9*d[i]))/2.0))

	return y
	

