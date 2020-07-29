## happy path
* saludar
  - utter_saludo
* animo_bien
  - utter_feliz

## sad path 1
* saludar
  - utter_saludo
* animo_mal
  - utter_animar
  - utter_te_ayude
* afirmar
  - utter_feliz

## sad path 2
* saludar
  - utter_saludo
* animo_mal
  - utter_animar
  - utter_te_ayude
* negar
  - utter_adios

## say goodbye
* despedir
  - utter_adios

## bot challenge
* pregunta_eres_robot
  - utter_soy_robot
