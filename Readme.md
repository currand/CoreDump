# CoreDump

A system to retrieve, analyze and format coredump files for ETI Triad.</br>

<pre>
Usage:
  formatcore.py  [-c <configfile>] ([-p] | [-o <directory>] [-s <suffix>]) <coredumps>...

Arguments:
  coredumps    Coredump file(s) to process.  May be a file, directory, or wildcard

Options:
  -p                     Print output to screen
  -c <configfile>        Specify a configuration file.   [default: ./coredump.cfg]
  -o <directory>         Specifiy an output destination directory
  -s <suffix>            Specify a suffix for output files
</pre>
</br>

example:

1) Outputs a formatted core file based on the provided coredump

formatcore.py core.12345

2) Outputs a formatted core to STDOUT

formatcore.py -p core.12345

3) Outputs multiple core files found in ~/input to ~/output with a suffix of .output

formatcore.py -s .output -o ~/output ~/input/core.* 

here's a change
CoreDump
