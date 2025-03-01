==========================================
POS: Caisse-AP payment protocol for France
==========================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:a1ab6e38232fd67b589a22498e84e8336029abbc96cb4fba57a4244e159593b7
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--france-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-france/tree/14.0/l10n_fr_pos_caisse_ap_ip
    :alt: OCA/l10n-france
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-france-14-0/l10n-france-14-0-l10n_fr_pos_caisse_ap_ip
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-france&target_branch=14.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds support for the **Caisse AP** protocol over IP in the Odoo Point of Sale.

The `Caisse AP protocol <https://www.associationdupaiement.fr/protocoles/protocole-caisse/>`_ is a vendor-independent protocol used in France to communicate between a point of sale and a payment terminal. It is implemented by `Ingenico <https://ingenico.com/fr/produits-et-services/terminaux-de-paiement>`_ payment terminals, `Verifone <https://www.verifone.com/>`_ payment terminal and other brands of payment terminals. This protocol is designed by a French association called `Association du paiement <https://www.associationdupaiement.fr/>`_, abbreviated as **AP**. Note that the Caisse-AP protocol is used by Ingenico payment terminals deployed in France, but not by the same model of Ingenico payment terminals deployed in other countries!

This module support a bi-directionnal link with the payment terminal:

1. it sends the amount to the payment terminal
2. it waits for the end of the payment transaction
3. it parses the answer of the payment terminal which gives the payment status: in case of success, the payment line is automatically validated ; in case of failure, an error message is displayed and the Odoo user can retry or delete the payment line.

The Caisse-AP protocol was initially written for serial and USB. Since the Caisse AP protocol version 3.x, it also supports IP. When used over IP, the client (point of sale) and the server (payment terminal) exchange simple text data encoded as ASCII over a raw TCP socket.

The Caisse-AP protocol has one important drawback: as it uses a raw TCP socket, it cannot be used from pure JS code. So the JS code of the point of sale cannot generate the query to send the amount to the payment terminal by itself. In this module, the JS code of the point of sale sends a query to the Odoo server that opens a raw TCP socket to the payment terminal. It implies that, if the Odoo server is not on the LAN but somewhere on the Internet and the payment terminal has a private IP on the LAN, you will need to setup a TCP port forwarding rule on the firewall to redirect the TCP connection of the Odoo server to the payment terminal.

**Table of contents**

.. contents::
   :local:

Configuration
=============

In the menu *Point of sale > Configuration > Payment Method*, on the payment method that correspond to a payment by card:

* select the appropriate journal, which should be a bank journal (and not a cash journa, otherwise the field *Use a payment terminal* is invisible)
* field *Use a payment terminal*: select **Caisse AP over IP (France only)**
* field *Caisse-AP Payment Terminal IP Address*: set the IP address of the payment terminal,
* field *Caisse-AP Payment Terminal Port*: set the TCP port of the payment terminal (8888 by default),
* field *Payment Mode*: set *Card* (the value *Check* is for the *Check* payment method if you use a check printer connected to the payment terminal such as Ingenico i2200)

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-france/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-france/issues/new?body=module:%20l10n_fr_pos_caisse_ap_ip%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Akretion

Contributors
~~~~~~~~~~~~

* Alexis de Lattre <alexis.delattre@akretion.com>
* Pierrick Brun <pierrick.brun@akretion.com>

Other credits
~~~~~~~~~~~~~

The development of this module has been financially supported by `Camptocamp <https://www.camptocamp.com/>`_.

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-alexis-via| image:: https://github.com/alexis-via.png?size=40px
    :target: https://github.com/alexis-via
    :alt: alexis-via

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-alexis-via| 

This module is part of the `OCA/l10n-france <https://github.com/OCA/l10n-france/tree/14.0/l10n_fr_pos_caisse_ap_ip>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
