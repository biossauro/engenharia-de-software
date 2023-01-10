#include <stdio.h>
#include <stdlib.h>

#define FOSC 16000000U // Clock Speed
#define BAUD 9600
#define MYUBRR FOSC / 16 / BAUD - 1

#define PwmOut (1 << PD5)
#define FREIO (1 << PD2)
#define FREIANDO (PIND & FREIO) == 0

char msg_tx[20];
char msg_rx[32];
int pos_msg_rx = 0;
int tamanho_msg_rx = 1;

unsigned int velocidade;
unsigned long aux;
unsigned char pwm;
u16 adc_result0;

// Prototipo das Funcoes ADC
void ADC_Init();
int ADC_Read(u8 ch);

// Prototipos das Outras Funcoes
void UART_Init(unsigned int ubrr);
void UART_Transmit(char *dados);

ISR(USART_RX_vect)
{
    // Escreve o valor recebido pela UART na posicao pos_msg_rx do buffer msg_rx
    msg_rx[pos_msg_rx++] = UDR0;

    if (pos_msg_rx == tamanho_msg_rx)
    {
        pos_msg_rx = 0;
    }
}

void setup()
{
    // Define entradas e saidas
    DDRD |= PwmOut;
    PORTD &= ~PwmOut;

    // Configura o Timer PWM
    TCCR0A |= (1 << WGM01) | (1 << WGM00) | (1 << COM0B1);
    TCCR0B = (1 << CS00);
    OCR0B = 0;

    // Habilita resistor de pull-up no PD2
    PORTD |= FREIO;

    // Habilita UART
    UART_Init(MYUBRR);

    // Habilita interrupcao externa global
    sei();

    // Inicializa ADC
    ADC_Init();
}

void loop()
{
    UART_Transmit("L p/ ligar\n");
    while (1)
    {
        if (msg_rx[0] == 'L' || msg_rx[0] == 'l')
        {
            // Liga o sistema
            velocidade = 0;
            OCR0B = 0;

            UART_Transmit("Sistema Ligado\n");
            break;
        }
    }

    UART_Transmit("D p/ desligar\nV p/ valor\n");
    while (1)
    {
        if (msg_rx[0] == 'D' || msg_rx[0] == 'd')
        {
            // Desliga o sistema
            velocidade = 0;
            OCR0B = 0;
            UART_Transmit("Sistema Desligado\n");
            break;
        }
        else if (msg_rx[0] == 'V' || msg_rx[0] == 'v')
        {
            // Mostra 'velocidade'
            UART_Transmit("Velocidade: ");
            itoa(velocidade, msg_tx, 10);
            UART_Transmit(msg_tx);
            UART_Transmit("\n");

            msg_rx[0] = 'n';
        }
        else if (FREIANDO)
        {
            velocidade = 0;
            OCR0B = 0;
        }
        else
        {
            // Converte o valor lido
            adc_result0 = ADC_Read(ADC0D);
            _delay_ms(50);
            pwm = adc_result0 * 0.2493;
            OCR0B = pwm;

            // Passa o valor p/ 'velocidade'
            aux = (long)adc_result0 * 280;
            aux /= 1023;
            velocidade = (unsigned int)aux;
        }
    }
}

void UART_Init(unsigned int ubrr)
{
    // Configura a baud rate
    UBRR0H = (unsigned char)(ubrr >> 8);
    UBRR0L = (unsigned char)ubrr;
    // Habilita a recepcao, tranmissao e interrupcao na recepcao
    UCSR0B = (1 << RXEN0) | (1 << TXEN0) | (1 << RXCIE0);
    // Configura o formato da mensagem: 8 bits de dados e 1 bits de parada
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

void UART_Transmit(char *dados)
{
    // Envia todos os caracteres do buffer dados ate chegar um final de linha
    while (*dados != 0)
    {
        while (!(UCSR0A & (1 << UDRE0)))
            ; // Aguarda a transmissao acabar
        // Escreve o caractere no registro de tranmissao
        UDR0 = *dados;
        // Passa para o próximo caractere do buffer dados
        dados++;
    }
}

void ADC_Init()
{
    ADMUX = (1 << REFS0);
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

int ADC_Read(u8 ch)
{
    char i;
    int ADC_temp = 0;
    int ADC_Read = 0;
    ch &= 0x07;
    ADMUX = (ADMUX & 0xF8) | ch;
    ADCSRA |= (1 << ADSC);
    while (!(ADCSRA & (1 << ADIF)))
        ;
    for (i = 0; i < 8; i++)
    {
        ADCSRA |= (1 << ADSC);
        while (!(ADCSRA & (1 << ADIF)))
            ;
        ADC_temp = ADCL;
        ADC_temp += (ADCH << 8);
        ADC_Read += ADC_temp;
    }
    ADC_Read = ADC_Read >> 3;
    return ADC_Read;
}
