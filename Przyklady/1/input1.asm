global _start
section .text:
_start:
mov eax,0x4
mov ebx,1
mov ecx,message1
mov edx, message_length1
int 0x80
mov eax,2
cmp eax,number
jl less
jg wieksze

less:
mov eax,0x4
mov ebx,1
mov ecx,message2
mov edx,message_length2
int 0x80
mov eax,message_length2
cmp eax,11
jl wakanda
jmp exit

wieksze:
mov eax,0x4
mov ebx,1
mov ecx,message3
mov edx, message_length3
mov eax,number
inc eax
int 0x80
jmp exit

exit:
mov eax,0x1
mov ebx,0
int 0x80

wakanda:
mov eax,0x4
mov ebx,1
mov ecx,message4
mov edx, message_length4
int 0x80
jmp exit



section .data:
message1 db "czesc"
message_length1 equ $-message1
message2 db "mniejsze"
message_length2 equ $-message2
message3 db "wieksze"
message_length3 equ $-message3
message4 db "wakanda"
message_length4 equ $-message4
number dw 2