## out of scope
* out_of_scope
    - respond_out_of_scope
    - utter_posibilidades

## entrar datos fuera del flujo
* saludar
    - action_greet_user
* entrar_datos
    - utter_sin_estar_seguro
    - utter_posibilidades

## afirmar fuera del flujo
* saludar
    - action_greet_user
* afirmar
    - utter_entendido

## saludar fuera del flujo
* saludar
    - action_greet_user
* saludar OR entrar_datos{"nombre": "alejandra"}
    - action_greet_user