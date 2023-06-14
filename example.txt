global _start
section .text:
_start:
mov eax,0x4
mov ebx,1
mov ecx,wiadomosc1
mov edx, len_1
int 0x80
mov eax,number
cmp eax,5
jl less

less:
mov eax,0x4
mov ebx,1
mov ecx,wiadomosc2
mov edx,len_2
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
wiadomosc1 db "przed skonczona petla"
len_1 equ $-wiadomosc1
wiadomosc2 db "zaraz koniec"
len_2 equ $-wiadomosc1

