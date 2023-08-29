#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

typedef struct dlistint_s
{
	int n;
	struct dlistint_s *prev;
	struct dlistint_s *next;
} dlistint_t;

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n);
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index);
void free_dlistint(dlistint_t *head);
size_t print_dlistint(const dlistint_t *h);

#endif /* LISTS_H */

