#!/usr/bin/env python

import os.path
import plistlib
import subprocess

PREF = os.path.expanduser("~/Library/Preferences/com.github.filipp.offlink.plist")

def open_plist():
    try:
        return plistlib.readPlist(PREF)
    except Exception:
        d = dict(folders=[])
        return plistlib.writePlist(d, PREF)

def is_linked(path):
    """
    Returns True if path is in the linked list

    >>> is_linked("/tmp2")
    False
    """
    plist = open_plist()
    for x in plist['folders']:
        if x['source'] == path:
            return True
    return False

def add_path(source, target):
    """
    Adds source and target to list of synced folders

    >>> add_path('/blaa', '/bluu') #doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError...
    >>> add_path('/var', '/tmp')
    /var linked with /tmp
    """
    plist = open_plist()
    for path in (source, target,):
        if not os.path.exists(path):
            raise ValueError("%s is not a valid path" % path)
    f = dict(source=source, target=target)
    plist['folders'] = plist['folders'] + [f]
    plistlib.writePlist(plist, PREF)

    print("%s linked with %s" % (source, target))

def forget_path(path):
    """
    Removes this source from the linked folders list

    >>> forget_path("/var")
    /var removed from synced list
    """
    plist = open_plist()
    newlist = []

    for x in plist['folders']:
        if x['source'] != path:
            newlist.append(x)
    plist['folders'] = newlist
    plistlib.writePlist(plist, PREF)

    print("%s removed from synced list" % path)

def sync(source, target):
    subprocess.call(["/usr/bin/rsync", "-auE", source, target])
    print("%s synced with %s" % (source, target))

def source_to_target():
    plist = open_plist()
    
    for x in plist['folders']:
        sync(x['source'], x['target'])

def target_to_source():
    plist = open_plist()

    for x in plist['folders']:
        sync(x['target'], x['source'])


if __name__ == '__main__':
    import sys
    import doctest

    if len(sys.argv) == 1:
        doctest.testmod()
        sys.exit()

    if sys.argv[1] == 'add':
        add_path(sys.argv[2], sys.argv[3])
    if sys.argv[1] == 'forget':
        forget_path(sys.argv[2])
    if sys.argv[1] == 'check':
        sys.exit(255) if is_linked(sys.argv[2]) else sys.exit(0)
    if sys.argv[1] == 'sync':
        source_to_target()
