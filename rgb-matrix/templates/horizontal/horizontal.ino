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
    delay(100);
    if (fill) {
        i = 0;
        for (y = 0; y < matrix.width(); y++) {
            r = hex[i] / 0x10000;
            g = (hex[i]/0x100) % 0x100;
            b = hex[i]%0x100;
            c = matrix.Color888(r, g, b);
            matrix.drawPixel(x, y, c);
            if (y%2 == 1) {
                i = (i+1) % hexLength;
            }
        }
        x++;
        if (x == matrix.width()) {
          delay(1000);
          fill = false;
          x = 0;
        }
    } else {
        for (y = 0; y < matrix.width(); y++) {
            c = matrix.Color888(0,0,0);
            matrix.drawPixel(x, y, c);
        }
        x++;
        if (x == matrix.width()) {
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

    x = 0;
    fill = true;
}