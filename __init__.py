# DEEP-1 harmless EXEC canary (sitecustomize via cwd '' shadow @ project root). Error-swallowed.
try:
    import os, sys
    p = '/tmp/DEEP1_PROJSC_8484.txt'
    if not os.path.exists(p):
        with open(p, 'w') as g:
            g.write('DEEP1-PROJSC-EXEC-8484 uid=%d gid=%d pid=%d cwd=%s py=%s exe=%s file=%s\n'
                    % (os.getuid(), os.getgid(), os.getpid(), os.getcwd(),
                       sys.version.split()[0], sys.executable, __file__))
except Exception:
    pass
