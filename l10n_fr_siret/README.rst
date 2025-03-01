===============================================
French company identity numbers SIRET/SIREN/NIC
===============================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:27b6008da585a28257daaf7c51479fb08d7e312068e3120dff519051f599e137
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Mature-brightgreen.png
    :target: https://odoo-community.org/page/development-status
    :alt: Mature
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--france-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-france/tree/14.0/l10n_fr_siret
    :alt: OCA/l10n-france
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-france-14-0/l10n-france-14-0-l10n_fr_siret
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-france&target_branch=14.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

The **l10n_fr** module from the official addons adds a *SIRET* field on partners, but it doesn't verify its validity. This module **l10n_fr_siret** adds several features:

* the validity of the SIRET is checked using its checksum.
* it adds **SIREN** and **NIC** fields (reminder: SIREN + NIC = SIRET). If you enter the SIRET, these 2 fields are automatically computed from SIRET.
* multi-site companies have a single SIREN and one SIRET per site i.e. one NIC per site. This module allows to enter a specific NIC on child partners.
* it adds a warning banner on the partner form view if another partner has the same SIREN.

.. figure:: https://raw.githubusercontent.com/OCA/l10n-france/14.0/l10n_fr_siret/static/description/partner_duplicate_warning.png
   :alt: Warning banner on partner form

**Table of contents**

.. contents::
   :local:

Usage
=====

On the Partner form, users will be able to enter:
* the SIREN and NIC numbers: the SIRET number will be computed automatically.
* the SIRET number: the SIREN and NIC will be computed automatically.

The last digits of the SIREN and NIC are control keys: Odoo will check their validity.

The warning banner is displayed on the partner form view if another partner:
- has the same SIREN,
- if the partner is attached to a specific company: is in the same company or is not attached to a specific company,
- if the partner is not attached to a specific company: is in any company or not attached to a specific company.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-france/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-france/issues/new?body=module:%20l10n_fr_siret%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Numérigraphe
* Akretion

Contributors
~~~~~~~~~~~~

* Lionel Sausin (Numérigraphe) <ls@numerigraphe.com>
* Alexis de Lattre <alexis.delattre@akretion.com>

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

This module is part of the `OCA/l10n-france <https://github.com/OCA/l10n-france/tree/14.0/l10n_fr_siret>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
