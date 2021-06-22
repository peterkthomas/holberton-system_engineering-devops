#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - Infinite loop
 * @void: void
 *
 * Description: Loops infinitely
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Program entry point
 * @void: void
 *
 * Description: Program entry point
 * Return: 0
 */
int main(void)
{
	pid_t child;

	for (int i = 0; i < 5; i++)
	{
		child = fork();

		if (child)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
