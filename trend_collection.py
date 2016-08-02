import getopt
import posixpath
import pycurl
import os
import time
import collections
import traceback


def usage():
    print('usage: python license_sync.py [-h]'
          '[--server server] [--username username] [--password password] [--proxy proxy]'
          '[--dbhost dbhost] [--dbuser dbuser] [--dbpassword dbpassword]')
    print('arguments')
    print('--server SERVER,         :   server')
    print('--username USERNAME      :   username,')
    print('--password PASSWORD      :   password')
    print('--proxy PROXY            :   proxy')
    print('--dbhost DB HOST         :   db host')
    print('--dbuser DB USER         :   db account')
    print('--dbpassword DBPASSWORD  :   password of db account')
    print('example:\n'
          'python license_sync.py --server=https://plsdatasync.trendmicro.com/HMS'
                                  '--user=HMS --password=1qaz@WSX'
                                  '--dbhost=dcdb --dbuser=osdp_writer --dbpassword=safesync')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help',
                                                       'server=', 'username=', 'password=', 'proxy=',
                                                       'dbhost=', 'dbuser=', 'dbpassword='])
    except getopt.GetoptError as err:
        usage()
        sys.exit(-1)

    cfg = collections.namedtuple('config',
                                 [
                                    'pls_server',
                                    'pls_account',
                                    'pls_password',
                                    'proxy',
                                    'dbhost',
                                    'dbuser',
                                    'dbpassword'
                                 ],
                                 verbose=False)(pls_server=None, pls_account=None, pls_password=None, proxy=None,
                                                dbhost='dcdb', dbuser='osdpwriter', dbpassword='safesync')

    for o, a in opts:
        if o in ['--help', '-h']:
            usage()
            sys.exit(0)
        elif o in ['--server']:
            cfg = cfg._replace(pls_server=a)
        elif o in ['--username']:
            cfg = cfg._replace(pls_account=a)
        elif o in ['--password']:
            cfg = cfg._replace(pls_password=a)
        elif o in ['--proxy']:
            cfg = cfg._replace(proxy=a)
        elif o in ['--dbhost']:
            cfg = cfg._replace(dbhost=a)
        elif o in ['--dbuser']:
            cfg = cfg._replace(dbuser=a)
        elif o in ['--dbpassword']:
            cfg = cfg._replace(dbpassword=a)

    if not cfg.pls_server or not cfg.pls_account or not cfg.pls_password:
        usage()
        sys.exit(-1)