// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// Pseudocode:
// product = R2
// n = R1
// i = 1
// for (i, i<=n, i++)
//     product = product + R0
//----------------------------------

    @i      // initializing a for loop, i <- 1
    M=1
    @R1
    D=M
    @n
    M=D     // n <- R1
    @R2
    M=0     // R2 <- 0

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @END
    D;JGT   // if i>n goto END

    @R0
    D=M
    @R2
    M=M+D   // R2 <- R2 + R0
    @i
    M=M+1   // i <- i++
    @LOOP
    0;JMP
(END)
    @END
    0;JMP
