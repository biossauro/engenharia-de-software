.data 0x10010000
input_1: .asciiz "Entre com o inteiro 'A': "
input_2: .asciiz "Entre com o inteiro 'B': "
output_1: .asciiz "A = "
output_2: .asciiz "\nB = "
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
# Trocar 'A' por 'B' e vice-versa
move $t0, $s0
move $t1, $s1
move $s0, $t1
move $s1, $t0
# Mostrar 'A' (Trocado)
li $v0, 4
la $a0, output_1
syscall
li $v0, 1
move $a0, $s0
syscall
# Mostrar 'B' (Trocado)
li $v0, 4
la $a0, output_2
syscall
li $v0, 1
move $a0, $s1
syscall