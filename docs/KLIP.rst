.. _KLIP:

KLIP: Create an add-on for reusable units of content in Kotti
=============================================================

Proposer
    Andreas Kaiser (disko)

Seconder
    ?

Motivation
----------

Scope of the package is to provide support for reusable units of
content in Kotti that can be defined by either

-   a content manager (via Kotti UI) for "static" content or

-   the developer (by subclassing a base class and using the new
    package's API) for "dynamic" content units - i.e. such that have
    some additional logic.  E.g.: tag cloud, navigation, etc.

Assumptions
-----------

None.

Proposals & Implementation
--------------------------

-   The feature should be implemented as a separate package that is part of
    Klone bt can be also used as a add-on for plain Kotti.

-   Name of the package: kotti_panels.

-   Primary focus in phase 1 is API definition and documentation thereof.

-   Implementation will not start before docs and API are complete.

Risks
-----

None.

Participants
------------

-   Andreas Kaiser (disko)

Progress
--------

-   You can find the repo here: https://github.com/disko/kotti_panels/

Dependencies
------------

None.

