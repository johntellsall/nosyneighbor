# nosyneighbor

Listen in to process on same node to see what they're up to.


## Background

Inspired by [Julia Evans](https://jvns.ca/blog/2017/12/02/taking-a-sabbatical-to-work-on-ruby-profiling-tools/):

> I’ve been frustrated for a long time by Ruby and Python’s available profiling tools. In C and Java, I can just attach to any program (`strace -p $PID`, `sudo perf record -g -p $PID`, attach with YourKit/VisualVM) and immediately start getting information about what the program is doing.

...

> There are 3 main things I would like to be easy to get from any program:

> - the current stack trace of the program (from every thread, say)
a memory profile of the program (how many of every object is being used?)
> - a sampled CPU profile / flamegraph of the program (what functions are being called the most?)

Also: [How to Spy on a Ruby program](https://jvns.ca/blog/2016/06/12/a-weird-system-call-process-vm-readv/)

# Nosyneighbor

Sniff another process's memory space, get information, like stack trace.

# Current Status

pre-alpha

There's a sample C "hello" program to listen to, and a Python sniffer in "nosy_orig.py".

# Usage: macOS

To get memory addresses, we need to 1) install the GDB debugger, and 2) sign it, so it can see user memory.

TBD

# Usage: Docker

    docker-machine start default

    eval $(docker-machine env)

    docker build -t nosy . && docker run -it nosy bash

# NOTES

## get symbol address with gdb debugger

Note we've compiled the "chat" program with symbols, which isn't normally the case with most programs.

	gdb chat
	(gdb) p &chat_name
	$3 = (char **) 0x601048 <chat_name>

## get symbol address with objdump

	objdump -t chat | egrep _name
	0000000000601048 g     O .bss	0000000000000008              chat_name


## start sniffee in background

	./chat >/dev/null &

## run sniffer, giving sniffee information

Example only, your process ID and symbol values will be different.

	python3 ./nosy_orig.py 9 0x601048

