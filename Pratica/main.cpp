#include "stm32f103c8t6.h"
#include "mbed.h"
#include "TextLCD.h"

/******************************************************************
*
*	Definição dos pinos usados na placa da UFSCar
*
*******************************************************************/
 TextLCD lcd(PA_4,PA_5,PA_6,PB_12,PB_13,PB_14,PB_15);
 DigitalOut led_red(PC_14);
 DigitalOut led_yellow(PC_15);
 DigitalOut  myled(LED1);
  
 DigitalIn  key1(PA_7);
 DigitalIn  key2(PB_0);
 DigitalIn  key3(PB_1);
 DigitalIn  key4(PB_10);

Serial pc(PB_6,PB_7);

/******************************************************************
*
*	Espaço de definição para variáveis globais
*
*******************************************************************/

/******************************************************************
*
*	Espaço para inserir a função de multiplicação de matrizes
*
*******************************************************************/
   
int main() {
    confSysClock();     //Configure system clock (72MHz HSE clock, 48MHz USB clock)
    
    // The on-board LED is connected, via a resistor, to +3.3V (not to GND). 
    // So to turn the LED on or off we have to set it to 0 or 1 respectively

/******************************************************************
*
*	Espaço para inserir as funções dentro da main.
*
*******************************************************************/




}
 