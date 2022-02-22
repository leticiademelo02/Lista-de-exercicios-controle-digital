#include "stm32f103c8t6.h"
#include "mbed.h"
#include "TextLCD.h"

//Pré-diretiva de compilação
#define MATRIZ_FLOAT
#define Teste_dados

//#define HABILITA_UART
//#define HABILITA_LCD

//Definições
#ifdef HABILITA_LCD
 TextLCD lcd(PA_4,PA_5,PA_6,PB_12,PB_13,PB_14,PB_15);
 #endif
 #ifdef HABILITA_UART
 Serial pc(PB_6,PB_7);
#endif
 DigitalOut led_red(PC_14);
 DigitalOut led_yellow(PC_15);
 DigitalOut  led_board(LED1); //O led da placa liga no 0.
 DigitalIn  key1(PA_7);
 DigitalIn  key2(PB_0);
 DigitalIn  key3(PB_1);
 DigitalIn  key4(PB_10);


#ifdef MATRIZ_FLOAT
    float A[5][5] = {{17,24,1,8,15},{23,5,7,14,16},{4,6,13,20,22},{10,12,19,21,3},{11,18,25,2,9}};
    float B[5][5] = {{1,3,-3,-1,1},{3,-2,-1,1,1},{-2,-1,0,2,3},{0,0,2,2,-2},{0,2,3,-2,-1}};
    float multMatrix(int repet, int norm);
#else
    int32_t A[5][5] = {{17,24,1,8,15},{23,5,7,14,16},{4,6,13,20,22},{10,12,19,21,3},{11,18,25,2,9}};
    int32_t B[5][5] = {{1,3,-3,-1,1},{3,-2,-1,1,1},{-2,-1,0,2,3},{0,0,2,2,-2},{0,2,3,-2,-1}};
    int32_t multMatrix(int repet, int norm);
#endif

 #ifdef HABILITA_UART
int baudrate = 9600;
#endif

int main()
{
    confSysClock();     //Configure system clock (72MHz HSE clock, 48MHz USB clock)
     #ifdef HABILITA_UART
     pc.baud(baudrate);
    #endif
    //Desliga os Leds
    led_board=1;
    led_red=0;
    led_yellow=0;
    int32_t atraso = 0;
    while(1)
    {
    #ifdef Teste_dados
    /***************************************************
    *
    *    Código para Efeito da Escolha dos dados
    *
    ***************************************************/
        led_red = 1;
        led_yellow = 0;
        atraso = multMatrix(40, 117);
        led_red=0;
        led_yellow=1;
        #ifdef MATRIZ_FLOAT
        wait_us(atraso*20);
        #else
        wait_us(atraso);
        #endif
    #else
    /***************************************************
    *
    *    Código para Efeito da USART
    *   implemente o algoritmo da usart.
    *  Não esqueça de Habilitar a USART
    ***************************************************/
    #endif
    #ifdef HABILITA_LCD
        lcd.gotoxy(1,1);
        lcd.printf("Sistema Funcionando!");
    #endif


   }
}

/*************************************************
*
*     Espaço para as funções
*
**************************************************/
#ifdef MATRIZ_FLOAT
float multMatrix(int repet, int norm)
{

float sum = 0;
if(repet>50)
{
    repet=50;
}
for(int n=0;n<repet;n++)
{
    for (int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            for(int k=0;k<5;k++)
            {
                sum += A[i][k]*B[k][j];
            }
        }
    }
}
return floor(sum/norm);

}
#else
int32_t multMatrix(int repet, int norm)
{

int32_t sum = 0;
if(repet>50)
{
    repet=50;
}
for(int n=0;n<repet;n++)
{
    for (int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            for(int k=0;k<5;k++)
            {
                sum += A[i][k]*B[k][j];
            }
        }
    }
}
return (int32_t)(sum/norm);

}

#endif