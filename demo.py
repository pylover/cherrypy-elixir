
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
        'engine.elixir.db_uri'    : 'sqlite:///demo.db'
    },
}

if __name__ == '__main__':
    #cherrypy.quickstart()
    
    cherrypy.config.update(_cp_config)
    cherrypy.tree.mount(Root(), '')
    cherrypy.engine.start()
    cherrypy.engine.block()
