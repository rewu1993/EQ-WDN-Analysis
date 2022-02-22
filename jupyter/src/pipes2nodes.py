import json
import pandas as pd
import geocoder
import numpy as np


class NodeRegistry():
    def __init__(self):
        self.nodes = {}
        self.id = 0
    def register(self,coord):
        if coord not in self.nodes:
            self.id +=1 
            self.nodes[coord] = self.id
            
    def node_id(self,coord):
        if coord in self.nodes:
            return self.nodes[coord]
        else:
            print ('node is not registered')
            return 0
        
    
def parse_pipe_nodes(p,node_register):
    coords = p['geometry']['coordinates'][0]
    start_coord,end_coord = tuple(coords[0]),tuple(coords[-1])
    
    node_register.register(start_coord)
    node_register.register(end_coord)
    
    return (node_register.node_id(start_coord),
           node_register.node_id(end_coord))
    
    
def active(p):
    return (p['properties']['LIFE_CYCLE_STATUS'] == 'AC')

def parse_pipe_id(p):
    return p['properties']['pipe_id']

def parse_pipe_length(p):
    return p['properties']['SHAPE_Length']

def parse_pipe_diameter(p):
    return p['properties']['NOMINALDIAMETER']

def parse_pipe_material(p):
    return p['properties']['MATERIALTYPE']

def parse_pipe_age(p):
    try :
        age = 2020-int(p['properties']['INSTALLATIONYEAR'])
    except:
        age = np.nan
    return age

def parse_roughness(p):
    try:
        C = int(p['properties']['ROUGHNESS'])
    except: 
        C = np.nan
    return C
    
