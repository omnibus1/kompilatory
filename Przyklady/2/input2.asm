global _start
section .text:
_start:
mov eax,0x4
mov ebx,1
mov ecx,message1
mov edx, message_length1
int 0x80
mov eax,2
cmp eax,5
jl less

less:
mov eax,0x4
mov ebx,1
mov ecx,message2
mov edx,message_length2
int 0x80
mov eax,number
inc eax
cmp eax,10
jg less


exit:
mov eax,0x1
mov ebx,0
int 0x80




section .data:
przeddb "zaczynamy petle"
dlugosc1 equ $-przed_petla
w_petli db "bez konca"
dlugosc2 equ $-w_petli
