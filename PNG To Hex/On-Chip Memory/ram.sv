/*
 * ECE385-HelperTools/PNG-To-Txt
 * Author: Rishi Thakkar
 *
 */

module  frameRAM
(
		input [4:0] data_In,
		input [18:0] write_address, read_address,
		input LOAD, CLK,

		output logic [4:0] data_Out
);

	// mem has width of 3 bits and a total of 400 addresses
	logic [3:0] mem [265:0];

	initial
	begin
		 $readmemh("sprite_bytes/tetris_I.txt", mem);
	end


	always_ff @ (posedge Clk) begin
		if (LOAD)
			mem[write_address] <= data_In;
		data_Out <= mem[read_address];
	end

endmodule
