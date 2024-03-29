global    _start

section .text
    _start:    
        mov       rax, 1                  ; system call for write
        mov       rdi, 1                  ; file handle 1 is stdout
        mov       rsi, arrayMsg           ; address of string to output
        mov       rdx, 14                 ; number of bytes
        syscall                           ; invoke operating system to do the write
        
        ; write the array NUMBERS here
        
        
        mov       rax, 60                 ; system call for exit
        xor       rdi, rdi                ; exit code 0
        syscall                           ; invoke operating system to exit

section .data
    NUMBERS	DW  2, 3, 4, 10, 40
    arrayMsg: db  "The array is", 10      ; note the newline at the end