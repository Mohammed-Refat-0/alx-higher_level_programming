#include "lists.h"
/**
 * check_cycle - check if a linked list is cyclic
 * @list: pointer to list to be checked
 * Return: 0 - no cycle, 1 - cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;

	while (list->next != NULL)
	{
		list = list->next;
		if (list == head)
		{
			return (1);
		}
	}
	return (0);
}
