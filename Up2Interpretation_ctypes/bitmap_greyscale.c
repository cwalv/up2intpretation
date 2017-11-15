
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * Plucked From http://stackoverflow.com/questions/2654480/writing-bmp-image-in-pure-c-c-without-other-libraries
 */
void read_grayscale_bmp(char *filename, int w, int h, unsigned char **img_out)
{
    unsigned char *img = NULL;

    FILE *f;
    unsigned char ignored[40];
    const size_t bmppad_sz = (4 - (w * 3) % 4) % 4;

    if (img)
        free(img);
    img = (unsigned char *)malloc(3 * w * h);
    memset(img, 0, 3 * w * h);

    f = fopen(filename, "rb");
    fread(ignored, 1, 14, f);
    fread(ignored, 1, 40, f);
    for (int i = 0; i < h; i++)
    {
        fread(img + (w * 3 * (h - i - 1)), 3, w, f);
        fread(ignored, 1, bmppad_sz, f);
    }
    fclose(f);

    for (int i = 0; i < w; i++)
    {
        for (int j = 0; j < h; j++)
        {
            int y = h - j - 1;

            // Calculate "luma" from RGB
            // http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/POYNTON1/ColorFAQ.html#RTFToC18
            float r = img[(i + y * w) * 3 + 2];
            float g = img[(i + y * w) * 3 + 1];
            float b = img[(i + y * w) * 3 + 0];

            float ciey = .212671 * r + .715160 * g + .072169 * b;
            img[(i + y * w) * 3 + 2] = img[(i + y * w) * 3 + 1] = img[(i + y * w) * 3 + 0] = ciey;
        }
    }

    *img_out = img;
}

void write_bmp(char *filename, unsigned char *img, int w, int h)
{

    FILE *f;

    unsigned char bmpfileheader[14] = {'B', 'M', 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0};
    unsigned char bmpinfoheader[40] = {40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 24, 0};
    unsigned char bmppad[3] = {0, 0, 0};
    const size_t bmppad_sz = (4 - (w * 3) % 4) % 4;

    int filesize = 54 + 3 * w * h; //w is your image width, h is image height, both int

    bmpfileheader[2] = (unsigned char)(filesize);
    bmpfileheader[3] = (unsigned char)(filesize >> 8);
    bmpfileheader[4] = (unsigned char)(filesize >> 16);
    bmpfileheader[5] = (unsigned char)(filesize >> 24);

    bmpinfoheader[4] = (unsigned char)(w);
    bmpinfoheader[5] = (unsigned char)(w >> 8);
    bmpinfoheader[6] = (unsigned char)(w >> 16);
    bmpinfoheader[7] = (unsigned char)(w >> 24);
    bmpinfoheader[8] = (unsigned char)(h);
    bmpinfoheader[9] = (unsigned char)(h >> 8);
    bmpinfoheader[10] = (unsigned char)(h >> 16);
    bmpinfoheader[11] = (unsigned char)(h >> 24);

    f = fopen(filename, "wb");
    fwrite(bmpfileheader, 1, 14, f);
    fwrite(bmpinfoheader, 1, 40, f);
    for (int i = 0; i < h; i++)
    {
        fwrite(img + (w * (h - i - 1) * 3), 3, w, f);
        fwrite(bmppad, 1, bmppad_sz, f);
    }
    fclose(f);
}
