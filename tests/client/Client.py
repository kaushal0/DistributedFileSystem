#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import random

import dfs.client

if __name__ == '__main__':
    with dfs.client.open('/data/file', 'a') as f:
        f.write('%6d\n' % random.randint(0, 10 ** 10))
        try:
            open('/data/file')
        except:
            print('Exception..')
