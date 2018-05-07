#include <iostream>
#include <cstdlib>
#include "parcmetre.h"
#include <string>

using namespace std;

void Parcmetre::introduire_somme(int a)
{
    solde=solde+a;
}

void Parcmetre::rendre_monnaie(int a,int b)
{
    /*
    a représente la valeur rentrée dans le parcmètre en euros,
    b représente le temps demandé en minutes pour garer la voiture.
    On a obligatoirement a>=b.
    */
    solde=solde-(a-(b/50));
}

void Parcmetre::get_solde()
{
    cout << "Il y a " << solde <<" euros dans le parcmetre"<<endl;
}

void Parcmetre::initialize_solde()
{
    solde=0;
}

void Parcmetre::get_stock_papier()
{
    cout << "Il reste " << stock_papier << " tickets dans le parcmetre." << endl;
}

void Parcmetre::initialize_stock_papier()
{
    stock_papier=100;
}

void Parcmetre::donner_tickets()
{
    stock_papier=stock_papier-1;
}
