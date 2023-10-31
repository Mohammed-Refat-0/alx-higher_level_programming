#include "lists.h"
/**
 * insert_node - insert number in a sorted linked list
 * @number: integer to insert
 * @head: pointer to head pointer
 * Return: address of newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *ptr;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else if (number <= (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else
	{
		ptr = *head;
		while (ptr->next != NULL)
		{
			if (ptr->n <= number && ptr->next->n >= number)
			{
				newnode->next = ptr->next;
				ptr->next = newnode;
				return (newnode);
			}
			ptr = ptr->next;
		}
		ptr->next = newnode;
		newnode->next = NULL;
		return (newnode);
	}
}
