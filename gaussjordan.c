#include<stdio.h>
#define INPUT_X 1000
#define INPUT_Y 1000
int main()
{
    int i,j,k,n;
    float A[INPUT_X][INPUT_Y],c,saida[10];
    for(int y=0;y<INPUT_Y;y++)
	for(int x=0;x<INPUT_X;x++)
	    A[x][y] = rand();
    for(j=1; j<=n; j++)
    {
        for(i=1; i<=n; i++)
        {
            if(i!=j)
            {
                c=A[i][j]/A[j][j];
                for(k=1; k<=n+1; k++)
                {
                    A[i][k]=A[i][k]-c*A[j][k];
                }
            }
        }
    }
    for(i=1; i<=n; i++)
    {
        saida[i]=A[i][n+1]/A[i][i];
    }
    return(0);
}
