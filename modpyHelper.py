# -*-
#
# @author: jaumebonet
# @email:  jaume.bonet@gmail.com
# @url:    jaumebonet.github.io
#
# @date:   2015-05-08 16:15:32
# @lab:    LPDI/EPFL
#
# @last modified by:   jaumebonet
# @last modified time: 2015-05-08 17:24:10
#
# -*-
import re

from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter


def basic_parser(*args, **kargs):
    '''
    Include those options that most likely are going to be shared
    by all (or most of) the modpy scripts.

    Advantages:
        1) Write less
        2) Homogenization of parameters

    @return: argparse.ArgumentParser object
    '''
    parser = ArgumentParser(ormatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('--pir', dest='alignment', type=str, action='store',
                        help="PIR formated alignment", metavar="PIR_FILE")

    parser.add_option("--out", dest="out", type=str, action="store",
                      default='seqNAME', metavar="OUT_PREFIX",
                      help="Prefix for the log and error file")
    parser.add_option("-v", dest="verbose", action="store_true",
                      default=False, help="Verbose Mode")
    return parser


def identify_pir(filename):
    '''
    Identify known structures and query sequence in the alignment.

    @return: {'str': [str(), ...], 'seq': str()}
    '''
    _idr = re.compile('^>\w+\;(\S+)')
    data = {'str': [], 'seq': None}

    with open(filename) as fd:
        for line in fd:
            m = _idr.match(line)
            if m:
                if fd.readline().startswith('strcutureX'):
                    data['str'].append(m.group(1).strip())
                else:
                    data['seq'].append(m.group(1).strip())
    return data
