#include"sem.h"
#define N 10

typedef struct Message
{
	int data[10];
}mesg_t;

typedef struct Port
{
	int head, tail;
	Semaphore_t *prod, *cons, *mutex;
	mesg_t *buffer[N];
}port_t;

port_t portSet[100];

void initPort(port_t *port)
{
	int i = 0;
	port->head  = 0;
	port->tail = 0;

	port->mutex = CreateSem(1);
	port->prod = CreateSem(N);
	port->cons  = CreateSem(0);

	for ( i=0; i < 10; i++)
	{
		mesg_t* mesg  = (mesg_t*) calloc(10, sizeof(int));
		port->buffer[i] = mesg;
	}
}

void send (int portNo, mesg_t* mesg)
{
	port_t *port = &portSet[portNo];

	P(port->prod);
	P(port->mutex);

	port->buffer[port->tail] = mesg;
	port->tail = ((port->tail) + 1) % N;

	V(port->mutex);
	V(port->cons);	
}

mesg_t* receive (int portNo)
{
    	mesg_t *mesg = (mesg_t*)malloc(sizeof(mesg_t));
	port_t *port    = &portSet[portNo];

	P(port->cons);
	P(port->mutex);

	mesg = port->buffer[port->head];
	port->head = ((port->head) + 1) % N;

	V(port->mutex);
	V(port->prod);	

	return mesg;
}
