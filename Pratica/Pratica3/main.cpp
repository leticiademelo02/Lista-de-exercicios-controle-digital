#include "stm32f103c8t6.h"
#include "mbed.h"
#include "TextLCD.h"

#define Ts 0.1f
#define BAUD 9600
 TextLCD lcd(PA_4,PA_5,PA_6,PB_12,PB_13,PB_14,PB_15);
 DigitalOut ledR(PC_14);
 DigitalOut ledY(PC_15);
 DigitalOut  myled(LED1);
 Serial pc(PA_2,PA_3);
 
 DigitalOut step(PA_12);
 InterruptIn key2(PB_0);
 AnalogIn dataIN(A0);

Ticker looper;

bool _btnFunction=false;
bool loopFlag = false;
bool first = false;
uint16_t voltage;

void pressed()
{
    _btnFunction = !_btnFunction;
}

void wait_user()
{
    while(!_btnFunction) {
        wait_ms(10);
    }
    _btnFunction = 0;
}

void blink_led(int period_in_ms, int times)
{
    for(int i=0; i<2*times; i++) {
        myled = !myled;
        wait_ms(period_in_ms/2);
    }
    myled=0;
}

void loop()
{
    loopFlag = true;
} 
 
int main() {
    confSysClock();     //Configure system clock (72MHz HSE clock, 48MHz USB clock)
    pc.baud(BAUD);
    ledY = 0;
    key2.fall(&pressed); 
    // The on-board LED is connected, via a resistor, to +3.3V (not to GND). 
    // So to turn the LED on or off we have to set it to 0 or 1 respectively
    myled=0;
    ledR=0;
    wait_user();
    pc.printf("Sync message!\r\n");
    myled=1;
    lcd.gotoxy(1,1);
    lcd.printf("Sistema Ligado!");
    blink_led(200, 10);
    lcd.gotoxy(1,2);
    lcd.printf("Dados em 2s!");
    wait(2);  
    lcd.gotoxy(1,2);
    lcd.printf("                ");
    looper.attach(&loop,Ts);
    while(1) {
        
        if(loopFlag)
        {
            loopFlag = 0;
            ledR = !ledR;
            //myled = !myled;
            if(!_btnFunction)
            {
                ledY=1;
                step = 1;
                first = false;
                voltage =  dataIN.read_u16()>>4;
                pc.printf("A[%4d]\r\n",voltage);
                ledY=0;
            }
            else
            {
                step=0;
                if(!first)
                {
                    pc.printf(" Aperte para amostrar de novo\r\n");
                    first = true;
                }
                else
                {
                    wait_ms(10);
                    myled = !myled;
                }
             }  
        }     
   }
}