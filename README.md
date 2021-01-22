# ChairDB

A small but CouchDB-compatible database implementation in Python. Also implements replication.

For more information, please read the [blog post](https://ma.rtendevri.es/chairdb.html).

## File overview

- blog: the source files for the blog post on ChairDB
- chairdb: the main package
	- chairdb.db: database interface implementations
		- chairdb.db.datatypes: error types and definition of ``Change``
		- chairdb.db.memory: the location of the InMemoryDatabase class
		- chairdb.db.multipart: a mixed/multipart implementation used by chairdb.db.remote
		- chairdb.db.remote: wraps the CouchDB HTTP API in an API similar to that exposed by .memory and .sql
		- chairdb.db.revtree: the location of the RevisionTree class
		- chairdb.db.shared: functions shared between database implementations
		- chairdb.db.sql: an (aio)sqlite implementation of the same API as defined in .memory
	- chairdb.server: an ASGI application that imitates a CouchDB installation using in-memory databases
		- chairdb.db: build_db_app() allows you to wrap any database in an ASGI app. So not just in-memory databases!
	- chairdb.replicate: the replicator implementation
	- chairdb.utils: miscellaneous helpers
- tests: contains the test suite
- LICENSE: Apache 2.0
- requirements.txt: install using ``pip -r requirements.txt``
- serve.sh: starts Uvicorn with the ASGI app defined in chairdb.server. Auto-reloads when changes are made.
- test.sh: run the test suites. Requires you to have a CouchDB instance running with two databases: activiteitenweger and brassbandwirdum. So rename some of your own to be called that, or search for those terms in the source so you can replace them.

