#-*- coding: utf-8 -*-

import atexit
import logging
import os
import shelve

import web

import utils

class NameServer:
    #NameServer is responsible of the mapping between directory names and file servers.

    def GET(self, filepath):
        #Return a server which hold the directory in which filepath is located

        web.header('Content-Type', 'text/plain; charset=UTF-8')
        filepath = str(filepath)
        if filepath == '/':
            return '\n'.join('%s=%s' % (dirpath, _names[dirpath])
                    for dirpath in sorted(_names))

        dirpath = str(os.path.dirname(filepath))

        if dirpath in _names:
            return _names[dirpath]

        raise web.notfound('No file server serve this file.')


    def POST(self, dirpath):
        """See _update (with add=True)."""

        return _update(str(dirpath))

    def DELETE(self, dirpath):
        """See _update (with add=False)."""

        return _update(str(dirpath), False)


def _update(dirpath, add=True):
    #Add pair of directory/server to the name server if ADD= TRUE else REMOVE(DELETE)

    web.header('Content-Type', 'text/plain; charset=UTF-8')
    i = web.input()

    if 'srv' not in i:
        raise web.badrequest()

    srv = i['srv']

    if dirpath == '/':
        if 'dirs' not in i:
            raise web.badrequest()

        for dirpath in i['dirs'].split('\n'):
            if not dirpath:
                continue

            try:
                _update_names(dirpath, srv, add)
            except ValueError as e:
                logging.exception(e)

    else:
        try:
            _update_names(dirpath, srv, add)
        except ValueError as e:
            logging.exception(e)

    return 'OK'



def _update_names(dirpath, srv, add=True):
    #Just update the name dictionary and the database.
    if dirpath[-1] == '/':
        dirpath = os.path.dirname(dirpath)

    if add:
        logging.info('Update directory %s on %s.', dirpath, srv)
        _names[dirpath] = srv

    elif dirpath in _names:
        logging.info('Remove directory %s on %s.', dirpath, srv)
        del _names[dirpath]

    else:
        raise ValueError('%s wasn\'t not deleted, because it wasn\'t'
                         ' in the dictionnary/database.' % dirpath)


_config = {
            'dbfile': 'names.db',
         }

logging.info('Loading config file nameserver.dfs.json.')
utils.load_config(_config, 'nameserver.dfs.json')
_names = shelve.open(_config['dbfile'])

atexit.register(lambda: _names.close())
