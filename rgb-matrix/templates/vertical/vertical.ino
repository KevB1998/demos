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
bool fill, down;

void setup() {
    matrix.begin();
    reset();
}

void loop() {
    delay(20);
    if (fill) {
        i = (x/2) % hexLength;
        r = hex[i] / 0x10000;
        g = (hex[i]/0x100) % 0x100;
        b = hex[i]%0x100;
        c = matrix.Color888(r, g, b);
        matrix.drawPixel(x, y, c);
        matrix.drawPixel(x+1, y, c);

        if (down) {
            y++;
        } else {
            y--;
        }

        if ((y == -1 || y == matrix.width()) && x == matrix.width()) {
            delay(1000);
            fill = false;
            y = 0;
            x = 0;
        } else if (y == -1) {
            down = true;
            y++;
            x += 2;
        } else if (y == matrix.width()) {
            down = false;
            y--;
            x += 2;
        }
    } else {
        c = matrix.Color888(0, 0, 0);
        matrix.drawPixel(x, y, c);
        matrix.drawPixel(x+1, y, c);

        if (down) {
            y++;
        } else {
            y--;
        }

        if ((y == -1 || y == matrix.width()) && x == matrix.width()) {
            delay(500);
            reset();
        } else if (y == -1) {
            down = true;
            y++;
            x += 2;
        } else if (y == matrix.width()) {
            down = false;
            y--;
            x += 2;
        }
    }
}

void reset() {
    r = hex[0] / 0x10000;
    g = (hex[0]/0x100) % 0x100;
    b = hex[0]%0x100;
    c = matrix.Color888(r, g, b);
    hexLength = sizeof(hex)/sizeof(hex[0]);

    fill = true;
    down = true;
    y = 0;
    x = 0;
}