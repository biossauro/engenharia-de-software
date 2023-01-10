.data 0x10010000
input_1: .asciiz "Inteiro 'A': "
input_2: .asciiz "Inteiro 'B': "
input_3: .asciiz "\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\nCódigo de Operação: "
output: .asciiz "\nResultado = "
.text
        # Entrada de 'A'
        li $v0, 4
        la $a0, input_1
        syscall
        li $v0, 5
        syscall
        # Salvar 'A'
        move $t0, $v0
        # Entrada de 'B'
        li $v0, 4
        la $a0, input_2
        syscall
        li $v0, 5
        syscall
        # Salvar 'B'
        move $t1, $v0
op:     # Entrada de 'OP'
        li $v0, 4
        la $a0, input_3
        syscall
        li $v0, 5
        syscall
        beq $v0, 1, op_1
        beq $v0, 2, op_2
        beq $v0, 3, op_3
        beq $v0, 4, op_4
        j op
op_1:   # Soma
        add $s0, $t0, $t1
        j fim
op_2:   # Subtração
        sub $s0, $t0, $t1
        j fim
op_3:   # Divisão
        div $s0, $t0, $t1
        j fim
op_4:   # Multiplicação
        mul $s0, $t0, $t1
        j fim
fim:    # Saida do resultado
        li $v0, 4
        la $a0, output
        syscall
        li $v0, 1
        la $a0, ($s0)
        syscall