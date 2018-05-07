#include <iostream>
#include <cstdlib>
#include "parcmetre.h"
#include <string>

using namespace std;

int main()
{
    Parcmetre garer;
    garer.initialize_solde();
    garer.initialize_stock_papier();
    garer.get_solde();
    garer.get_stock_papier();
    garer.introduire_somme(256);
    garer.get_solde();
    garer.rendre_monnaie(256,125);
    garer.get_solde();
    garer.donner_tickets();
    garer.get_stock_papier();


}
