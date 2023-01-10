# Trabalho de E209

## Enunciado

Uma fabricante de veículos chamada WMB decidiu investir pesado em microcontroladores para integrar parte do sistema de funcionamento de seus veículos. Sabendo que vocês são experts no assunto, a WMB decidiu conta-los para implementar parte do sistema de funcionamento de um dos seus modelos de carro, o super veloz i023.

## Condições de Projeto

1. Para que o veículo seja ligado, o motorista deve enviar "L" através da serial(UART) do microcontrolador, e para que seja desligado deve ser enviada a letra "D".

2. Através de uma entrada analógica, utilizando um potênciometro, por exemplo, o microcontrolador deve ler a quantidade de tensão que está sendo entregue, tensão essa que varia de 0V a 5V e representa o quanto o carro está sendo acelerado.

3. O retorno do conversor ADC deve ser usado para controlar (através de um pino de PWM) a velocidade do i023, por meio da quantidade de tensão aplicada em seu motor (pode ser representado por um LED).

4. Caso o freio (pode ser representado por um chave ou botão) seja pressionado, o motor deve ser parado, independente do quando o carro esteja acelerado, e quando o freio for solto o carro deve retornar a aceleração de acordo com a posição do potenciômetro.

5. A velocidade do i023 varia entre 0 km/h e 280 km/h(0V a 5V), caso seja enviada através da serial(UART) a letra “V”, deve ser mostrada na mesma, a velocidade do carro.
