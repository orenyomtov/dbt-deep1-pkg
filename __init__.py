# DEEP-1 harmless EXEC canary (sitecustomize via cwd '' shadow). Error-swallowed; cannot break the interpreter.
try:
    import os, sys
    d = os.path.dirname(__file__)
    with open(os.path.join(d, 'APPSCFIRED.txt'), 'w') as f:
        f.write('DEEP1-APPSC-EXEC-7373 uid=%d gid=%d pid=%d cwd=%s py=%s exe=%s file=%s\n'
                % (os.getuid(), os.getgid(), os.getpid(), os.getcwd(),
                   sys.version.split()[0], sys.executable, __file__))
    p = '/tmp/DEEP1_APPSC_7373.txt'
    if not os.path.exists(p):
        with open(p, 'w') as g:
            g.write('appsc-fired pid=%d cwd=%s\n' % (os.getpid(), os.getcwd()))
except Exception:
    pass
