#include "msgs.h"
#include<stdlib.h>

/*
* Message Passing Protocol
0 - The port on which it has to send an ACK
1 - Type of operation --> 1 - Add, 2 - Delete, 3 - Update , 4 - Print, 5 - ACK
2 - The index of the table that has to be added, updated or deleted.
3-9 - Is the string that will be added modified, deleted or printed
*/

Semaphore_t *mutex;

void server()
{
	//Message array snd initialized to string
	int i = 0;
	int j = 0;
	char table[10][7] = {"anirudh", "acharya", "anirudh", "acharya", "anirudh", "acharya", "anirudh", "anirudh", "acharya", "acharya"};


/*{{97, 110, 105, 114, 117, 100, 104},
				{97, 110, 105, 114, 117, 100, 104},
				{97, 110, 105, 114, 117, 100, 104},
				{97, 99, 104, 97, 114, 121, 97},
				{97, 99, 104, 97, 114, 121, 97},
				{97, 99, 104, 97, 114, 121, 97},
				{115, 97, 109, 97, 114, 116, 104},
				{115, 97, 109, 97, 114, 116, 104},
				{115, 97, 109, 97, 114, 116, 104},
				{100, 97, 118, 101, 0, 0, 0}};*/
	for(i=0 ; i<10 ; i++){
		for(j=0 ; j<7 ; j++){
			printf("%c",table[i][j]);
		}
		printf("\n");
	}

	int tail = 0;
	//int deleteIndex = 0;
	int flag=0;
	
	
	mesg_t* m = malloc(sizeof(mesg_t));
	int port = 5;
	Semaphore_t* S_mutex;	
	S_mutex = CreateSem(1);
    	while (1){
		flag = 0;
		m = receive(port);
		int recPort = m->data[0];	
		if(m->data[1]==1)
		{
			printf("\n\n*** Server *** received request to Add string at index %d *********\n", tail);
			P(mutex);
			for(j=0 ; j<7 ; j++){
				table[tail][j] = m->data[3+j];
			}
			tail = (tail+1)%10;
			V(mutex);
			m->data[1] = 5; // 5 is a ACK for ADD operation
			//strcpy(&(m->data[3], "ADD ACK");
			/*for(i=0 ; i<7 ; i++){
				printf("%c", table[tail-1][i]);
			}
			printf("\n");*/
			send(recPort, m);
		}
		
		else if(m->data[1]==2){
			printf("\n\n******* Server received request to Delete string: at index %d *******\n", tail);
			P(mutex);
			/*for(j=0 ; j<7 ; j++){
				table[tail][j] = 0;
			}*/
			if(tail==0){
				tail = 9;
			}
			else{
				tail = tail-1;
			}
			V(mutex);
			m->data[1] = 6;   // 6 is an ACK for DELETE operation
			//strcpy(&(m->data[3], "DEL ACK");
			/*for(i=0 ; i<7 ; i++){
				printf("%c", table[tail-1][i]);
			}*/
			send(recPort, m);	
		}
		
		else if(m->data[1]==3)
		{
			printf("\n\n******* Server received request to UPDATE string at %d *******\n",m->data[2]);
			int index = m->data[2];
			P(mutex);
			if(index<10&&index>=0){
				
				for(j=0 ; j<7 ; j++){
					table[index][j] = m->data[3+j];
				}
			}	
			V(mutex);	
			m->data[1] = 7; // 7 is ACK for UPDATE operation
			/*for(i=0 ; i<7 ; i++){
				printf("%c", table[tail-1][i]);
			}*/
			send(recPort, m);
		}
		
		else if(m->data[1]==4)
		{
			printf("\n\n********* Server received request to PRINT table. ********\n\n");
			/*for(i=0 ; i<10 ; i++){
				for(j=0 ; j<7 ; j++){
					printf("%c",table[i][j]);
				}
				printf("\n");
			}*/
			P(mutex);
			for(i=0;i<10;i++){
				for(j=0 ; j<7 ; j++){
					m->data[j+3] = table[i][j];
				}
				m->data[1] = 8; // 8 is RETURN DATA for PRINT operation	
				m->data[2] = i;
				/*printf("Verifying data before sending\n");
				for(j=0 ; j<7 ; j++){
					printf("%c",m->data[j+3]);
				}
				printf("\n");*/
				send(recPort, m);	
			}
			V(mutex);
		}
		else{

		}
		sleep(1);
    }
}

void client1()
{
	mesg_t* m = malloc(sizeof(mesg_t));
	//int port = 2;
	int i = 0;
	int j=0;
	char str1[] = "anirudh";//{97, 110, 105, 114, 117, 100, 104};
	char str2[] = "acharya";//{97, 99, 104, 97, 114, 121, 97};
	int ran;
	
	while (1){
		ran = rand()%10;
		if(ran<5)
		{
			m->data[0] = 4;
			m->data[1] = 1;
			int ran1 = rand()%2;
			if(ran1==0){
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str1[i];
				}
				printf("\n\n******* Client1 sent ADD request to server for string: anirudh \n");	
			}
			else{
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str2[i];
				}
				printf("\n\n******* Client1 sent ADD request to server for string: acharya \n");	
			}
					
			send(5, m);
			mesg_t* add_ack = receive(4);
			
			printf("\n\n*******Client1 got ack for ADDING string: %d\n", add_ack->data[1]);	
			sleep(1);
		}
		
		else if(ran<8)
		{
			m->data[0] = 3;
			m->data[1] = 2;

			printf("\n\n*******Client1 sent DELETE request to server for string \n");
			send(5, m);
			mesg_t* del_ack = receive(3);
			printf("\n\n*******Client1 got ack for DELETING string: %d\n",del_ack->data[1]);	

			sleep(1);
		}
		
		else if(ran<10)
		{
			m->data[0] = 2;
			m->data[1] = 3;
			m->data[2] = rand()%10;
			int ran1 = rand()%2;
			if(ran1==0){
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str1[i];
				}
				printf("\n\n**** Client1 sent UPDATE request to server for string anirudh at index %d \n", m->data[2]);	
			}
			else{
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str2[i];
				}
				printf("\n\n******* Client1 sent ADD request to server for string acharya at index %d \n", m->data[2]);	
			}
					
			send(5, m);
			mesg_t* upd_ack = receive(2);
			
			printf("\n\n*******Client1 got ack for UPDATING string: %d \n", upd_ack->data[1]);	
			sleep(1);
		}
	}
}

void client2()
{
	mesg_t* m = malloc(sizeof(mesg_t));
	
	int i = 0;
	int j = 0;
	char str1[] = "samarth";//{115, 97, 109, 97, 114, 121, 97};
	char str2[] = "daveabc";//{100, 97, 118, 101, 0, 0, 0};
	int ran;
	
	while (1){
		ran = rand()%10;
		if(ran<5)
		{
			m->data[0] = 4;
			m->data[1] = 1;
			int ran1 = rand()%2;
			if(ran1==0){
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str1[i];
				}
				printf("\n\n******* Client1 sent ADD request to server for string: anirudh \n");	
			}
			else{
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str2[i];
				}
				printf("\n\n******* Client1 sent ADD request to server for string: acharya \n");	
			}
					
			send(5, m);
			mesg_t* add_ack = receive(4);
			
			printf("\n\n*******Client1 got ack for ADDING string: %d\n", add_ack->data[1]);	
			sleep(1);
		}
		
		else if(ran<8)
		{
			m->data[0] = 3;
			m->data[1] = 2;

			printf("\n\n*******Client1 sent DELETE request to server for string \n");
			send(5, m);
			mesg_t* del_ack = receive(3);
			printf("\n\n*******Client1 got ack for DELETING string: %d\n",del_ack->data[1]);	

			sleep(1);
		}
		
		else if(ran<10)
		{
			m->data[0] = 2;
			m->data[1] = 3;
			m->data[2] = rand()%10;
			int ran1 = rand()%2;
			if(ran1==0){
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str1[i];
				}
				printf("\n\n**** Client1 sent UPDATE request to server for string anirudh at index %d \n", m->data[2]);	
			}
			else{
				for(i=0 ; i<7 ; i++){
					m->data[i+3] = str2[i];
				}
				printf("\n\n******* Client1 sent ADD request to server for string acharya at index %d \n", m->data[2]);	
			}
					
			send(5, m);
			mesg_t* upd_ack = receive(2);
			
			printf("\n\n*******Client1 got ack for UPDATING string: %d \n", upd_ack->data[1]);	
			sleep(1);
		}
	}
}

void client3()
{
	mesg_t* m = malloc(sizeof(mesg_t));
	mesg_t* print_data = malloc(sizeof(mesg_t));;
	int i = 0;
	int j = 0; 
    	while (1){
		if((rand()%10)>2)
		{
			m->data[0] = 1;
			m->data[1] = 4;
			i=0;
			
			printf("\n\n*******Client3 sent PRINT request to server ****\n");
			send(5, m);
			
			char printTable[10][7];			
			while(i<10)
			{
				print_data = receive(1);
				int ind = print_data->data[2];
				/*printf("Print Data Received \n");
				for(j=0 ; j<7 ; j++){
					printf("%c",print_data->data[j+3]);
				}
				printf("\n");*/
				for(j=0 ; j<7 ; j++){
					printTable[ind][j] = print_data->data[3+j];
					//printf("\nCopied %c to %c", print_data->data[3+j], printTable[ind][j]);
					//j++;
				}
				/*printf("Print data Copied \n");
				for(j=0 ; j<7 ; j++){
					printf("%c",printTable[ind][j]);
				}
				printf("\n");*/
				i++;
			}
			printf("\n\n*******Client3 got Data from server for PRINTING.\n");
			printf("\nPRINT Table \n");
			for(i=0 ; i<10 ; i++){
				for(j=0 ; j<7 ; j++){
					printf("%c",printTable[i][j]);
				}
				printf("\n");
			}
			yield();
		}
		
		else
		{
		  
		  printf("\n\n<-------*****-------Client3 skipping printing for a few iterations and will now yield.--------*****------->\n");
		  
		  yield();
		}
		//sleep(1);
    }
}

int main()
{
        printf("\n\n ******Program Description*******\n");
        sleep(1);
	printf("\n\n Client 1 and 2, either adds, updates or deletes from the table. It adds strings - anirudh, samarth, daveabc and acharya \n And updates a combination of those \n");

        printf("\n\n Client 3 prints the contents of the table \n");

        printf("\n\n Server handles these requests at the appropriate ports and sends ACK messages back to the clients \n");
        sleep(3);
	mutex = CreateSem(1);

	int i=0;
	for(i=0;i<100;i++)
	{
		initPort(&portSet[i]);
	}

	start_thread(client1);
	start_thread(client2);
	start_thread(client3);

	start_thread(server);

	run();
}
