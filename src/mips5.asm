.data 0x10010000
msg: .asciiz "Entre com seu voto: "
msg_votos: .asciiz "Total: "
msg_votos_1: .asciiz "\n1 - Joao: "
msg_votos_2: .asciiz "\n2 - Jose: "
msg_votos_3: .asciiz "\n3 - Maria: "
.text
entrada:    # Entrada do Voto
            li $v0, 4
            la $a0, msg
            syscall
            li $v0, 5
            syscall
            # Salvar Voto
            move $t0, $v0
            # Encerrar
            beq $t0, 0, fim
            # Incrementar Total
            addi $s0, $s0, 1
            # Votos Validos
            beq $t0, 1, voto_1
            beq $t0, 2, voto_2
            beq $t0, 3, voto_3
            j entrada
voto_1:     # 1 - Voto em Joao
            addi $s1, $s1, 1
            j entrada
voto_2:     # 2 - Voto em Jose
            addi $s2, $s2, 1
            j entrada
voto_3:     # 3 - Voto em Maria
            addi $s3, $s3, 1
            j entrada
fim:        # Imprimir Total de Votos
            li $v0, 4
            la $a0, msg_votos
            syscall
            li $v0, 1
            la $a0, ($s0)
            syscall
            # Imprimir Votos de Joao
            li $v0, 4
            la $a0, msg_votos_1
            syscall
            li $v0, 1
            la $a0, ($s1)
            syscall
            # Imprimir Votos de Jose
            li $v0, 4
            la $a0, msg_votos_2
            syscall
            li $v0, 1
            la $a0, ($s2)
            syscall
            # Imprimir Votos de Maria
            li $v0, 4
            la $a0, msg_votos_3
            syscall
            li $v0, 1
            la $a0, ($s3)
            syscall