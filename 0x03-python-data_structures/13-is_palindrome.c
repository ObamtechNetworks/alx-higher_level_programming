#include "lists.h"
#include <stddef.h>
/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: the head of the reversed list
 */
void reverse_list(listint_t **head)
{
	/* set pointer to the head of the list as current*/
	listint_t *current = *head;
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
	*head = prev;
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
 * loop_slow_fast - loop for to compare slow and fast ptrof the list
 * @head: ptr to head of the list
 * @slw_ptr: the ptr to the head
 * @fst_ptr: ptr to mv twice the slw ptr
 * @prev_slw_ptr: previous of the slw ptr
 * @secnd_half: second half of the list
 * @mid_node: to identify the mid node
 * Return: returns result
 */
int loop_slow_fast(listint_t **head, listint_t *slw_ptr, listint_t *fst_ptr,
		listint_t *prev_slw_ptr, listint_t *mid_node,
		listint_t *secnd_half)
{
	int result = 1;

	slw_ptr = *head;
	fst_ptr = *head;
	prev_slw_ptr = *head;
	mid_node = NULL;
	while (fst_ptr && fst_ptr->next)
	{
		fst_ptr = fst_ptr->next->next;
		prev_slw_ptr = slw_ptr;
		slw_ptr = slw_ptr->next;
	}
	if (fst_ptr)
	{
		mid_node = slw_ptr;
		slw_ptr = slw_ptr->next;
	}
	secnd_half = slw_ptr;
	prev_slw_ptr->next = NULL; /*terminates first half*/
	reverse_list(&secnd_half); /*reverses the secnd_haf*/
	while (*head && secnd_half) /*compare*/
	{
		if ((*head)->n == secnd_half->n)
		{
			*head = (*head)->next;
			secnd_half = secnd_half->next;
		}
		else
		{
			result = 0;
			break;
		}
	}
	reverse_list(&secnd_half); /*construct original list back*/
	if (mid_node != NULL)
	{
		prev_slw_ptr->next = mid_node;
		mid_node->next = secnd_half;
	}
	else
		prev_slw_ptr->next = secnd_half;
	return (result);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: a pointer to the head of the list
 * Return: 1 if a palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw_ptr = NULL, *fst_ptr = NULL, *secnd_half = NULL,
		  *prev_slw_ptr = NULL;
	listint_t *mid_node = NULL; /*to handle odd size list*/
	int result = 1; /*initialize result*/

	if (!head || *head == NULL || (*head)->next == NULL)
		return (1);

	if (*head != NULL && (*head)->next != NULL)
	{
		result = loop_slow_fast(head, slw_ptr, fst_ptr, prev_slw_ptr,
				mid_node, secnd_half);
	}
	return (result);
}
