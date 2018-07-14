#include "q.h"

const int STACK_SIZE = 8192;
TCB_t* RunQ;

void start_thread(void (*function)(void))
{ 
/* begin pseudo code
allocate a stack (via malloc) of a certain size (choose 8192)
allocate a TCB (via malloc)
call init_TCB with appropriate arguments
call addQ to add this TCB into the “RunQ” which is a global header pointer
end pseudo code*/
	void* stack_p = malloc(STACK_SIZE);
	TCB_t *tcb = malloc(sizeof(TCB_t));
	init_TCB(tcb, function, stack_p, STACK_SIZE);
	AddQ(&RunQ, tcb);
}

void run()
{   // real code
    ucontext_t parent;     // get a place to store the main context, for faking
    getcontext(&parent);   // magic sauce
    swapcontext(&parent, &(RunQ->context));  // start the first thread
}

void yield() // similar to run
{
	RotateQ(&RunQ);
	swapcontext((&(RunQ->prev)->context),&(RunQ->context));
}

void abc(){
	TCB_t *tcb = DelQ(&RunQ);
	if(RunQ==NULL){
		ucontext_t parent;     // get a place to store the main context, for faking
    		getcontext(&parent);
		swapcontext(&(tcb->context),&parent);
	}
	else
		swapcontext(&(tcb->context),&(RunQ->context));
}
