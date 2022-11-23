#ifndef SLIDERANDSPIN_H
#define SLIDERANDSPIN_H

#include <QWidget>

namespace Ui {
class SliderAndSpin;
}

class SliderAndSpin : public QWidget
{
    Q_OBJECT

public:
    explicit SliderAndSpin(QWidget *parent = nullptr);
    ~SliderAndSpin();

private slots:
    void on_spinBox_valueChanged(int arg1);

private:
    Ui::SliderAndSpin *ui;
};

#endif // SLIDERANDSPIN_H
