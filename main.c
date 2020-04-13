#include <stdio.h>
#include <math.h>
#include <time.h>
#define ANSI_COLOR_RESET   "\x1b[0m"

const char colors[15][12] = {"\x1b[0;31;46m", "\x1b[1;31;46m", "\x1b[0;32;45m", "\x1b[1;32;45m", "\x1b[0;33;44m", "\x1b[1;33;44m",
                            "\x1b[0;34;43m", "\x1b[1;34;43m", "\x1b[0;35;42m", "\x1b[1;35;42m", "\x1b[0;36;41m", "\x1b[1;36;41m"
};


int xs = 256;
int ys = 256;

int arr[256][256];

int main() 
{
for(;;) 
{	
	for (int x=0; x<xs; x++)
	{
		for (int y=0; y<xs; y++)
			{	
			printf("%s",colors[(int)round((x^y)/24)]);
			putchar(round(65+(x^y)/8));
			printf(ANSI_COLOR_RESET);
			
			}
		putchar('\n'); usleep(20000);
	}
}
	return 0;
}

