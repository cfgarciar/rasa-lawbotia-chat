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
* contactar_ventas
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

## FAQ - solo ventas
* saludar
    - action_greet_user
* faq
    - respond_faq
    - action_set_faq_slot
* contactar_ventas
    - utter_mas_informacion
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_preguntar_feedback