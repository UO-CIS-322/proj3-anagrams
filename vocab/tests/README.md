# Nose tests #

Run as "nosetests" from the "vocab" directory.

Does not work from repo main directory (tests not found by
Nose). 

Does not work from within vocab/tests. 

If run within the "tests" subdirectory, import errors will occur because
the path does not include the files to be imported.  The documented
workaround for this is clumsy and fragile; I basically gave up on it.

