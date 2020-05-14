#include <iostream>
#include <random>
#include <vector>
#include <string>
#include <map>
#include <ctime>

using namespace std;

string BuscarColor(int m){
  map<int,string> ruleta;
  ruleta.insert(pair<int,string>(0 , "Verde")) ;
  bool flag = true;
  for(int i = 1; i < 37; i++){
    if(flag == true && i != 28 && i != 10 && i != 19){
        ruleta.insert(pair<int,string>(i, "Rojo"));
        flag = false;

    }
    else if(i == 10 || i == 28){
      ruleta.insert(pair<int,string>(i, "Negro"));
      flag = false;
    }
    else if(i == 19){
      ruleta.insert(pair<int,string>(i, "Rojo"));
      flag = false;
    }
    else{
        ruleta.insert(pair<int,string>(i, "Negro"));
        flag = true;
    }
 }
   map<int,string>::iterator r = ruleta.find(m);
   string color = r->second;
   return color;
}

void LlenarVector(vector<pair<string,int>> &valores){
      srand(time(0));
      for(int i = 0; i < 20; i++){
        valores.push_back(make_pair("1", rand()%37));
      }
      for(int i = 0; i < 20; i++){
        valores[i].first = BuscarColor(valores[i].second);
      }
}
void CalcularEstadisticas(vector<pair<string,int>> &valores){
  double PromedioRojo = 0;
  double PromedioNegro = 0;

  for(unsigned int i = 0; i < valores.size(); i++){
    if(valores[i].first == "Rojo"){
      PromedioRojo += 1;
    }
    else{
      PromedioNegro +=1;
    }
  }
  cout << "El porcentaje en colores fue:   " << endl;
  cout << "Rojo: " << (PromedioRojo/2) * 10 << "%" << endl;
  cout << "Negro: " << (PromedioNegro/2) * 10 << "%";
  }

int main(){
  vector<pair<string,int>> prueba1;
  LlenarVector(prueba1);
  for(unsigned int i = 0; i < prueba1.size(); i++){
    cout << prueba1[i].first << "   " << prueba1[i].second << endl;
  }
  CalcularEstadisticas(prueba1);

}
