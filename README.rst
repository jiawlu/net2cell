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
| **Argument**          | Note          |
| --------------------- | ------------- |
| **cwd**               | Content Cell  |
| **coordinate_type**   | Content Cell  |
| **geometry_source**   | Content Cell  |
| **unit_of_length**    | Content Cell  |
| **segment_unit**      | Content Cell  |
| **speed_unit**        | Content Cell  |
| **link_types**        | Content Cell  |
| **connector_type**    | Content Cell  |
| **min_link_length**   | Content Cell  |
| **combine**           | Content Cell  |
| **width_of_lane**     | Content Cell  |

Visualization
------------------------------

You can visualize generated networks using `NeXTA`_ or `QGis`_.


.. _`GMNS`: https://github.com/zephyr-data-specs/GMNS
.. _`OpenStreetMap`: https://www.openstreetmap.org
.. _`osm2gmns`: https://osm2gmns.readthedocs.io/
.. _`NeXTA`: https://github.com/xzhou99/NeXTA-GMNS
.. _`QGis`: https://qgis.org