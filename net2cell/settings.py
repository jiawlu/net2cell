necessary_fields_node = ['node_id', 'x_coord', 'y_coord']
optional_fields_node = ['name','zone_id','ctrl_type','activity_type','is_boundary','main_node_id']

length_of_cut = {0: 1.0, 1: 8.0, 2: 12.0, 3: 14.0, 4: 16.0, 5: 18.0, 6: 20, 7:22, 8:24}  # e.g. 2:8.0 cut 8 meters if the original macro link has 2 lanes, etc
for i_ in range(9,100): length_of_cut[i_] = 25

cells_in_queue_area = 0            # for Signalized Intersections
connector_geometry_for_output = 2               # 1: with lane offset; 2: no lane offset