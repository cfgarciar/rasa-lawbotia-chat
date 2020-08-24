## saludo
* saludar
    - action_greet_user

## gracias
* agradecer
    - utter_de_nada
    - utter_algo_mas

## adios
* despedir
    - utter_adios

## algo mas? si
    - utter_algo_mas
* afirmar
    - utter_que_mas

## algo mas? no
    - utter_algo_mas
* negar
    - utter_entendido

## algo mas?
    - utter_algo_mas
* entrar_datos
    - utter_sin_estar_seguro
    - utter_posibilidades

## reaccion positiva
* reaccion_positiva
    - utter_reaccion_positiva

## reaccion negativa
* reaccion_negativa
    - utter_reaccion_negativa

## iniciar_conversacion
* iniciar_consulta
    - action_begin_user

## informacion en accion
* informacion
    - action_info_user

## guardar nombre usuario
* usuario_nombre{"guardar_nombre":"si"}
    - utter_grandioso
    - user_name_form
    - form{"name": "user_name_form"}
    - form{"name": null}
    - utter_posibilidades

## no guardar nombre usuario
* usuario_nombre{"guardar_nombre":"no"}
    - utter_sin_problemas
    - utter_posibilidades

## welcome
* welcome
    - action_welcome_user

    