#include<stdio.h>
#include<stdlib.h>
#include "TCB.h"

int InitQ(TCB_t** Q){
	*Q = NULL;
	return 1;
}

int AddQ(TCB_t** Q, TCB_t *item){
	if(*Q==NULL){
		*Q = malloc(sizeof(TCB_t));
		(*Q)->context = item->context;
		(*Q)->next = *Q;
		(*Q)->prev = *Q;
		return 1;
	}
	else{
		TCB_t* newNode = malloc(sizeof(TCB_t));
		newNode->context = item->context;
		(((*Q)->prev)->next) = newNode;
		
		newNode->prev = (*Q)->prev;
		newNode->next = *Q;
		(*Q)->prev = newNode;
		return 1;
	}
	return -1;
}

TCB_t* DelQ(TCB_t** Q){
	TCB_t* out1 = malloc(sizeof(TCB_t));
	if(*Q==NULL){
		printf("Tried to delete from empty Queue\n");
	}
	else if((*Q) == (*Q)->next){
		out1 = *Q;
		*Q = NULL;
		return out1;
	}
	else{
		((*Q)->prev)->next = (*Q)->next;
		((*Q)->next)->prev = (*Q)->prev;
		out1 = *Q;
		*Q = (*Q)->next;
		return out1;
	}
	return out1;
}

int RotateQ(TCB_t** Q){
	if(*Q==NULL){
		printf("Queue is empty, Rotate Failed\n");
		return -1;
	}
	else{
		*Q = (*Q)->next;
		return 1;
	}
}
