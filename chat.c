#include <stdio.h>
#include <unistd.h>


char* chat_name = NULL;
int chat_num = 0;

int main(int argc, char **argv)
{
    chat_name = argv[0];

	for (int chat_num = 0; chat_num < 1000; chat_num++) {
		printf("%s %d\n", chat_name, chat_num);
        sleep(1);
	}
 	return 0;
}