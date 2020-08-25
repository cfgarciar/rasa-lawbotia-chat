import json
from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)


INTENT_DESCRIPTION_MAPPING_PATH = "actions/intent_description_mapping.csv"


class ActionWelcomeUser(Action):
    def name(self) -> Text:
        return "action_welcome_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        dispatcher.utter_message(template="utter_welcome_avatar")
        dispatcher.utter_message(template="utter_welcome_saludo")
        dispatcher.utter_message(template="utter_welcome_angel")
        dispatcher.utter_message(template="utter_welcome_continuar")
        return [SlotSet("conversacion_iniciada", False)]


class ActionBeginUser(Action):
    def name(self) -> Text:
        return "action_begin_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        dispatcher.utter_message(template="utter_comencemos")
        dispatcher.utter_message(template="utter_informar_privacidad")
        dispatcher.utter_message(template="utter_pedir_nombre")
        return [SlotSet("shown_privacy", True), SlotSet("conversacion_iniciada", True)]


class ActionInfoUser(Action):
    def name(self) -> Text:
        return "action_info_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        info = next(tracker.get_latest_entity_values("info"), None)
        if info == "general":
            dispatcher.utter_message(template="utter_info_general")
            dispatcher.utter_message(template="utter_especificar")
            return []
        elif info == "consulta":
            dispatcher.utter_message(template="utter_info_consulta")
            dispatcher.utter_message(template="utter_especificar")
            return []
        elif info == "documento":
            dispatcher.utter_message(template="utter_info_documento")
            dispatcher.utter_message(template="utter_especificar")
            return []
        elif info == "otro":
            dispatcher.utter_message(template="utter_info_otro")
            dispatcher.utter_message(template="utter_especificar")
            return []
        else:
            dispatcher.utter_message(template="utter_info_error")
            dispatcher.utter_message(template="utter_especificar")
            return []


class UserNameForm(FormAction):
    """Accept free text input from the user for suggestions"""

    def name(self) -> Text:
        return "user_name_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return ["nombre"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "nombre": [
                self.from_entity(entity="nombre"),
                self.from_text(intent="entrar_datos"),
            ]
        }

    def submit(self, dispatcher, tracker, domain) -> List[EventType]:
        nombre = tracker.get_slot("nombre")
        dispatcher.utter_message(template="utter_agradecer_nombre")
        return []


class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:

        intent = tracker.latest_message["intent"].get("name")
        shown_privacy = tracker.get_slot("shown_privacy")
        name_entity = next(tracker.get_latest_entity_values("nombre"), None)

        if intent == "saludar" or (intent == "entrar_datos" and name_entity):
            if shown_privacy and name_entity and name_entity.lower() != "angel":
                dispatcher.utter_message(
                    template="utter_saludo_nombre", name=name_entity
                )
                return []
            elif shown_privacy:
                dispatcher.utter_message(template="utter_saludo_no_nombre")
                return []
            else:
                dispatcher.utter_message(template="utter_saludo")
                dispatcher.utter_message(template="utter_utter_informar_privacidad")
                dispatcher.utter_message(template="utter_preguntar_meta")
                return [SlotSet("shown_privacy", True)]
        else:
            dispatcher.utter_message(template="utter_saludo")
            return []


class ActionExplainFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_explain_faq"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:

        topic = tracker.get_slot("faq")

        if topic in ["lawbotia", "canales", "requisitos", "costos", "servicios"]:
            dispatcher.utter_message(template=f"utter_faq_{topic}_mas")
        else:
            dispatcher.utter_message(template="utter_no_mas_info")

        return []


class ActionSetFaqSlot(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        return "action_set_faq_slot"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        full_intent = (
            tracker.latest_message.get("response_selector", {})
            .get("faq", {})
            .get("full_retrieval_intent")
        )
        if full_intent:
            topic = full_intent.split("/")[1]
        else:
            topic = None

        return [SlotSet("faq", topic)]


class ActionGuardarproductoDesconocido(Action):
    """Stores unknown tools people are migrating from in a slot"""

    def name(self) -> Text:
        return "action_guardar_producto_desconocido"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        return [SlotSet("producto_desconocido", tracker.latest_message.get("text"))]


class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv(INTENT_DESCRIPTION_MAPPING_PATH)
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]
        print(intent_ranking)        

        # for the intent name used to retrieve the button title, we either use
        # the name of the name of the "main" intent, or if it's an intent that triggers
        # the response selector, we use the full retrieval intent name so that we
        # can distinguish between the different sub intents

        first_intent_names = [
            intent.get("name", "")
            if intent.get("name", "") not in ["out_of_scope", "faq", "chitchat"]
            else tracker.latest_message.get("response_selector")
            .get(intent.get("name", ""))
            .get("full_retrieval_intent")
            for intent in intent_ranking
        ]
        print(first_intent_names) 

        message_title = (
            "Lo siento, no estoy segura de haber entendido" "correctamente 🤔 ¿Quieres decir ..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)
        print(entities_json) 

        buttons = []
        for intent in first_intent_names:
            button_title = get_button_title(intent, entities)
            if "/" in intent:
                # here we use the button title as the payload as well, because you
                # can't force a response selector sub intent, so we need NLU to parse
                # that correctly
                buttons.append({"title": button_title, "payload": button_title})
            else:
                buttons.append(
                    {"title": button_title, "payload": f"/{intent}{entities_json}"}
                )

        buttons.append({"title": "Algún otro asunto", "payload": "/trigger_rephrase"})

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []


def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:

    default_utterance_query = self.intent_mappings.intent == intent

    utterance_query = (self.intent_mappings.entities == entities.keys()) & (
        default_utterance_query
    )

    utterances = self.intent_mappings[utterance_query].button.tolist()

    if len(utterances) > 0:
        button_title = utterances[0]
    else:
        utterances = self.intent_mappings[
            default_utterance_query
        ].button.tolist()
        button_title = utterances[0] if len(utterances) > 0 else intent

    return button_title.format(**entities)


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):

            dispatcher.utter_message(template="utter_restart_with_button")

            return [SlotSet("feedback_value", "negativo"), ConversationPaused()]

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_default")
            return [UserUtteranceReverted()]
