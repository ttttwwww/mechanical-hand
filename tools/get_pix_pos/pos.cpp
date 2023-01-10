#include "pos.h"

Pos::Pos(int x,int y)
{
    this->x = x;
    this->y = y;

    qDebug()<<("pos saved");

}

Pos::Pos()
{
    this->x = 0;
    this->y = 0;
}

Pos::~Pos()
{
    printf("the number %d pos is deleted",this->index);
}
