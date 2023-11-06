#include "lists.h"
#include <stddef.h>
/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: the head of the reversed list
 */
void reverse_list(listint_t *head)
{
	/* set pointer to the head of the list as current*/
	listint_t *current = head;
	/* set another pointer to NULL as prev node*/
	listint_t *prev = NULL;
	/*set a next pointer to NULL, needed as next of current.next*/
	listint_t *next = NULL;
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
	head = prev;
}
/**
 * free_reverse - frees the reversed linked list
 * @head: pointer to the head of the node
 * Return: nothing
 */
void free_reverse(listint_t *head)
{
	listint_t *current = head;
	listint_t *next = NULL;

	if (head)
	{
		while (current != NULL)
		{
			next = current->next;
			free(current);
			current = next;
		}
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
	listint_t *copy = NULL;
	listint_t *temp = NULL;

	if (!head || *head == NULL || (*head)->next == NULL)
		return (1);

	copy = *head;
	temp = *head;

	reverse_list(temp);
	/*iterate throught the list*/
	while (temp && copy)
	{
		if (copy->n != temp->n)
		{
			return (0);
		}
		copy = copy->next;
		temp = temp->next;
	}
	if (temp != NULL || copy != NULL) /*If either list has some el rema*/
		return (0);

	return (1);
}
