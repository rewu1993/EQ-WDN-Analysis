import pandas as pd
import os

def parse_cast_iron(age):
    if age > 100:
        age = 100
    if age <= 10:
        return 110
    elif age <= 20:
        return 95
    elif age <= 30:
        return 80
    elif age <= 40:
        return 75
    else:
        return 50+int((age-40)*(5/12))
    
def get_HW_C(pipe_info):
    c = []
    for material,age in zip(pipe_info['material'],pipe_info['age']): 
        if material == 'A':
            c.append(140)
        elif material == 'C':
            c.append(parse_cast_iron(age))
        elif material == 'D':
            c.append(140)
        elif material == 'F':
            c.append(120)
        elif material == 'H':
            c.append(140)
        elif material == 'K':
            c.append(135)
        elif material == 'L':
            c.append(120)
        elif material == 'N':
            c.append(140)
        elif material == 'P':
            c.append(120)
        elif material == 'R':
            c.append(120)
        elif material == 'S':
            c.append(140)
        elif material == 'T':
            c.append(120)
        elif material == 'W':
            c.append(120)
        
    return c

def write_pipes(file_path,pipe_info,closing_pids):
    with open(file_path, 'a') as the_file:
        the_file.write('\n[PIPES]\n')
        the_file.write(';ID   Node1   Node2   Length   Diameter   Roughness   Minorloss   Status   \n')
        for index, pipe in pipe_info.iterrows():
            the_file.write("PIPE-"+str(pipe['pipe_id'])+'   ')
            the_file.write(str(pipe['node1']) +'   ')
            the_file.write(str(pipe['node2']) +'   ')
            the_file.write(str(pipe['length']) +'   ')
            the_file.write(str(pipe['diameter']) +'   ')
            the_file.write(str(pipe['C']) +'   ')
            the_file.write(str(0) +'   ')
            if pipe['pipe_id'] in closing_pids:
                print ("Closing pipe: ",pipe['pipe_id'])
                the_file.write('Closed' +'   ;\n')
            else:
                the_file.write('Open' +'   ;\n')
            
def write_reservors(file_path,src_nodes,head = 150):
    with open(file_path, 'a') as the_file:
        the_file.write('[RESERVOIRS]\n')
        the_file.write(';ID   Head   Pattern  \n')
        for nid in src_nodes:
            the_file.write(str(nid) +'   ')
            the_file.write(str(head) +'   ')
            the_file.write('   ;\n')

def write_junctions(file_path,node_info): 
    with open(file_path, 'a') as the_file:
        the_file.write('[JUNCTIONS]\n')
        the_file.write(';ID   Elev   Demand   Pattern  \n')
        for index, node in node_info.iterrows():
            the_file.write(str(node['node_id']) +'   ')
            the_file.write(str(node['elevation']) +'   ')
            the_file.write(str(node['demand']) +'   ')
            the_file.write('   ;\n')

def write_pumps(file_path,pump_info):
    with open(file_path, 'a') as the_file:
        the_file.write('\n[PUMPS]\n')
        the_file.write(';ID   Node1   Node2   Parameters   \n')
        if pump_info:
            for index, pump in pump_info.iterrows():
                the_file.write("PUMP-"+str(pump['nearest_pipes'])+'   ')
                the_file.write(str(pump['node1']) +'   ')
                the_file.write(str(pump['node2']) +'   ')
                the_file.write('HEAD '+str(pump['curve_id']) +'   ;\n')
            
def write_curves(file_path,curve_info):
    with open(file_path, 'a') as the_file:
        the_file.write('\n[CURVES]\n')
        the_file.write(';ID   X-Value   Y-Value   \n')
        if curve_info:
            for index, curve in curve_info.iterrows():
                the_file.write(str(int(curve['curve_id'])) +'   ')
                the_file.write(str(curve['Q']) +'   ')
                the_file.write(str(curve['H']) +'   ;\n')
            

def add_post_fix(file_path,prototype_path = '../data/EBMUD-DATA/inp-post-fix.txt'):
    with open(prototype_path,'r') as f:
        lines = f.readlines()
    with open(file_path, 'a') as the_file:
        for line in lines:
            the_file.write(line)
        
            
    
def write_inp(file_path,node_info,src_nodes,pipe_info,pump_info = None,curve_info = None,closing_pids = []):
    if os.path.exists(file_path):
        os.remove(file_path)
        print ('Overwrite previous file')
    write_junctions(file_path,node_info)
    write_reservors(file_path,src_nodes)
    write_pipes(file_path,pipe_info,closing_pids)
    write_pumps(file_path,pump_info)
    write_curves(file_path,curve_info)
    add_post_fix(file_path)
    print ('Done!')
    
    
        