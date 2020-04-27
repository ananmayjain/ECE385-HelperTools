/* SpriteParser.c - Parses the t files from matlab into an MIF file format
 */

#include <stdio.h>
#include <stdlib.h>

#define INPUT_FILE "viridian_back.png"			// Input filename
#define OUTPUT_FILE "vback.ram"		// Name of file to output to
#define NUM_COLORS 	4								// Total number of different colors
#define WIDTH		8
#define DEPTH		3072

// Use this to define value of each color in the palette
const long Palette_Colors[] = {8388736, 15987705, 8483442, 14145495, 14143953, 9013648, 6974081,
	9001562, 10451578, 12820376, 13722202, 14580338, 15503482, 15507329, 14600877, 16372120,
	8483409, 9470281, 10455377, 11902810, 13284730, 13745274, 16370305, 12367185, 14142096,
	14140282, 14600856, 15512913, 14602577, 15064749, 15062874, 15525272, 15987665, 15984016,
	11922554, 8047202, 9492338, 9033586, 12838317, 12843416, 6993242, 6996888, 8507821, 10018499,
	11396554, 14607845, 11917285, 10464700, 13291991, 11912145, 14607852, 7515614, 13754092, 8504307,
	10934265, 8034513, 6965585, 11873847, 13254737};
int addr = 0;

int main()
{
	char line[21];
	FILE *in = fopen(INPUT_FILE, "r");
	FILE *out = fopen(OUTPUT_FILE, "w");
	size_t num_chars = 20;
	long value = 0;
	int i;
	int *p;

	if(!in)
	{
		printf("Unable to open input file!");
		return -1;
	}

	// Get a line, convert it to an integer, and compare it to the palette values.
	while(fgets(line, num_chars, in) != NULL)
	{
		value = (char)strtol(line, NULL, 10);
		p = (int *)&value;
		fwrite(p, 2, 1, out);
	}

	fclose(out);
	fclose(in);
	return 0;
}
