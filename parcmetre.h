#include <cstdlib>
#include <iostream>

using namespace std;

class Parcmetre
{
private:
    int stock_papier;
    float solde;
public:
    void introduire_somme(int);
    void rendre_monnaie(int,int);
    void get_solde();
    void initialize_solde();
    void get_stock_papier();
    void initialize_stock_papier();
    void donner_tickets();
};
