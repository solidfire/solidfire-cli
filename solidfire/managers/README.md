Manager modules for extending the client/cli
============================================

Currently for the CLI we're just leveraging the methods
in the solidfire_element_api.  In the future, resource
managers can be added here, and also picked up with
cli.commands.

We'd expect managers that tie some of the base methods
into more complex actions.  So for example, things like:
* backup
* replication



