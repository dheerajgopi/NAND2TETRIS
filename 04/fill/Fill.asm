// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

@SCREEN
	D=A
	@addr 
	M=D
(INFINITE_LOOP)	
	@KBD
	D=M
@CLEAR_SCREEN
	D;JLE        
(BLACKEN)
	@addr
	D=M
	@KBD    
	D=D-A
	@INFINITE_LOOP
	D;JGE
	@addr
	M=M+1
	@KBD
	D=D+A 
	A=D
	M=-1
	@INFINITE_LOOP
	0;JMP
(CLEAR_SCREEN)
	@addr
	D=M-1
	@SCREEN
	D=D-A
	@INFINITE_LOOP
	D;JLT
	@addr
	M=M-1
	@SCREEN
	D=D+A
	A=D
	M=0
	@INFINITE_LOOP
	0;JMP

