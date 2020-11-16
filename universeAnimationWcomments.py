import bpy
import csv

#TODO: Add a GUI, read the entire dataframe as one csv file

#I'm importing bpy. This script will only work if you copy and paste it into a '.blend' file within the scripting workspace. With some minor modifications
#this could work headlessly.

NUM_PARTICLES = 10
NUM_STEPS = 5000

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.context.scene.frame_end = NUM_STEPS #Ample documention by Blender Foundation. These lines starting with 'bpy' use the blender API to delete
                                        #all the meshes in the blender scene and to set the final frame to 'NUM_STEPS'

data = csv.reader('xX_ARCH_Xx.csv') #In this repo there's a file named 'universeSimulation.py' which will create this csv file here

SIM_COL = ['x_pos','y_pos','z_pos','x_vel','y_vel','z_vel']

ARCH_COL = ['x_pos_init','y_pos_init','z_pos_init','x_vel_init','y_vel_init','z_vel_init']

def insertFrame():
    bpy.ops.object.select_all(action='SELECT') #selects all meshes
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale') #inserts a keyframe. Again, this is 'bpy' module
        
def moveMass(xs,ys,zs):
    i = 1 #setting an index
    bpy.ops.object.select_all(action='SELECT') #selecting all meshes
    for obj in bpy.context.selected_objects: #referencing each particle by its Blender Mesh Name, one by one
        bpy.ops.object.select_all(action='DESELECT') #deselecting all meshes
        name = obj.name #bpy module to get the mesh name
        bpy.data.objects[name].select_set(True) #selecting the mesh by name
        x_pos = float(xs[i])/100 #using the index here. This is bad. But because in the 'bang()' function all the objects were added iteratively, the same
                                 #list order is preserved. The first object selected here will always be the first mesh added in bang()
        y_pos = float(ys[i])/100
        z_pos = float(zs[i])/100 #Below here I'm just creating a new position for the selected object
        bpy.ops.transform.translate(value=(x_pos, y_pos, z_pos), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        i += 1
        
def bang(xs,ys,zs):
    for i in range(1,NUM_PARTICLES+1):
        x_pos = float(xs[i])/100
        y_pos = float(ys[i])/100
        z_pos = float(zs[i])/100
        bpy.ops.mesh.primitive_ico_sphere_add(location = (x_pos,y_pos,z_pos)) #key line, adding meshes and setting their locations
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subdivision") #just smoothing out the meshes, nothing important

    
def timesteps(num_steps):
    for i in range(0,num_steps+1):
        with open('/home/james/Universe_Simulation/arch'+str(i)+'.csv') as csvfile: 
            readCSV = csv.reader(csvfile, delimiter=',') #Sadly, being my first coding project, a 5000 frame animation requires opening 5000 csv files. Sorry
            xs = []
            ys = []
            zs = []
            for row in readCSV:
                x = row[1]
                y = row[2]
                z = row[3] #each csv has a row for each particle
                xs.append(x)
                ys.append(y)
                zs.append(z) #Just creating lists of x,y,z positions. 
        bpy.data.scenes["Scene"].frame_set(i*5) #Setting the current frame using the 'bpy' module
        if i == 0: #this is basically just checking to see if the particle meshes have been added yet
            bang(xs,ys,zs) #If the meshes haven't been added they have to be created
            insertFrame()
        else:
            moveMass(xs,ys,zs) #if its past the first frame, the particles must exist, and so existing meshes have their locations in 3D updated
            insertFrame()
    
def main():
    timesteps(NUM_STEPS)
    bpy.data.scenes["Scene"].frame_set(0)

main()
