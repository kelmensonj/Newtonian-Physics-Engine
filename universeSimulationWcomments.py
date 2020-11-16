from random import uniform
import pandas

############^Imports^#############

rowsParticles = [] #My first coding project, forgive the global variables
rowsBangs = []  
LIST_INITS = [] #This will be populated by the initial positions, velocities, and accelerations, and masses of various particles at the start of the simulation
NUM_PARTICLES = 10
NUM_STEPS = 5000 #Simulation timesteps

SIM_COL = ['x_pos','y_pos','z_pos','x_vel','y_vel','z_vel','mass'] #Column names

ARCH_COL = ['x_pos_init','y_pos_init','z_pos_init','x_vel_init','y_vel_init','z_vel_init','mass_init'] #More column names

        
def vectors(df):
    for particle1 in df.index:  #each row of df is a different particle's init at the bang
        G = 6.67*10**-11
        t = 1
	AX = 0
	AY = 0
	AZ = 0 #Initial acceleration is zero in x,y,z
	m1 = df['mass'][particle1]
        dix = df['x_pos'][particle1]
        diy = df['y_pos'][particle1]
        diz = df['z_pos'][particle1] #getting initial position vector
        vix = df['x_vel'][particle1]
        viy = df['y_vel'][particle1]
        viz = df['z_vel'][particle1] #getting initial velocity vector
        for particle2 in df.index: #This line will allow us to compare each particle to every other
            if particle2 != particle1: #but not itself
		m2 = df['mass'][particle2] #getting second particles mass
                dx = df['x_pos'][particle2]
                dy = df['y_pos'][particle2]
                dz = df['z_pos'][particle2] #getting second particles position
		dr = ((dx-dix)**2 + (dy-diy)**2 + (dz-diz)**2)**.5  ##3D Pythagorean theorem, gets distance between particles
		F = G*m1*m2/dr	#Another well known equation for calculating force of gravity
		ax = F/m1*(dx-dix)/dr #F=ma to calculate acceleration
		ay = F/m1*(dy-diy)/dr
		az = F/m1*(dz-diz)/dr
		AX += ax
		AY += ay
		AZ += az #updating the acceleration of the original particle, based on the masses and positions of all other particles. Frame drag ignored so velocity ignored
	print(AX,AY,AZ)
        dfx = (vix*t + .5*AX*(t**2)) + dix #d=vit + .5at^2, the displacement in x direction. Added to the initial x you get the final x position
        dfy = (viy*t + .5*AY*(t**2)) + diy
        dfz = (viz*t + .5*AZ*(t**2)) + diz
        vfx = vix + AX*t #vf = vi + at
        vfy = viy + AY*t
        vfz = viz + AZ*t 
        df['x_pos'][particle1] = dfx 
        df['y_pos'][particle1] = dfy
        df['z_pos'][particle1] = dfz
        df['x_vel'][particle1] = vfx
        df['y_vel'][particle1] = vfy
        df['z_vel'][particle1] = vfz #Coded this a long time ago but i dont like these lines. I believe it works because df isn't being modified inplace. It works though
    return df #returns the DataFrame. That's a snapshot of the universe at a point in time
        
def bang(num_particles):
    for i in range(num_particles):
	mass = uniform(0,1) #create a random mass for each particle 'i'
        x_pos_init = uniform(-10,10)
        y_pos_init = uniform(-10,10)
        z_pos_init = uniform(-10,10)
        x_vel_init = uniform(-1**10**2,1**10**2)
        y_vel_init = uniform(-1**10**2,1**10**2) #calculations using basic physics
        z_vel_init = uniform(-1**10**2,1**10**2) #creating more random initial positions and velocities, broken up into euclidean vectors
        sim_init = [x_pos_init,y_pos_init,z_pos_init,x_vel_init,y_vel_init,z_vel_init,mass]
        LIST_INITS.append(sim_init)
    black_hole = [0,0,0,0,0,0,10000000000] #creating a stabilizing force to produce a more interesting animation
    LIST_INITS.append(black_hole)
    ARCH_DF = pandas.DataFrame(LIST_INITS,columns=ARCH_COL)
    SIM_DF = pandas.DataFrame(LIST_INITS,columns=SIM_COL) #Turning the initialization vectors into a 'pandas DataFrame' object
    return ARCH_DF,SIM_DF
    
def timesteps(df, num_steps):
    for i in range(1,num_steps+1):
        df = vectors(df) #This function is going to step the simulation forward, returning a dataframe detailing the universe's next step
	df.to_csv('arch'+str(i)+'.csv') #saving each timestep as a csv file with a unique name pertaining to the current timestep

	

def main():
    ARCH_DF,SIM_DF = bang(NUM_PARTICLES) #Calling the function 'bang()' in order to start the simulation. 
    SIM_DF.to_csv('arch'+str(0)+'.csv') #This will create a CSV file of the initial state of this particular universe. The intention is to run 
                                        #algorithms and determine what initialization vectors produce desireable characteristics. For example, repetition
    timesteps(SIM_DF, NUM_STEPS)

main()
