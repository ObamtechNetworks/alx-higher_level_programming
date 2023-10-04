#include "lists.h"
/**
 * insert_node - inserts a number into a sorted linked list
 * @head: the head of the list
 * @number: the number to insert
 * Return: address of the new node, NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	/**initialize and create new node for the data to insert*/
	listint_t *new = NULL; /*new node*/
	listint_t *cur_node = NULL; /*to traverse the head node*/
	/**allocate space for new node*/
	new = malloc(sizeof(listint_t));
	if (new == NULL)/*malloc return*/
		return (NULL);
	new->n = number;/*set the data to insert*/
	/*set pointer to traverse head to point to head*/
	cur_node = *head;
	/*check for empty list or when val is greater/equal to number*/
	if (cur_node == NULL || cur_node->n >= number)
	{
		new->next = cur_node;/*set next of new to cur node8*/
		*head = new;/*set head to point to new node*/
		return (new);
	} /*next val frm head is nt NULL && less than number*/
	while (cur_node->next != NULL && cur_node->next->n < number)
	{/*logic is to move pointer to right position to insert*/
		cur_node = cur_node->next;
	}
	/*inser the node*/
	new->next = cur_node->next;
	cur_node->next = new;
	return (new);
}
