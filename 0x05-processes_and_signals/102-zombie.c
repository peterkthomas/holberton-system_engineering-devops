/** 102-zombie.c
*   Creates 5 zombie processes and calls an infinite loop
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/** infinite_while
 * 	takes no parameters
 * 	performs an infinite loop
 */

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/** main()
 * Program entry point
 */

int main(void)
{
	pid_t child;

	for (int i=0; i < 5; i++)
	{
		child = fork();

		if(child)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(0);
	}

	infinite_while();

	return 0;
}
