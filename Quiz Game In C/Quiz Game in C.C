#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<string.h>

int n=0,right=0,wrong=0,updat=0;
int a,b[20];

void intro()
{ clrscr();
  cleardevice();
  printf("\n\n\t\t\t**********************************");
  printf("\n\t\t\t*\t\t\t\t *\n\t\t\t*     WELCOME TO THE QUIZ GAME   *\n\t\t\t*\t\t\t\t *");
  printf("\n\t\t\t**********************************");
}

void load()
{
   int i;
   delay(100);
   printf("\n\n\t\t\t  L");
   delay(150);
   printf("O");
   delay(150);
   printf("A");
   delay(150);
   printf("D");
   delay(150);
   printf("I");
   delay(150);
   printf("N");
   delay(150);
   printf("G");
   delay(150);

    rectangle(270,127,445,140);

    for(i=0;i<176;i++)
    {
      rectangle(270,127,270+i,140);
      setcolor(GREEN);
      delay(20);
     }

}

void selection_menu()
{  printf("\n\n\n\n\t\t\t\t");
   setcolor(WHITE);
   rectangle(180,180,475,310);

   printf("  SELECTION MENU");
   printf("\n\n\t\t\t");
   printf(" 1. Create Quiz");
   printf("\n\t\t\t");
   printf(" 2. Play Quiz");
   printf("\n\t\t\t ");
   printf("3. Update Quiz(Delete Questions)");
   printf("\n\t\t\t ");
   printf("4. View Result");
   printf("\n\t\t\t ");
   printf("5. Exit");

   line(180,180,180,310);

}

struct question
{
  char question[100];
  char answer[100];
  char input[100];
  char opt_1[100];
  char opt_2[100];
  char opt_3[100];
}q[20];


void create_quiz()
{
  int i;
  clrscr();
  cleardevice();

  printf("\n\n\t\t\t\tCREATE THE QUIZ");
  B:
  printf("\n\nEnter The Number Of Questions...: ");
  scanf("%d",&n);

   if(n<=20)
    {
  for(i=0;i<n;i++)
  {
    printf("\nEnter The Question %d:",i+1);
    fflush(stdin);
    gets(q[i].question);
    printf("\nEnter The Answer:");
    fflush(stdin);
    gets(q[i].answer);
    printf("\nEnter Option 1: ");
    fflush(stdin);
    gets(q[i].opt_1);
    printf("\nEnter Option 2: ");
    fflush(stdin);
    gets(q[i].opt_2);
    printf("\nEnter Option 3: ");
    fflush(stdin);
    gets(q[i].opt_3);
   }

   printf("\n\nQUIZ CREATED SUCCESSFULLY");

   printf("\n\nPRESS ANY KEY TO GO TO THE SELECTION MENU");
   getch();

   intro();
   load();
   selection_menu();
  }
  else
  {
   printf("\nMaximum Value Of Questions Exceeded...\nMaximum Limit Is 20 ");
   goto B;
  }

}

void quiz()
{
   int i,count=0,l;
   right=0,wrong=0;

   clrscr();
   cleardevice();

   printf("\n\nPRESS ANY KEY TO START THE GAME");

   getch();

   for(i=0;i<n;i++)
   { count=0;
    for(l=0;l<a;l++)
    {
     if(i==(b[l]-1))
       count++;
    }
    if(count==0)
    {
     printf("\n\nQuestion : ");
     fflush(stdin);
     puts(q[i].question);

     printf("\n");

     printf("1. ");
     fflush(stdin);
     puts(q[i].opt_1);
     printf("\n2. ");
     fflush(stdin);
     puts(q[i].opt_2);
     printf("\n3. ");
     fflush(stdin);
     puts(q[i].opt_3);
     printf("\n\nEnter The Answer: ");
     fflush(stdin);
     gets(q[i].input);

     if(strcmp(q[i].answer,q[i].input)==0)
	 right++;
     else
	 wrong++;
    }

    else
    continue;
   }
     printf("\n\nQUIZ HAS BEEN COMPLETED..\n\nPRESS ANY KEY TO VIEW RESULT");
     getch();
   intro();
   load();
   selection_menu();

}

void result()
{

 clrscr();
 cleardevice();
 printf("\nRESULT\n******");

 printf("\n\nYour Result Is: ");
 printf("   You Have Given %d Right Answers And %d Wrong Answers.",right,wrong);
   printf("\n\n\n\nEnter Any Key To Go To Selection Menu.");
   getch();

   intro();
  load();
  selection_menu();

}

void update()
{
  int k,i,len;
  clrscr();
  cleardevice();
   printf("\n UPDATION CENTRE\n****************\n");
   for(i=0;i<n;i++)
   {
      if(i<9)
       {
	 printf("%d.  ",i+1);
	 puts(q[i].question);
       }
       if(i>=9)
       {
	printf("%d. ",i+1);
	puts(q[i].question);
       }

   }
  printf("\n\n\n\nEnter The Number Of Questions You Want To Delete: ");
  scanf("%d",&a);

  printf("\n\nEnter The Question's Number You Want To Delete: ");
  for(k=0;k<a;k++)
   scanf("%d",&b[k]);

  printf("\n\nUpdation Done Successfully..\n\nPress Any Key To Go To The Selection Menu");
  getch();

  intro();
  load();
  selection_menu();

}


void main()
{
  int choice;
  int gd=DETECT,gm;
   initgraph(&gd,&gm,"C://turboc3//bgi");


     intro();
     load();
     selection_menu();

    A:

    printf("\n\n\n\t\t\tEnter Your Choice :   ");
    scanf("%d",&choice);

   switch(choice)
    {
      case 1 : create_quiz();
		 goto A;


      case 2 : quiz();
		 goto A;


      case 3 : update();
		 goto A;


      case 4 : result();
		 goto A;


      case 5 : break;


      default: printf("\nWrong Choice.....");
		 goto A;
      }

      printf("\n\n\n\tThanks For Using The Quiz Game.");

 getch();
}