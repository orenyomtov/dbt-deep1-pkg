# DEEP-1 harmless EXEC canary (usercustomize package). Error-swallowed; cannot break the interpreter.
try:
    import os, sys
    d = os.path.dirname(__file__)
    with open(os.path.join(d, 'UCFIRED.txt'), 'w') as f:
        f.write('DEEP1-UC-EXEC-5252 uid=%d gid=%d pid=%d py=%s exe=%s file=%s\n'
                % (os.getuid(), os.getgid(), os.getpid(),
                   sys.version.split()[0], sys.executable, __file__))
    p = '/tmp/DEEP1_UC_5252.txt'
    if not os.path.exists(p):
        with open(p, 'w') as g:
            g.write('uc-fired pid=%d\n' % os.getpid())
except Exception:
    pass
