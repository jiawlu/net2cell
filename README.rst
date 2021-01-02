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


.. table:: Arguments of function ``readMacroNet()``
    :class: classic

    +----------------+---------------+----------+---------------------------------------------------------------+
    |      Field     |      Type     | Required?|                           Comments                            |
    +================+===============+==========+===============================================================+
    |      name      |     string    |          |                                                               |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |    link_id     |      int      |   yes    | unique key                                                    |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |   osm_way_id   | string or int |          | corresponding way id in osm data                              |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |  from_node_id  |      int      |   yes    |                                                               |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |   to_node_id   |      int      |   yes    |                                                               |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |    dir_flag    |     enum      |          | 1: forward, -1: backward, 0:bidirectionial                    |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |     length     |     float     |          | unit: meter                                                   |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |      lanes     |      int      |          |                                                               |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |   free_speed   |     float     |          |                                                               |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |    capacity    |     float     |          | unit: veh/hr/lane                                             |
    +----------------+---------------+----------+---------------------------------------------------------------+
    | link_type_name |     string    |          |                                                               |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |    link_type   |       int     |          |                                                               |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |    geometry    |     Geometry  |          | `wkt`_                                                        |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |  allowed_uses  |      enum     |          | auto, bike, walk                                              |
    +----------------+---------------+----------+---------------------------------------------------------------+
    |   from_biway   |      bool     |          | 1: link created from a bidirectional way, 0: not              |
    +----------------+---------------+----------+---------------------------------------------------------------+


Visualization
------------------------------

You can visualize generated networks using `NeXTA`_ or `QGis`_.


.. _`GMNS`: https://github.com/zephyr-data-specs/GMNS
.. _`OpenStreetMap`: https://www.openstreetmap.org
.. _`osm2gmns`: https://osm2gmns.readthedocs.io/
.. _`NeXTA`: https://github.com/xzhou99/NeXTA-GMNS
.. _`QGis`: https://qgis.org
.. _`wkt`: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry