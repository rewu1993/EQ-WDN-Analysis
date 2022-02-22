demand_dict = {'residential': 2500/(24*60),
              'commercial':5000/(24*60)}

def m2_acre(a_m2):
    return a_m2/4046.8

def calc_demand(land_type,area,demand_dict):
    return area*demand_dict[land_type]

def find_discharge_node(block_id,block_node_info):
    block = block_node_info[block_node_info['block_id'] == block_id]
    return block['node_id'].item()