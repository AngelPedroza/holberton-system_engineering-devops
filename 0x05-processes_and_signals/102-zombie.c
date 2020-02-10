#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - infinity loop
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
 * main - create a 5 zombie process
 * Return: 0
 */
int main(void)
{
	int pid, i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %u\n", pid);
		else
			return (0);
	}
	infinite_while();
	return (0);
}
