#include "threads.h"

typedef struct Semaphore{
	int count;
	TCB_t* blockingQ;
}Semaphore_t;

Semaphore_t* CreateSem(int InputValue){
	Semaphore_t* sem = malloc(sizeof(Semaphore_t));
	InitQ(&(sem->blockingQ));
	sem->count = InputValue;
	return sem;
}

void P(Semaphore_t* sem){
	//Wait() operation
	sem->count--;
	if(sem->count<0){
		//block the process in the queue
		// i.e. block in *blockingQ
		TCB_t* newTCB = DelQ(&RunQ);
		AddQ(&(sem->blockingQ), newTCB);
		swapcontext(&((sem->blockingQ)->context),&(RunQ->context));
	}
}

void V(Semaphore_t* sem){
	//signal() Operation
	sem->count++;
	if(sem->count <= 0){
		// take the PCB from the semaphore to RunQ
		TCB_t* newTCB = DelQ(&(sem->blockingQ));
		AddQ(&RunQ,newTCB);
		//swapcontext(&((sem->blockingQ)->context),&(RunQ->context));
	}
	yield();
}
