from .initnet import CInitNet
from .netgen import CNetGenerator
from .outputnet import *
from .util import exitProgram
from .settings import *


def readMacroNet(cwd='', coordinate_type='ll', geometry_source='l', unit_of_length='m', segment_unit='m', speed_unit='mph',
                 link_types=None, connector_type=None, min_link_length=3.0, combine=False, width_of_lane=3.5):

    if coordinate_type not in ['m', 'll', 'f']:
        print('ERROR: coordinate_type must be chosen from m,ll,f')
        exitProgram()
    if geometry_source not in ['n', 'l', 'g']:
        print('ERROR: geometry_source must be chosen from n,l,g')
        exitProgram()
    if unit_of_length not in ['m', 'km', 'mi', 'f']:
        print('unit_of_length must be chosen from m,km,mi,f')
        exitProgram()
    if segment_unit not in ['m', 'km', 'mi', 'f']:
        print('segment_unit must be chosen from m,km,mi,f')
        exitProgram()
    if speed_unit not in ['mph', 'kph']:
        print('speed_unit must be chosen from mph,kph')
        exitProgram()
    if speed_unit not in ['mph', 'kph']:
        print('speed_unit must be chosen from mph,kph')
        exitProgram()
    if (link_types is not None) and (not isinstance(link_types, list)):
        print('argument link_type_list must be a list')
        exitProgram()
    if not (isinstance(min_link_length, int) or isinstance(min_link_length, float)):
        print('min_link_length must be an integer and float')
        exitProgram()
    if not isinstance(combine, bool):
        print('combine must be a bool')
        exitProgram()
    if not (isinstance(width_of_lane, int) or isinstance(width_of_lane, float)):
        print('width_of_lane must be an integer and float')
        exitProgram()
    if width_of_lane <= 0:
        print('width_of_lane must be positive')
        exitProgram()

    macro_net = CInitNet(cwd, coordinate_type, geometry_source, unit_of_length, segment_unit, speed_unit,
                         link_types, connector_type, min_link_length, combine, width_of_lane)
    macro_net.readInputData()
    macro_net.initialization()

    return macro_net


def generateHybridNets(macro_net, length_of_cell=7.0, auto_connection=True):
    net_generator = CNetGenerator(macro_net, length_of_cell, length_of_cut, macro_net.width_of_lane, auto_connection, cells_in_queue_area)
    net_generator.generateNet()
    outputNetworks(macro_net, net_generator, connector_geometry_for_output)
