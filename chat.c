#include <stdio.h>
#include <unistd.h>

int main(int argc, char **argv)
{
    const char* proc_name = argv[0];

	for (int i = 0; i < 1000; i++) {
		printf ("%s %d\n", proc_name, i);
        sleep(1);
	}
 	return 0;
}