# @author       Jiawei Lu
# @email        jiaweil9@asu.edu
# @create date  2020/07/26 12:55
# @desc         [description]

import copy
import micronet
import mesonet

class CQueueArea:
    def __init__(self,ng):
        self.ng = ng
        self.cells_in_queue_area = ng.cells_in_queue_area
        self.macro_net = ng.macro_net

        self.number_of_micro_nodes = 0
        self.number_of_micro_links = 0
        self.number_of_meso_nodes = 0
        self.number_of_meso_links = 0

        self.micro_node_list = []
        self.micro_link_list = []
        self.meso_node_list = []
        self.meso_link_list = []

        self.meso_node_id_to_seq_no_dict = {}
        self.micro_node_id_to_seq_no_dict = {}
        self.meso_link_id_to_seq_no_dict = {}
        self.micro_link_id_to_seq_no_dict = {}

        self.meso_link_key_to_seq_no_dict = {}

    def initialize(self):
        self.number_of_micro_nodes = self.ng.number_of_micro_nodes
        self.number_of_micro_links = self.ng.number_of_micro_links
        self.number_of_meso_nodes = self.ng.number_of_meso_nodes
        self.number_of_meso_links = self.ng.number_of_meso_links

        self.micro_node_list, self.micro_link_list, self.meso_node_list, self.meso_link_list = \
            copy.deepcopy((self.ng.micro_node_list, self.ng.micro_link_list, self.ng.meso_node_list, self.ng.meso_link_list))

        # self.micro_node_list = copy.deepcopy(self.ng.micro_node_list)
        # self.micro_link_list = copy.deepcopy(self.ng.micro_link_list)
        # self.meso_node_list = copy.deepcopy(self.ng.meso_node_list)
        # self.meso_link_list = copy.deepcopy(self.ng.meso_link_list)

        self.meso_node_id_to_seq_no_dict = copy.deepcopy(self.ng.meso_node_id_to_seq_no_dict)
        self.micro_node_id_to_seq_no_dict = copy.deepcopy(self.ng.micro_node_id_to_seq_no_dict)
        self.meso_link_id_to_seq_no_dict = copy.deepcopy(self.ng.meso_link_id_to_seq_no_dict)
        self.micro_link_id_to_seq_no_dict = copy.deepcopy(self.ng.micro_link_id_to_seq_no_dict)

        self.meso_link_key_to_seq_no_dict = copy.deepcopy(self.ng.meso_link_key_to_seq_no_dict)


    def createQueueArea(self):
        for node in self.macro_net.node_list:
            if (node.control_type != 1) or (not node.valid): continue
            print('node id: {}'.format(node.node_id))
            for link_id in node.m_incoming_link_list:
                print('link id: {}'.format(link_id))
                macro_link = self.macro_net.link_list[self.macro_net.link_id_to_seq_no_dict[link_id]]
                print('link id: {}'.format(macro_link.link_id))
                meso_link_id = macro_link.meso_link_id_list[-1]
                meso_link = self.meso_link_list[self.meso_link_id_to_seq_no_dict[meso_link_id]]
                meso_node = self.meso_node_list[self.meso_node_id_to_seq_no_dict[meso_link.to_node_id]]
                for connector_id in meso_node.m_outgoing_link_list:
                    connector_seq_no = self.meso_link_id_to_seq_no_dict[connector_id]
                    connector = self.meso_link_list[connector_seq_no]
                    connector.valid = False
                    to_meso_node = self.meso_node_list[self.meso_node_id_to_seq_no_dict[connector.to_node_id]]
                    print('building new connector for the original connector {}'.format(connector.link_id))
                    min_nodes_in_lane = float('inf')
                    for i in range(connector.number_of_lanes):
                        nodes_in_lane = len(connector.micro_node_list[i])
                        if nodes_in_lane < min_nodes_in_lane: min_nodes_in_lane = nodes_in_lane
                    print('min nodes in lane: {}'.format(min_nodes_in_lane))

                    connector_start_x, connector_start_y = connector.geometry_list[0][0], connector.geometry_list[0][1]
                    connector_end_x, connector_end_y = connector.geometry_list[1][0], connector.geometry_list[1][1]
                    actual_cells = 0
                    if min_nodes_in_lane == 0:
                        mid_x_coord = (connector_start_x + connector_end_x) * 0.5
                        mid_y_coord = (connector_start_y + connector_end_y) * 0.5
                    else:
                        if min_nodes_in_lane < self.cells_in_queue_area:
                            actual_cells = min_nodes_in_lane - 1
                        else:
                            actual_cells = self.cells_in_queue_area
                        mid_x_coord = (connector_end_x - connector_start_x) / connector.length * self.ng.length_of_cell * actual_cells + connector_start_x
                        mid_y_coord = (connector_end_y - connector_start_y) / connector.length * self.ng.length_of_cell * actual_cells + connector_start_y

                    mid_meso_node = mesonet.CMesoNode()
                    mid_meso_node.node_id = self.number_of_meso_nodes
                    mid_meso_node.node_seq_no = self.number_of_meso_nodes
                    mid_meso_node.x_coord = mid_x_coord
                    mid_meso_node.y_coord = mid_y_coord
                    self.meso_node_list.append(mid_meso_node)
                    self.number_of_meso_nodes += 1
                    self.meso_node_id_to_seq_no_dict[mid_meso_node.node_id] = mid_meso_node.node_seq_no

                    meso_link1 = mesonet.CMesoLink()
                    meso_link1.link_id = self.number_of_meso_links
                    meso_link1.link_seq_no = self.number_of_meso_links
                    meso_link1.from_node_id = meso_node.node_id
                    meso_link1.to_node_id = mid_meso_node.node_id
                    meso_link1.number_of_lanes = connector.number_of_lanes
                    meso_link1.speed_limit = connector.speed_limit
                    meso_link1.lane_cap = connector.lane_cap
                    meso_link1.geometry_list = [(connector.geometry_list[0][0], connector.geometry_list[0][1]), (mid_meso_node.x_coord, mid_meso_node.y_coord)]
                    meso_link1.length = ((meso_link1.geometry_list[0][0] - meso_link1.geometry_list[1][0])**2 + (meso_link1.geometry_list[0][1] - meso_link1.geometry_list[1][1])**2)**0.5
                    meso_link1.main_node_id = connector.main_node_id
                    meso_link1.movement_str = connector.movement_str
                    self.meso_link_list.append(meso_link1)
                    self.number_of_meso_links += 1
                    self.meso_link_id_to_seq_no_dict[meso_link1.link_id] = meso_link1.link_seq_no

                    meso_link2 = mesonet.CMesoLink()
                    meso_link2.link_id = self.number_of_meso_links
                    meso_link2.link_seq_no = self.number_of_meso_links
                    meso_link2.from_node_id = mid_meso_node.node_id
                    meso_link2.to_node_id = to_meso_node.node_id
                    meso_link2.number_of_lanes = connector.number_of_lanes
                    meso_link2.speed_limit = connector.speed_limit
                    meso_link2.lane_cap = connector.lane_cap
                    meso_link2.geometry_list = [(mid_meso_node.x_coord, mid_meso_node.y_coord), (connector.geometry_list[1][0], connector.geometry_list[1][1])]
                    meso_link2.length = ((meso_link2.geometry_list[0][0] - meso_link2.geometry_list[1][0])**2 + (meso_link2.geometry_list[0][1] - meso_link2.geometry_list[1][1])**2)**0.5
                    meso_link2.main_node_id = connector.main_node_id
                    self.meso_link_list.append(meso_link2)
                    self.number_of_meso_links += 1
                    self.meso_link_id_to_seq_no_dict[meso_link2.link_id] = meso_link2.link_seq_no

                    if min_nodes_in_lane == 0:
                        # need to create a new micro node on each lane
                        for i in range(connector.number_of_lanes):
                            original_micro_link = connector.micro_link_list[i][0]
                            # original_micro_link = self.micro_link_list[original_micro_link.link_seq_no]
                            original_micro_link.valid = False
                            from_micro_node = self.micro_node_list[self.micro_node_id_to_seq_no_dict[original_micro_link.from_node_id]]
                            to_micro_node = self.micro_node_list[self.micro_node_id_to_seq_no_dict[original_micro_link.to_node_id]]

                            mid_micro_node = micronet.CMicroNode()
                            mid_micro_node.node_id = self.number_of_micro_nodes
                            mid_micro_node.node_seq_no = self.number_of_micro_nodes
                            mid_micro_node.x_coord = 0.5 * (from_micro_node.x_coord + to_micro_node.x_coord)
                            mid_micro_node.y_coord = 0.5 * (from_micro_node.y_coord + to_micro_node.y_coord)
                            mid_micro_node.meso_link_id = meso_link1.link_id
                            mid_micro_node.lane_no = i + 1
                            self.micro_node_list.append(mid_micro_node)
                            self.micro_node_id_to_seq_no_dict[mid_micro_node.node_id] = mid_micro_node.node_seq_no
                            # mesolink.micro_node_list[-1].append(micronode.node_id)
                            self.number_of_micro_nodes += 1

                            microlink1 = micronet.CMicroLink()
                            microlink1.link_id = self.number_of_micro_links
                            microlink1.link_seq_no = self.number_of_micro_links
                            microlink1.from_node_id = from_micro_node.node_id
                            microlink1.to_node_id = mid_micro_node.node_id
                            microlink1.meso_link_id = meso_link1.link_id
                            microlink1.length = ((from_micro_node.x_coord - mid_micro_node.x_coord)**2 + (from_micro_node.y_coord - mid_micro_node.y_coord)**2)**0.5
                            microlink1.speed_limit = meso_link1.speed_limit
                            microlink1.cell_type = 1  # //1:traveling; 2:changing
                            microlink1.additional_cost = 0.0
                            self.number_of_micro_links += 1
                            self.micro_link_list.append(microlink1)
                            # mesolink.micro_link_list[-1].append(microlink)

                            microlink2 = micronet.CMicroLink()
                            microlink2.link_id = self.number_of_micro_links
                            microlink2.link_seq_no = self.number_of_micro_links
                            microlink2.from_node_id = mid_micro_node.node_id
                            microlink2.to_node_id = to_micro_node.node_id
                            microlink2.meso_link_id = meso_link2.link_id
                            microlink2.length = ((mid_micro_node.x_coord - to_micro_node.x_coord)**2 + (mid_micro_node.y_coord - to_micro_node.y_coord)**2)**0.5
                            microlink2.speed_limit = meso_link2.speed_limit
                            microlink2.cell_type = 1  # //1:traveling; 2:changing
                            microlink2.additional_cost = 0.0
                            self.number_of_micro_links += 1
                            self.micro_link_list.append(microlink2)
                            # mesolink.micro_link_list[-1].append(microlink)

                    else:
                        # no new micro node is needed
                        for i in range(connector.number_of_lanes):
                            for j in range(len(connector.micro_node_list[i])):
                                micro_node = self.micro_node_list[connector.micro_node_list[i][j].node_seq_no]
                                if j < actual_cells:
                                    micro_node.meso_link_id = meso_link1.link_id
                                else:
                                    micro_node.meso_link_id = meso_link2.link_id
                            for j in range(len(connector.micro_link_list[i])):
                                micro_link = self.micro_link_list[connector.micro_link_list[i][j].link_seq_no]
                                if j < actual_cells:
                                    micro_link.meso_link_id = meso_link1.link_id
                                else:
                                    micro_link.meso_link_id = meso_link2.link_id
