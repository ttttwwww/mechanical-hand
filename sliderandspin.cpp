#include "sliderandspin.h"
#include "ui_sliderandspin.h"

SliderAndSpin::SliderAndSpin(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SliderAndSpin)
{
    ui->setupUi(this);
}

SliderAndSpin::~SliderAndSpin()
{
    delete ui;
}

void SliderAndSpin::on_spinBox_valueChanged(int arg1)
{
    ui->horizontalSlider->setValue(arg1);
}
