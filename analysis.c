#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include"brain.h"



// needs to be fixed
void analyzeBrain(brain * b , int inputCount, int outputCount)
{

	assert(inputCount <= 1000);

	int run = 1;

	char userInputs[1000] = {""};
	int  inputs[inputCount];// = malloc(sizeof(int) * inputCount);
	int  outputs[outputCount];//] = malloc(sizeof(int)* outputCount);
	//char userInputField[1000] = {""};


	while(run)
	{

		brain * testInstance = forkBrain(b);
		printf("PLEASE ENTER A STRING SPECIFYING %d INPUTS\n", inputCount);
		fgets(userInputs, inputCount+1, stdin);
		for(int i = 0; i < inputCount; i++)
		{
			if (userInputs[i] == '1') 
			{
				inputs[i] = 1;

			}
			else if (userInputs[i] == '0')
			{
				inputs[i] = 0;

			}
			else
			{
				printf("INPUT STRING: %c INVALID, RESTARTING\n", userInputs[i] );
				free(testInstance);
				exit(1);
			}

		}
		


		int advanceTo = 0;

		while(!advanceTo > 0)
		{
		printf("PLEASE SPECIFY THE NUMBER OF DESIRED TIME-SLICES:\n");
		stdin = freopen(NULL,"r",stdin);
		fgets(userInputs, 20, stdin);
		 advanceTo = atoi(userInputs);
		}

		for(int i = 0; i < advanceTo; i++)
		{
			advanceBrain(testInstance, inputs, inputCount, outputs, outputCount);
		}


		printf("OUTPUTS:");
		for(int i = 0 ; i < outputCount; i ++)
		{
			printf("%d",outputs[i]);
		}
		printf("\n");

	}






}
