.. pymlconf documentation master file, created by
   sphinx-quickstart on Sat Apr 14 05:05:05 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cherrypy's Elixir Plugin
====================================

``CherrypyElixir`` is a cherrypy plugin that provides elixir functionalities on top of sqlalchemy , within cherrypy as a process bus plugin.

Example::

	import cherrypy
	import CherrypyElixir
	from elixir import Entity, String, Field, OneToMany, Unicode, ManyToOne
	CherrypyElixir.setup()
	
	
	# define models
	class Person(Entity):
	    name = Field(String(128))
	    addresses = OneToMany('Address')
	
	class Address(Entity):
	    email = Field(Unicode(128))
	    owner = ManyToOne('Person')
	
	
	class Root(object):
	    
	    @cherrypy.expose
	    @cherrypy.tools.elixir()
	    def index(self):
	        yield '<ul>'
	        for p in Person.query:
	            yield '<li>'
	            yield p.name
	            yield ' ' 
	            yield ','.join([a.email for a in p.addresses])
	            yield '</li>'
	        yield '</ul>'
	
	    @cherrypy.expose
	    @cherrypy.tools.elixir()
	    def add(self,name=None,address=None):
	        p = Person(name = name)
	        for addr in address.split(','):
	            p.addresses.append(Address(email=addr))
	    
	_cp_config={
	    'global':{
	        'server.socket_host'  : '0.0.0.0', 
	        'server.socket_port'  : 1919,
	        'engine.elixir.on'    : True,
	        'engine.elixir.echo'    : True,
	        'engine.elixir.db_uri'    : 'postgresql+psycopg2://postgres:password@localhost/test'
	    },
	}
	
	if __name__ == '__main__':
	    cherrypy.quickstart(Root(), '', config=_cp_config) 
	    

To access sqlalchemy's ``scoped_session`` directly , you can use ``cherrypy.request.db``  
