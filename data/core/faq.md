## faqs
* faq
    - respond_faq
    - action_set_faq_slot

## faqs
* faq{"producto": "consulta juridica"}
    - slot{"producto": "consulta juridica"}
    - respond_faq
    - action_set_faq_slot

## faqs
* faq{"producto": "documentos jurídicos"}
    - slot{"producto": "documentos jurídicos"}
    - respond_faq
    - action_set_faq_slot

## faqs
* faq{"producto": "asistente virtual"}
    - slot{"producto": "asistente virtual"}
    - respond_faq
    - action_set_faq_slot

## saludo + faqs
* saludar
    - action_greet_user
* faq
    - respond_faq
    - action_set_faq_slot

## saludo + mas faqs
* saludar
    - action_greet_user
* faq
    - respond_faq
    - action_set_faq_slot
* faq
    - respond_faq
    - action_set_faq_slot


## solo ventas
* saludar
    - action_greet_user
* faq
    - respond_faq
    - action_set_faq_slot
* pregunta_contactar_ventas
    - utter_mas_informacion

## FAQ - mas sobre lawbotia
* faq
    - respond_faq
    - action_set_faq_slot
* explicar
    - action_explain_faq

## FAQ - mas sobre canales
* faq
    - respond_faq
    - action_set_faq_slot
* explicar
    - action_explain_faq

## FAQ - mas sobre requisitos
* faq
    - respond_faq
    - action_set_faq_slot
* explicar
    - action_explain_faq

## FAQ - mas sobre costos 
* faq
    - respond_faq
    - action_set_faq_slot
* explicar
    - action_explain_faq

## FAQ - mas sobre servicios
* faq
    - respond_faq
    - action_set_faq_slot
* explicar
    - action_explain_faq

## Usuario Viejo + No intera
* saludar
    - action_greet_user
* pregunta_como_empezar
    - utter_empezar
    - utter_primer_servicio
* faq
    - respond_faq
    - action_set_faq_slot
    - utter_primer_servicio
* negar
    - utter_preguntar_cual_servicio
* negar
    - utter_thumbsup

## Usuario Viejo + No intera
* saludar
    - action_greet_user
* pregunta_como_empezar
    - utter_empezar
    - utter_primer_servicio
* negar
    - utter_preguntar_cual_servicio
* faq
    - respond_faq
    - action_set_faq_slot
    - utter_preguntar_cual_servicio
* negar
    - utter_thumbsup

## Usuario Viejo + Consultas Juridicas
* saludar
    - action_greet_user
* pregunta_como_empezar
    - utter_empezar
    - utter_primer_servicio
* negar
    - utter_preguntar_cual_servicio
* pregunta_como_empezar{"product": "consulta juridica"}
    - utter_consulta_juridica_especifico
* faq
    - respond_faq
    - action_set_faq_slot
    - utter_consulta_juridica_especifico
* negar
    - utter_info_general_consultas
    - utter_algo_mas

## Usuario Viejo + Consultas Juridicas + Desconocido
* saludar
    - action_greet_user
* pregunta_como_empezar
    - utter_empezar
    - utter_primer_servicio
* negar
    - utter_preguntar_cual_servicio
* pregunta_como_empezar{"product": "consulta juridica"}
    - utter_consulta_juridica_especifico
* faq
    - respond_faq
    - action_set_faq_slot
    - utter_consulta_juridica_especifico
* consultas_juridicas_info
    - action_store_unknown_consulta_juridica
    - utter_unknown_consulta_juridica
    - utter_escribir_mensaje
    - utter_algo_mas

## Usuario Viejo + Consultas Juridicas + Derechos de Peticion
* saludar
    - action_greet_user
* pregunta_como_empezar
    - utter_empezar
    - utter_primer_servicio
* negar
    - utter_preguntar_cual_servicio
* pregunta_como_empezar{"product": "consulta juridica"}
    - utter_consulta_juridica_especifico
* consultas_juridicas_info{"servicio": "derechos de peticion"}
    - utter_consultas_derechos de peticion
* faq
    - respond_faq
    - action_set_faq_slot
* negar
    - utter_thumbsup
    - utter_algo_mas

## Usuario Nuevo + conoce de chatbots 
* saludar
    - action_greet_user
* faq
    - respond_faq
    - action_set_faq_slot
* pregunta_como_empezar
    - utter_empezar
    - utter_nuevo_en_lawbotia
* afirmar
    - utter_primer_chatbot
* negar
    - utter_explicar_lawbotia
    - utter_explicar_servicios
    - utter_algo_mas
* afirmar OR how_to_get_started OR explain
    - utter_explicar_canales
    - utter_explicar_contacto

## Usuario Nuevo + no conoce de chatbots 
* saludar
    - action_greet_user
* faq
    - respond_faq
    - action_set_faq_slot
* pregunta_como_empezar
    - utter_empezar
    - utter_nuevo_en_lawbotia
* afirmar
    - utter_primer_chatbot
* afirmar
    - utter_explicar_chatbot
    - utter_explicar_servicios
    - utter_algo_mas
* afirmar OR how_to_get_started OR explain
    - utter_empezar
    - utter_explicar_contacto