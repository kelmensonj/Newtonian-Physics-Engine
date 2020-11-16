from random import uniform
import pandas

rowsParticles = []
rowsBangs = []  
LIST_INITS = []
NUM_PARTICLES = 10
NUM_STEPS = 5000

SIM_COL = ['x_pos','y_pos','z_pos','x_vel','y_vel','z_vel','mass']

ARCH_COL = ['x_pos_init','y_pos_init','z_pos_init','x_vel_init','y_vel_init','z_vel_init','mass_init']

        
def vectors(df):
    for particle1 in df.index:  #each row of df is a different particle's init at the bang
        G = 6.67*10**-11
        t = 1
	AX = 0
	AY = 0
	AZ = 0
	m1 = df['mass'][particle1]
        dix = df['x_pos'][particle1]
        diy = df['y_pos'][particle1]
        diz = df['z_pos'][particle1]
        vix = df['x_vel'][particle1]
        viy = df['y_vel'][particle1]
        viz = df['z_vel'][particle1]
        for particle2 in df.index:
            if particle2 != particle1:
		m2 = df['mass'][particle2]
                dx = df['x_pos'][particle2]
                dy = df['y_pos'][particle2]
                dz = df['z_pos'][particle2]
		dr = ((dx-dix)**2 + (dy-diy)**2 + (dz-diz)**2)**.5 
		F = G*m1*m2/dr	
		ax = F/m1*(dx-dix)/dr
		ay = F/m1*(dy-diy)/dr
		az = F/m1*(dz-diz)/dr
		AX += ax
		AY += ay
		AZ += az
	print(AX,AY,AZ)
        dfx = (vix*t + .5*AX*(t**2)) + dix
        dfy = (viy*t + .5*AY*(t**2)) + diy
        dfz = (viz*t + .5*AZ*(t**2)) + diz
        vfx = vix + AX*t
        vfy = viy + AY*t
        vfz = viz + AZ*t
        df['x_pos'][particle1] = dfx
        df['y_pos'][particle1] = dfy
        df['z_pos'][particle1] = dfz
        df['x_vel'][particle1] = vfx
        df['y_vel'][particle1] = vfy
        df['z_vel'][particle1] = vfz
    return df
        
def bang(num_particles):
    for i in range(num_particles):
	mass = uniform(0,1)
        x_pos_init = uniform(-10,10)
        y_pos_init = uniform(-10,10)
        z_pos_init = uniform(-10,10)
        x_vel_init = uniform(-1**10**2,1**10**2)
        y_vel_init = uniform(-1**10**2,1**10**2)    
        z_vel_init = uniform(-1**10**2,1**10**2)
        sim_init = [x_pos_init,y_pos_init,z_pos_init,x_vel_init,y_vel_init,z_vel_init,mass]
        LIST_INITS.append(sim_init)
    black_hole = [0,0,0,0,0,0,10000000000]
    LIST_INITS.append(black_hole)
    ARCH_DF = pandas.DataFrame(LIST_INITS,columns=ARCH_COL)
    SIM_DF = pandas.DataFrame(LIST_INITS,columns=SIM_COL)
    return ARCH_DF,SIM_DF
    
def timesteps(df, num_steps):
    for i in range(1,num_steps+1):
        df = vectors(df)
	df.to_csv('arch'+str(i)+'.csv')

	

def main():
    ARCH_DF,SIM_DF = bang(NUM_PARTICLES)
    SIM_DF.to_csv('arch'+str(0)+'.csv')
    timesteps(SIM_DF, NUM_STEPS)

main()
