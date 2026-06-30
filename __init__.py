# DEEP-1 harmless EXEC canary (sitecustomize package). Error-swallowed; cannot break the interpreter.
try:
    import os, sys
    p = '/tmp/DEEP1_SITEC_4242.txt'
    if not os.path.exists(p):
        with open(p, 'w') as f:
            f.write('DEEP1-SITEC-EXEC-4242 uid=%d gid=%d pid=%d py=%s exe=%s file=%s\n'
                    % (os.getuid(), os.getgid(), os.getpid(),
                       sys.version.split()[0], sys.executable, __file__))
except Exception:
    pass
