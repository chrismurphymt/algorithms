CC=gcc
CFLAGS=-I.
DEPS = funcs.h

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)
	
graph: graphics.c funcs.c funcs.h
	$(CC) -o graph graphics.c funcs.c -I.
