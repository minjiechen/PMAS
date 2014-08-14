import math
import cmath
import numpy

def getImpe(*args):
  (sigma,mu0,mur)=MaterialInfo
  (NumofLayer,h,s,w,m)=WindingInfo
  (g,Ae,le,nc,c)=CoreInfo

  d=le*nc #effective length of the winding

  #check length of input matrices
  if NumofLayer!=len(h):
    print 'NumofLayer mismatch with h, please revise #layer or #h'
  if NumofLayer!=len(s):
    print 'NumofLayer mismatch with h\s, please revise #layer or #s'

  Xa=[]
  Xb=[]
  Xs=[]
  for i1 in range(NumofLayer):
    delta=(2/(f*2*math.pi)/mu0/sigma)**0.5
    Psi=complex(1/delta,1/delta)
    Z=Psi/sigma
    A=cmath.exp(-Psi*h[i1])
    Za=Z*(1-A)/(1+A)
    Zb=Z*2*A/(1-A**2)
    Xa.append(d/w[i1]*Za)
    Xb.append(d/w[i1]*Zb)
    Xs.append(complex(0,1)*(f*2*math.pi)*mu0*s[i1]*d/w[i1])

  #impedance for the ferrite core
  Xfb=complex(0,1)*(f*2*math.pi)*mu0*Ae/(g+Ae*w[i1]/(mur*c*d))
  Xft=complex(0,1)*(f*2*math.pi)*mu0*mur*c*d/w[i1]

  #calculate output
  Ra=numpy.array([e.real for e in Xa])
  La=numpy.array([e.imag for e in Xa])/(f*2*math.pi)
  Rb=numpy.array([e.real for e in Xb])
  Lb=numpy.array([e.imag for e in Xb])/(f*2*math.pi)
  Ls=numpy.array([e.imag for e in Xs])/(f*2*math.pi)
  Lfb=Xfb.imag/(f*2*math.pi)
  Lft=Xft.imag/(f*2*math.pi)

  return [Ra,La,Rb,Lb,Ls,Lfb,Lft]
