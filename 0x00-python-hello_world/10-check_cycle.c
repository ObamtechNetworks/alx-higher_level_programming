#include "lists.h"
/**
 * check_cycle - checks if there is a cycle in a signly linked list
 * @lists: the linked list to check
 * Return: 0 if there's no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *lists)
{
	/*creat two pointers to the list*/
	listint_t *slow = lists;
	listint_t *fast = lists;

	/*traverse the pointers through the list*/
	/*move slow ptr 1 node at a time and fast two nodes*/
	while (slow != NULL && fast != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}
