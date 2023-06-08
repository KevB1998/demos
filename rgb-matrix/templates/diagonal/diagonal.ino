#include <RGBmatrixPanel.h>

#define CLK 8
#define OE 9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);

int x, y, i;
uint8_t r, g, b;
uint16_t c;

int hex[] = {0xE50000, 0xFF6000, 0xFFEE00, 0x028121, 0x004CFF, 0x770088};

int hexLength;
bool fill;

void setup() {
    matrix.begin();
    reset();
}

void loop() {
    delay(8);
    if (fill && x < matrix.width()-1 - y) {
        i = ((matrix.width()-y-x-2)/2) % hexLength;
        r = hex[i] / 0x10000;
        g = (hex[i]/0x100) % 0x100;
        b = hex[i]%0x100;
        c = matrix.Color888(r, g, b);
        matrix.drawPixel(x, y, c);
        x++;
    } else if (fill) {
        i = ((x+y-matrix.width())/2) % hexLength;
        r = hex[i] / 0x10000;
        g = (hex[i]/0x100) % 0x100;
        b = hex[i]%0x100;
        c = matrix.Color888(r, g, b);
        matrix.drawPixel(x, y, c);
        y++;

        if (y == matrix.width() && x == matrix.width()-1) {
            fill = false;
            x = 0;
            delay(1000);
        } else if(y == matrix.width()) {
            y -= x+2;
            x = 0;
        }
    } else {
        delay(42);
        int x1 = 0;
        int y1 = matrix.width() - 1 - x;

        int x2 = x;
        int y2 = matrix.width() - 1;
        
        while (x2 < matrix.width()) {
            c = matrix.Color888(0, 0, 0);
            matrix.drawPixel(x1, y1, c);
            matrix.drawPixel(x2, y2, c);
            x1++;
            y1--;
            x2++;
            y2--;
        }
        x++;
        if(x == matrix.width()) {
          delay(500);
          reset();
        }
    }
}

void reset() {
    r = hex[0] / 0x10000;
    g = (hex[0]/0x100) % 0x100;
    b = hex[0]%0x100;
    c = matrix.Color888(r, g, b);
    hexLength = sizeof(hex)/sizeof(hex[0]);

    y = matrix.width()-1;
    x = 0;
    fill = true;
    matrix.drawPixel(x, y, c);
    y--;
}