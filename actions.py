#This files contains your custom actions which can be used to run
#custom Python code.

#See this guide on how to implement these action:
#https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
# from rasa_sdk import Tracker, FormValidationAction
# from rasa_sdk.events import SlotSet

# def clean_name(name):
#     return "".join([c for c in name if c.isalpha()])
# class ValidateNewUser(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_new_user"
#     def validate_first_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         name = clean_name(slot_value)
#         if len(name) == 0:
#             dispatcher.utter_message(text="That must've been a typo.")
#             return {"first_name": None}
#         return {"first_name": name}
    
#     def validate_user_age(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         age = slot_value
#         if age <= 0:
#             dispatcher.utter_message(text="That must've been a typo.")
#             return {"user_age": None}
#         return {"user_age": age}

# class ValidateHealthInfo(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_health_form"
#     def validate_previous_conditions(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#         return{"previous_conditions": slot_value}
#     def validate_confirm_exercise(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
#        return{"confirm_exercise":slot_value}
#     def validate_stress_question_01(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#     ) -> Dict[Text, Any]:
    

# class ActionStressScore(Action):
#     def name(self) -> Text:
#         return "action_stress_score"
#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict:[Text, Any]]:
#         question01 = tracker.get_slot('stress_question_01')
#         question02 = tracker.get_slot('stress_question_02')
#         question03 = tracker.get_slot('stress_question_03')
#         question04 = tracker.get_slot('stress_question_04')
#         str_never = "Never"
#         str_almostNever = "Almost Never"
#         str_sometimes = "Sometimes"
#         str_often = "Fairly Often"
#         if question01 == str_never:
#             int_01 = 0
#         elif question01 == str_almostNever:
#             int_01 = 1
#         elif question01 == str_sometimes:
#             int_01 = 2
#         elif question01 == str_often:
#             int_01 = 3
#         else:
#             int_01 = 4
#         if question02 == str_never:
#             int_02 = 4
#         elif question02 == str_almostNever:
#             int_02 = 3
#         elif question02 == str_sometimes:
#             int_02 = 2
#         elif question02 == str_often:
#             int_02 = 1
#         else:
#             int_02 = 0
#         if question03 == str_never:
#             int_03 = 4
#         elif question03 == str_almostNever:
#             int_03 = 3
#         elif question03 == str_sometimes:
#             int_03 = 2
#         elif question03 == str_often:
#             int_03 = 1
#         else:
#             int_03 = 0
#         if question04 == str_never:
#             int_04 = 0
#         elif question04 == str_almostNever:
#             int_04 = 1
#         elif question04 == str_sometimes:
#             int_04 = 2
#         elif question04 == str_often:
#             int_04 = 3
#         else:
#             int_04 = 4
#         stressScore = int_01+int_02+int_03+int_04
#         return [SlotSet("percieved_stress",stressScore)]

# class ActionSleepScore(Action):
#     def name(self) -> Text:
#         return "action_sleep_score"
    
#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict:[Text, Any]]:
#         question01 = tracker.get_slot('sleep_question_01')
#         question03 = tracker.get_slot('sleep_question_03')
#         question04 = tracker.get_slot('sleep_question_04')
#         question05 = tracker.get_slot('sleep_question_05')
#         question06 = tracker.get_slot('sleep_question_06')
#         question07 = tracker.get_slot('sleep_question_07')
#         question08 = tracker.get_slot('sleep_question_08')
#         component_value = (question04/question05)*100
#         if question01 == "Very Good":
#             int_1 = 0
#         elif question01 == "Fairly Good":
#             int_1 = 1
#         elif question01 == "Fairly Bad":
#             int_1 = 2
#         else:
#             int_1 = 3
#         if question03 == "Never":
#             int_3 = 0
#         elif question03 == "Sometimes":
#             int_3 = 1
#         elif question03 == "Often":
#             int_3 = 2
#         else: 
#             int_3 = 3
#         if question04 > 7:
#             int_4 = 0
#         elif question04 >6:
#             int_4 = 1
#         elif question04 >5:
#             int_4 = 2
#         else:
#             int_4 = 3
#         if component_value >85:
#             int_5 = 0
#         elif component_value >75:
#             int_5 = 1
#         elif component_value > 65:
#             int_5 = 2
#         else: 
#             int_5 = 3
#         if question06 == "Never":
#             int_6 = 0
#         elif question06 == "Sometimes":
#             int_6 = 1
#         elif question06 == "Often":
#             int_6 = 2
#         else: 
#             int_6 = 3
#         if question07 == "Never":
#             int_7 = 0
#         elif question07 == "Sometimes":
#             int_7 = 1
#         elif question07 == "Often":
#             int_7 = 2
#         else: 
#             int_7 = 3
#         if question08 == "Never":
#             int_8 = 0
#         elif question08 == "Sometimes":
#             int_8= 1
#         elif question08 == "Often":
#             int_8 = 2
#         else: 
#             int_8 = 3
#         sleepScore = int_1+int_3+int_4+int_5+int_6+int_7+int_8
#         return [SlotSet("sleep_score",sleepScore)]

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
