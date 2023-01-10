.data 0x10010000
input_1: .asciiz "Entre com 'B': "
input_2: .asciiz "Entre com 'b': "
input_3: .asciiz "Entre com 'h': "
output: .asciiz "S = "
.text
# Entrada de 'B'
li $v0, 4
la $a0, input_1
syscall
li $v0, 5
syscall
# Salvar 'B'
move $s0, $v0
# Entrada de 'b'
li $v0, 4
la $a0, input_2
syscall
li $v0, 5
syscall
# Salvar 'b'
move $s1, $v0
# Entrada de 'h'
li $v0, 4
la $a0, input_3
syscall
li $v0, 5
syscall
# Salvar 'h'
move $s2, $v0
# Calculo da Area 'S'
add $t0, $s0, $s1
mul $t1, $t0, $s2
div $s3, $t1, 2
# Mostrar 'S'
li $v0, 4
la $a0, output
syscall
li $v0, 1
move $a0, $s3
syscall
