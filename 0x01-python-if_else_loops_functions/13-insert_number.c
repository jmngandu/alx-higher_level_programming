#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t)), *_head = *head;
listint_t *prev = _head;
if (!new_node)
return (NULL);
new_node->n = number;
if (!_head)
{
new_node->next = _head, *head = new_node;
return (new_node);
}
while (_head->next)
{
if (_head->n < number)
prev = _head, _head = _head->next;
else
break;
}
new_node->next = (_head->next) ? _head : NULL;
if (prev == _head)
*head = new_node;
else
{
if (_head->next)
prev->next = new_node;
else
_head->next = new_node;
}
return (new_node);
}
