#include <QApplication>
#include <QObject>
#include <QString>
#include <QTimer>
#include <QFile>

#include <QNetworkAccessManager>
#include <QSqlDatabase>
#include <qtconcurrentfilter.h>
#include <QDomText>
#include <QtWidgets>

#include "greeter.h"

int main(int argc, char *argv[]){
    QApplication app(argc, argv);
    QApplication::setApplicationName("Application Example");
    QApplication::setApplicationVersion("1.0.0");

    QString name = argc > 0 ? argv[1] : "";
    if (name.isEmpty()) {
        name = "World";
    }

    Greeter* greeter = new Greeter(name, &app);
    QObject::connect(greeter, SIGNAL(finished()), &app, SLOT(quit()));
    QTimer::singleShot(0, greeter, SLOT(run()));

    QFile f(":/resource.txt");
    if(!f.open(QIODevice::ReadOnly))
        qFatal("Could not open resource file");
    qDebug() << "Resource content:" << f.readAll();
    f.close();

    QNetworkAccessManager networkTester;

    QSqlDatabase sqlTester;

    QVector<int> v;
    v << 1 << 2 << 3 << 4;
    QtConcurrent::blockingFilter(v, [](int i)
    {
        return i % 2;
    });

    QDomText xmlTester;

    QWidget* w = new QWidget();
    w->show();

    return app.exec();
}
