import bpy
import csv

NUM_PARTICLES = 10
NUM_STEPS = 5000

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.context.scene.frame_end = NUM_STEPS

data = csv.reader('xX_ARCH_Xx.csv')

SIM_COL = ['x_pos','y_pos','z_pos','x_vel','y_vel','z_vel']

ARCH_COL = ['x_pos_init','y_pos_init','z_pos_init','x_vel_init','y_vel_init','z_vel_init']

def insertFrame():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
        
def moveMass(xs,ys,zs):
    i = 1
    bpy.ops.object.select_all(action='SELECT')
    for obj in bpy.context.selected_objects:
        bpy.ops.object.select_all(action='DESELECT')
        name = obj.name
        bpy.data.objects[name].select_set(True)
        x_pos = float(xs[i])/100
        y_pos = float(ys[i])/100
        z_pos = float(zs[i])/100
        bpy.ops.transform.translate(value=(x_pos, y_pos, z_pos), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        i += 1
        
def bang(xs,ys,zs):
    for i in range(1,NUM_PARTICLES+1):
        x_pos = float(xs[i])/100
        y_pos = float(ys[i])/100
        z_pos = float(zs[i])/100
        bpy.ops.mesh.primitive_ico_sphere_add(location = (x_pos,y_pos,z_pos))
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers["Subdivision"].levels = 2
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subdivision")

    
def timesteps(num_steps):
    for i in range(0,num_steps+1):
        with open('/home/james/Universe_Simulation/arch'+str(i)+'.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            xs = []
            ys = []
            zs = []
            for row in readCSV:
                x = row[1]
                y = row[2]
                z = row[3]
                xs.append(x)
                ys.append(y)
                zs.append(z)
        bpy.data.scenes["Scene"].frame_set(i*5)
        if i == 0:
            bang(xs,ys,zs)
            insertFrame()
        else:
            moveMass(xs,ys,zs)
            insertFrame()
    
def main():
    timesteps(NUM_STEPS)
    bpy.data.scenes["Scene"].frame_set(0)

main()
