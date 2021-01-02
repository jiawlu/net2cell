NET2CELL
========

For any given networks that meet the `GMNS`_ standard, net2cell helps users automatically build
mesoscopic and lane-by-lane cell-based microscopic transportation networks to accommdate different
modelling needs. For a quick start, users can easily get a network from `OpenStreetMap`_ (OSM)
using `osm2gmns`_, then use the network as an input of net2cell to obtain the corresponding hybrid
networks.

.. figure:: https://github.com/jiawei92/net2cell/blob/master/imgs/framework.png
    :name: framework
    :align: center
    :width: 100%

Installation
------------------------------

.. code-block:: bash

    pip install net2cell


Prepare macroscopic network
------------------------------

net2cell is compatible with any networks that meet the GMNS standard. Users can use their networks
at hand as inputs of net2cell, but the procedure of conversion to GMNS format may be needed before
feeding them to net2cell. For a quick start, users are recommended to use osm2gmns to quickly get
a macroscopic from OpenStreetMap (OSM). osm2gmns helps users easily convert the OSM map data to node
and link network files in the GMNS format.

Use net2cell
------------------------------

Get hybrid networks

.. code:: python

    >>> import net2cell as nc

    >>> macro_net = nc.readMacroNet()
    >>> nc.generateHybridNets(macro_net)

Arguments of function ``readMacroNet()``:
.. table::
    :class: classic

    +-------------+---------------+----------+---------------------------------------------------------------+
    |    Field    |      Type     | Required?|                           Comments                            |
    +=============+===============+==========+===============================================================+
    |    name     |     string    |          |                                                               |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |  node_id    |       int     |   yes    | unique key                                                    |
    +-------------+---------------+----------+---------------------------------------------------------------+
    | osm_node_id | string or int |          | corresponding point id in osm data                            |
    +-------------+---------------+----------+---------------------------------------------------------------+
    | osm_highway |     string    |          | point type in osm data                                        |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |  zone_id    |       int     |          |                                                               |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |  ctrl_type  |       int     |          | 1: Signalized; 0: not                                         |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |  node_type  |     string    |          |                                                               |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |activity_type|     string    |          | defined by adjacent links                                     |
    +-------------+---------------+----------+---------------------------------------------------------------+
    | is_boundary |      bool     |          | 1: boundary; 0: not                                           |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |  x_coord    |     double    |   yes    | WGS 84 is used in osm                                         |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |  y_coord    |     double    |   yes    | WGS 84 is used in osm                                         |
    +-------------+---------------+----------+---------------------------------------------------------------+
    | main_node_id|      int      |          | nodes belonging to one complex intersection have the same id  |
    +-------------+---------------+----------+---------------------------------------------------------------+
    |   poi_id    |      int      |          | id of the corresponding poi                                   |
    +-------------+---------------+----------+---------------------------------------------------------------+



Visualization
------------------------------

You can visualize generated networks using `NeXTA`_ or `QGis`_.


.. _`GMNS`: https://github.com/zephyr-data-specs/GMNS
.. _`OpenStreetMap`: https://www.openstreetmap.org
.. _`osm2gmns`: https://osm2gmns.readthedocs.io/
.. _`NeXTA`: https://github.com/xzhou99/NeXTA-GMNS
.. _`QGis`: https://qgis.org