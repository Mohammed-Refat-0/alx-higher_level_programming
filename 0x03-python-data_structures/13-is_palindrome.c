#include "lists.h"
/**
 * reverse_listint - reverses a linked list
 * @head: pointer to head of list
 * Return: pointer to the first node in the reversed list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head pointer of linked list
 * Return: 0 if it is not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head, *temp = *head, *dup = NULL;

	if ((*head) == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	dup = ptr;

	reverse_listint(&dup);
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
	{
		return (1);
	}

	return (0);
}
