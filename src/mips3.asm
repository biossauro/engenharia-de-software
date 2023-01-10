.data 0x10010000
input_1: .asciiz "Valor 'A': "
input_2: .asciiz "Valor 'B': "
input_3: .asciiz "Valor 'C': "
breakln: .asciiz "\n"
.text
            # Entrada de 'A'
            li $v0, 4
            la $a0, input_1
            syscall
            li $v0, 5
            syscall
            # Salvar 'A'
            move $s0, $v0
            # Entrada de 'B'
            li $v0, 4
            la $a0, input_2
            syscall
            li $v0, 5
            syscall
            # Salvar 'B'
            move $s1, $v0
            # Entrada de 'C'
            li $v0, 4
            la $a0, input_3
            syscall
            li $v0, 5
            syscall
            # Salvar 'C'
            move $s2, $v0
comparar:   # Compara 'A' e 'B'
            bgt $s0, $s1, troca_01
            # Compara 'B' e 'C'
            bgt $s1, $s2, troca_12
            # Pula p/ o Fim
            j fim
troca_01:   # Troca 'A' e 'B'
            move $t0, $s0
            move $s0, $s1
            move $s1, $t0
            j comparar
troca_12:   # Troca 'B' e 'C'
            move $t0, $s2
            move $s2, $s1
            move $s1, $t0
            j comparar
fim:        # Imprime Valores
            li $v0, 4
            la $a0, breakln
            syscall
            li $v0, 1
            move $a0, $s0
            syscall
            li $v0, 4
            la $a0, breakln
            syscall
            li $v0, 1
            move $a0, $s1
            syscall
            li $v0, 4
            la $a0, breakln
            syscall
            li $v0, 1
            move $a0, $s2
            syscall