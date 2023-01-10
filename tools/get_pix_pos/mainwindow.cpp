#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "main.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    set_connection();
    char mes[] = "./out.txt";
    m_fh = new QFile(mes);
    drawing_done_log = new QMessageBox(this);

    mark_index = 0;
    mark_width = MARK_WIDTH;
    mark_height = MARK_HEIGHT;
    scale = SCALE;

    for(int i = 0;i< MARK_NUMBER ; i++)
    {
        m_mark[i] = new QLabel(this);
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::set_connection()
{
    connect(ui->pos_export,&QAction::triggered,this,&MainWindow::export_pos);
    connect(ui->backword,&QMenu::aboutToShow,this,&MainWindow::back_word);
}


void MainWindow::mousePressEvent(QMouseEvent *event)
{
    if(event->x()<ui->label->x() || event->y()<ui->label->y()+ui->menubar->height())
        return;
    if(event->button() == Qt::LeftButton)
    {
        char text[MARK_NUMBER];
        sprintf(text,"x = %d y = %d number = %d",event->pos().x(),event->pos().y(),mark_index);
        this->statusBar()->showMessage(text);
        this->m_pos[this->mark_index] = Pos((event->x()-mark_width/2)/scale,
                                            (event->y()-mark_height/2)/scale);
        this->m_mark[this->mark_index]->setGeometry(event->x()-mark_width/2,event->y()-mark_height/2,
                                                   this->mark_width*scale,this->mark_height*scale);

        m_mark[this->mark_index]->setScaledContents(true);
        this->m_mark[this->mark_index]->setPixmap(pic_mark);
        qDebug()<<event->x()<<event->y()<<this->mark_width<<this->mark_height<<this->mark_index;

        this->m_mark[this->mark_index]->show();

        if(this->mark_index<MARK_NUMBER-1)
            this->mark_index++;
        else
        {
            this->drawing_done();
        }


    }
}

void MainWindow::drawing_done()
{
    this->drawing_done_log->setText("You've put enough marks");
    this->drawing_done_log->open();
}


void MainWindow::export_pos()
{
    qDebug()<<"saved";
    char mes[100] = "SPOTS_POS = [";
    this->m_fh->open(QIODevice::WriteOnly);
    this->m_fh->write(mes);
    for(int i = 0; i<MARK_NUMBER-1; i++)
    {
        sprintf(mes,"[%d,%d,%d,%d],\n",this->m_pos[i].x,this->m_pos[i].y,
                this->mark_width/scale,this->mark_height/scale);
        this->m_fh->write(mes);
    }
    sprintf(mes,"[%d,%d,%d,%d]\n",this->m_pos[MARK_NUMBER-1].x,this->m_pos[MARK_NUMBER-1].y,
            this->mark_width/scale,this->mark_height/scale);
    this->m_fh->write(mes);
    sprintf(mes,"]");
    this->m_fh->write(mes);
    m_fh->close();
}

void MainWindow::back_word()
{

    if(mark_index<=0)
        return;
    else
    {
        qDebug()<<"backed pre index is"<<mark_index;
        mark_index--;
        m_mark[mark_index]->hide();
    }

}
