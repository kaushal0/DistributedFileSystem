#-*- coding: utf-8 -*-

import logging
import os.path
import time

from contextlib import closing
from http.client import HTTPConnection

import web

import utils

class FileServer:
    #Fileserver for holding & sharing

    def GET(self, filepath):
        #Return the requested file if it's not locked

        web.header('Content-Type', 'text/plain; charset=UTF-8')
        return ''

    def PUT(self, filepath):
        #Replace the file by the data in the request.

        return ''

    def DELETE(self, filepath):
        #Remove the filepath if it's unlocked
        return ''

    def HEAD(self, filepath):
        #If the file exists/isn't locked, return the last-modified http header

        return ''
