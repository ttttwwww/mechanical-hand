#ifndef POS_H
#define POS_H

#include<stdio.h>
#include"main.h"

class Pos
{
public:
    Pos(int x,int y);
    Pos();
    ~Pos();
    int x;
    int y;
    int index;
};

#endif // POS_H
