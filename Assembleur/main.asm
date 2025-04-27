; ===============================
; Fichier : hello_win.asm
; Objectif : Afficher "Salut !" dans la console Windows
; Assembleur : NASM
; ===============================

section .data
    message db "Salut !", 0  ; Texte + terminator
    msg_length equ $-message ; Calcul automatique de la taille

section .text
    global _start
    extern  GetStdHandle, WriteConsoleA, ExitProcess

_start:
    ; Get handle vers la console
    mov     ecx, -11             ; STD_OUTPUT_HANDLE (-11)
    call    GetStdHandle
    mov     rbx, rax             ; Sauvegarder handle de sortie standard

    ; Préparer paramètres pour WriteConsoleA
    mov     rcx, rbx             ; HANDLE
    lea     rdx, [rel message]   ; Adresse du message
    mov     r8d, msg_length      ; Longueur
    xor     r9d, r9d             ; NULL pour le nombre écrit

    call    WriteConsoleA

    ; Quitter proprement
    xor     ecx, ecx             ; Code de sortie = 0
    call    ExitProcess