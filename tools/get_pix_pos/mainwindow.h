#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QApplication>
#include "main.h"
#include <QLabel>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

typedef void (mark_deploy_callback)(int width,int height);

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void set_connection();
    void mousePressEvent(QMouseEvent *event);
    void drawing_done();
    void export_pos();
    void back_word();
private:
    Ui::MainWindow *ui;


public:
    Pos* m_pos = new Pos[MARK_NUMBER];
    QLabel* m_mark[MARK_NUMBER]  ;
    QPixmap pic_hand=QPixmap(":mark/Resources/hand.png");
    QPixmap pic_mark=QPixmap(":mark/Resources/mark.png");
    QMessageBox* drawing_done_log;
    QFile* m_fh;

    int mark_index;
    int mark_width;
    int mark_height;
    int scale;

    char* path_pos_out;

};


#endif // MAINWINDOW_H
