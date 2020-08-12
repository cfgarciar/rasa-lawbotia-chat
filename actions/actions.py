# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


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


class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:

        intent = tracker.latest_message["intent"].get("name")
        shown_privacy = tracker.get_slot("shown_privacy")
        name_entity = next(tracker.get_latest_entity_values("name"), None)

        if intent == "saludar" or (intent == "entrar_datos" and name_entity):
            if shown_privacy and name_entity and name_entity.lower() != "sara":
                dispatcher.utter_message(
                    template="utter_saludo_nombre", name=name_entity
                )
                return []
            elif shown_privacy:
                dispatcher.utter_message(template="utter_saludo_no_nombre")
                return []
            else:
                dispatcher.utter_message(template="utter_saludo")
                dispatcher.utter_message(template="utter_inform_privacypolicy")
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



class ActionPause(Action):
    """Pause the conversation"""

    def name(self) -> Text:
        return "action_pause"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        return [ConversationPaused()]



class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "sales_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return [
            "person_name",
            "business_email"
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "person_name": [
                self.from_entity(entity="nombre"),
                self.from_text(intent="entrar_datos"),
            ],
            "business_email": [
                self.from_entity(entity="email"),
                self.from_text(intent="entrar_datos"),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""

        import datetime

        email = tracker.get_slot("business_email")
        person_name = tracker.get_slot("person_name")
        date = datetime.datetime.now().strftime("%d/%m/%Y")

        sales_info = [date, person_name, email]

        try:
            gdrive = GDriveService()
            gdrive.store_data(sales_info)
            dispatcher.utter_message(template="utter_confirm_salesrequest")
            return []
        except Exception as e:
            logger.error(
                "Failed to write data to gdocs. Error: {}" "".format(e.message),
                exc_info=True,
            )
            dispatcher.utter_message(template="utter_salesrequest_failed")
            return []