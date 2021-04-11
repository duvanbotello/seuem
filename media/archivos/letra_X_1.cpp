#include <iostream>
using namespace std;

int main(){

    /** BUCLES

    Realiza un programa que pinte una X hecha de asteriscos. El programa debe pedir la altura. Se debe comprobar que la altura sea un numero impar mayor
    o igual a 3, en caso contrario de debe mostrar un mensaje de error.

    **/


    int alturaIntroducida;

    cout<<"Ingresar la altura de la X: ";
    cin>>alturaIntroducida;

    int altura = 1;
    int i = 0;
    int espaciosInternos = alturaIntroducida - 1;
    int espaciosDelantes = 0;

    if((alturaIntroducida < 3) || (alturaIntroducida % 2 == 0)){
        cout<<"Error, datos incorrectos, debe introducir una altura impar mayor o igual a 3";
    } else {
        while(altura < alturaIntroducida / 2 + 1){
            for(i = 1; i <= espaciosDelantes; i++){
                cout<<" ";
            }
            cout<<"*";
            for(i = 1; i < espaciosInternos; i++){
                cout<<" ";
            }
            cout<<"*";
            cout<<""<<endl;
            altura++;
            espaciosDelantes++;
            espaciosInternos -= 2;
        }
        espaciosInternos = 0;
        espaciosDelantes = alturaIntroducida / 2;
        altura = 1;
        while(altura <= alturaIntroducida / 2 + 1){
            for(i = 1; i <= espaciosDelantes; i++){
                cout<<" ";
            }
            cout<<"*";
            for(i = 1; i < espaciosInternos; i++){
                cout<<" ";
            }
            if(altura>1){
                cout<<"*";
            }
            cout<<""<<endl;
            altura++;
            espaciosDelantes--;
            espaciosInternos+=2;
        }
    }
}
