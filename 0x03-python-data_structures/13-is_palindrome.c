#include "lists.h"
#include <stddef.h>
/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: the head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	/* set pointer to the head of the list as current*/
	listint_t *current = NULL;
	/* set another pointer to NULL as prev node*/
	listint_t *prev = NULL;
	/*set a next pointer to NULL, needed as next of current.next*/
	listint_t *next = NULL;
	/* EDGE CASES, FOR EMPTY LIST OR A SINGLE LIST*/
	if (head == NULL)
		return (NULL);
	current = head;
	/*traverse the list */
	while (current != NULL)
	{
		/*set next to be cur->next*/
		next = current->next;
		/*while moving forward, point backward*/
		current->next = prev;
		/*set prev to be the current*/
		prev = current;
		/* move to the next node to repeat reversal*/
		current = next;
	}
	/* return prev node*/
	return (prev);
}
/**
 * free_reverse - frees the reversed linked list
 * @head: pointer to the head of the node
 * Return: nothing
 */
void free_reverse(listint_t *head)
{
	listint_t *next = NULL;
	listint_t *current = head;
	while (current != NULL)
	{
		next = current->next;
		free(current);
		current = next;

	}
	head = NULL;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: a pointer to the head of the list
 * Return: 1 if a palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	/*start two pointers to point to the head*/
	listint_t *copy = *head;
	listint_t *reversed = NULL; /* to hold the reversed value*/

	/*check edge case of empty list or single node*/
	if ((*head) == NULL || ((*head)->next == NULL))
		return (1); /* it is a palindrome*/
	reversed = reverse_list(copy);
	/*now iterate through the list to compare the halves*/
	while (reversed != NULL && *head != NULL)
	{
		if ((*head)->n != reversed->n)
			return (0);
		(*head) = (*head)->next;
		reversed = reversed->next;
	}
	copy = NULL;
	free_reverse(reversed);
	return (1);
}
