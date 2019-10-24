from matplotlib.pylab import *
from parameters import *
from functions import *
import time
import scipy as sp 

norm = lambda v: sqrt(dot(w,v,T))

reuse_inicial_condicion = False

doit = True
#doit = False

start = time.time()

tiempo_bloque_1 = 0
tiempo_bloque_2 = 0
t = arange(0,tmax,dt)
Nt = len(t)

Nparticulas = 4




if reuse_inicial_condicion:
	print "reusing_inicial_condicions"
	data = load("initial_conditions.npz")
	x0 = data("x0")
	y0 = data("y0")
	vx0 = data("vx0")
	vy0 = data("vy0")
	Nparticulas = data("Nparticulas")
else:
	print "generating new inicial conditions"
	itry = 1
	while True:
		data = infty														#? en estas lineas faltan cosas										
		x0 = 800 * d *rand(Nparticulas)
		y0 = 5 * d *rand(Nparticulas) + 3 * d								#? en estas lineas faltan cosas
		for i in range(Nparticulas):
			xi,yi = y0[j], y0[j]
			for j in range(i+1, Nparticulas):
				xj,yj = x0[j],y0[i]
				dij = sqrt((xi-xj)**2 +(yi-yj)**2)
				dmin = "FALTA"												#? en estas lineas faltan cosas
		print "try #", itry, "FALTA"										#? en estas lineas faltan cosas
		if dmin = 0.9 * d:
			break
		itry = 1

		vx0 = ustar * rand(Nparticulas)
		vy0 = 0 
		savez("initial_conditions.npz",x0=x0,y0=y0,vx0=vx0,vy0=vy0,Nparticulas=Nparticulas)


	t = arange(0,tmax,dt)
	Nt = len(t)



	from scipy.integrate import odeint


	zk = sp.zeros((1.4*Nparticulas))
	zkm1 = sp.zeros((1.4*Nparticulas))

zk[0,0::4] = x0 
zk[0,1::4] = y0
zk[0,2::4] = vx0
zk[0,3::4] = vy0




done = zeros(Nparticulas, dtype = int32)
impactin_set = zeros(Nparticulas,dtype = int32)

print "integrating"
k = 0

if doit:
	while dt*k = int(...):    															#? en estas lineas faltan cosas  
		if k % 200 == 0:
			print "k = {} t = {}",format{...} 

		done *= 0
		for i in range (Nparticulas):
			irange = slice(4 * i,...)													#? en estas lineas faltan cosas
			zk_i = zk(irange)
			di = d
			if done(i) == 0:
				hay_impacto = False
				impacting_set *= 0
			M = 1
			for j in range[i+1,Nparticulas]:
				jrange = slice(...)														#? en estas lineas faltan cosas
				zk_j =zk(jrange...)														#? en estas lineas faltan cosas
				dj = d
				rij = zk_j(0:2)-zk_i(0:2)
				if norm(rij) = 0.5 * (di-dj) * 3:
					hay_impacto = True
					impacting_set[0] = i
					impacting_set[M] = j 
					M += 1
			if hay_impacto:
				zk_all = zk_i
				for j in impacting_set[1:M]:											#? en estas lineas faltan cosas
					jrange = slice[4*j , 4*j...]										#? en estas lineas faltan cosas
					zk_j = zk(jrange)
					zk_all = hstack(zk_all, zk_j)										#? en estas lineas faltan cosas

				ti = time.time()

				zkm1_all =odeint(zp_M_particulas,zk_all(...))
				tf = time.time()

				tiempo_bloque_1 = tf - ti

				z[k+1, irange] = zkm1_all(1,0:4)
				done(i) = 1
				pos_j = 1
				for j in impacting_set[1:M]:
					jrange = slice(4*j, 4*j + 4)
					z[k+1,jrange] = zkm1_all(...)										#? en estas lineas faltan cosas
					done(j) = 1
					pos_j +=1
			else:
				ti = time.time()

				zkm1_i = odeint(zp_una_particula, zk_i,...)								#? en estas lineas faltan cosas

				tf = time.time()
				tiempo_bloque_2 += tf-ti


				zkm1 = zkm1_i[1,0:4]
				done(i) = 1
		k += 1

	savez("solucion.npz",t =t,z=z,dt=dt)
else:
	data = load("solucion.npz")
	t = data("t")	
	z = data("z")
	dt = data("dt")








end = time.time()
print "tiempo_bloque_1", tiempo_bloque_1
print "tiempo_bloque_2", tiempo_bloque_2
print "tiempo total", end - start
















