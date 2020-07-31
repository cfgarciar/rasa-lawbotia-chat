## out of scope
* out_of_scope
    - respond_out_of_scope
    - utter_posibilidades:

## entrar datos fuera del flujo
* saludar
    - utter_saludo
* entrar_datos
    - utter_sin_estar_seguro
    - utter_posibilidades:

## afirmar fuera del flujo
* saludar
    - utter_saludo
* afirmar
    - utter_entendido

## saludar fuera del flujo
* saludar
    - utter_saludo
* saludar OR entrar_datos{"nombre": "alejandra"}
    - utter_saludo