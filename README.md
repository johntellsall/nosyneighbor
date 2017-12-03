# nosyneighbor
Listen in to processes on same node to see what they're up to

From Julia Evans:

> I’ve been frustrated for a long time by Ruby and Python’s available profiling tools. In C and Java, I can just attach to any program (strace -p $PID, sudo perf record -g -p $PID, attach with YourKit/VisualVM) and immediately start getting information about what the program is doing.

...

> There are 3 main things I would like to be easy to get from any program:

> the current stack trace of the program (from every thread, say)
a memory profile of the program (how many of every object is being used?)
>a sampled CPU profile / flamegraph of the program (what functions are being called the most?)

# Nosyneighbor

Sniff another process's memory space, get information, like stack trace.

# Current Status

pre-alpha.  There's a sample C "hello" program to listen to, and a Python sniffer in "nosy_orig.py".

