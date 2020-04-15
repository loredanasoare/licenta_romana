from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
import datetime

adminUser = False
normalUser = False


class ActionCredentials(Action):
    def name(self) -> Text:
        return "action_ask_about_credentials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user = next(tracker.get_latest_entity_values('user'), None)
        print(user)
        if "admin" in str(user):
            adminUser = True
        elif "normal" in str(user):
            normalUser = True

        return []


class ActionPulse(Action):
    def name(self) -> Text:
        return "action_ask_about_pulse"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        pulse = next(tracker.get_latest_entity_values('pulse'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if pulse is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Pulsul tau este " + str(dataDf.get_value(0, 'pulse')))
                    file.write("Pulsul tau este " + str(dataDf.get_value(0, 'pulse')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Pulsul tau este " + str(dataDf.get_value(0, 'pulse')))
                    file.write("Pulsul tau este " + str(dataDf.get_value(0, 'pulse')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Pulsul tau este " + str(dataDf.get_value(0, 'pulse')))
                    file.write("Pulsul tau este " + str(dataDf.get_value(0, 'pulse')))
                    file.write("\n")
                file.close()
                return []
            azi = None
        elif yesterday is not None:
            if pulse is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Pulsul tau este " + str(dataDf.get_value(1, 'pulse')))
                    file.write("Pulsul tau este " + str(dataDf.get_value(1, 'pulse')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Pulsul tau este " + str(dataDf.get_value(1, 'pulse')))
                    file.write("Pulsul tau este " + str(dataDf.get_value(1, 'pulse')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Pulsul tau este " + str(dataDf.get_value(1, 'pulse')))
                    file.write("Pulsul tau este " + str(dataDf.get_value(1, 'pulse')))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []


class ActionHealth(Action):
    def name(self) -> Text:
        return "action_ask_about_health"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        health = next(tracker.get_latest_entity_values('health'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if health is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Sanatatea ta este " + str(dataDf.get_value(0, 'health')))
                    file.write("Sanatatea ta este " + str(dataDf.get_value(0, 'health')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Sanatatea ta este " + str(dataDf.get_value(0, 'health')))
                    file.write("Sanatatea ta este " + str(dataDf.get_value(0, 'health')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Sanatatea ta este " + str(dataDf.get_value(0, 'health')))
                    file.write("Sanatatea ta este " + str(dataDf.get_value(0, 'health')))
                    file.write("\n")
                file.close()
                return []
            azi = None
        elif yesterday is not None:
            if health is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Sanatatea ta este " + str(dataDf.get_value(1, 'health')))
                    file.write("Sanatatea ta este " + str(dataDf.get_value(1, 'health')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Sanatatea ta este " + str(dataDf.get_value(1, 'health')))
                    file.write("Sanatatea ta este " + str(dataDf.get_value(1, 'health')))
                    file.write("\n")

                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Sanatatea ta este " + str(dataDf.get_value(1, 'health')))
                    file.write("Sanatatea ta este " + str(dataDf.get_value(1, 'health')))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []


class ActionSteps(Action):
    def name(self) -> Text:
        return "action_ask_about_steps"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        steps = next(tracker.get_latest_entity_values('steps'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if steps is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Numarul tau de pasi este " + str(dataDf.get_value(0, 'steps')))
                    file.write("Numarul tau de pasi este " + str(dataDf.get_value(0, 'steps')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Numarul tau de pasi este " + str(dataDf.get_value(0, 'steps')))
                    file.write("Numarul tau de pasi este " + str(dataDf.get_value(0, 'steps')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Numarul tau de pasi este " + str(dataDf.get_value(0, 'steps')))
                    file.write("Numarul tau de pasi este " + str(dataDf.get_value(0, 'steps')))
                    file.write("\n")
                file.close()
                return []
            azi = None
        elif yesterday is not None:
            if steps is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Numarul tau de pasi este " + str(dataDf.get_value(1, 'steps')))
                    file.write("Numarul tau de pasi este " + str(dataDf.get_value(1, 'steps')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Numarul tau de pasi este " + str(dataDf.get_value(1, 'steps')))
                    file.write("Numarul tau de pasi este " + str(dataDf.get_value(1, 'steps')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Numarul tau de pasi este " + str(dataDf.get_value(1, 'steps')))
                    file.write("Numarul tau de pasi este " + str(dataDf.get_value(1, 'steps')))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.close()
        return []


class ActionBloodPressure(Action):
    def name(self) -> Text:
        return "action_ask_about_blood_pressure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        blood_pressure = next(tracker.get_latest_entity_values('blood_pressure'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            print("intra aici")
            print(str(target))
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if blood_pressure is not None:
                if "diastolică" in str(blood_pressure):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message(
                            "Presiunea diastolica este " + str(dataDf.get_value(0, 'diastolic_pressure')))
                        file.write("Presiunea diastolica este " + str(dataDf.get_value(0, 'diastolic_pressure')))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message(
                            "Presiunea diastolica este " + str(dataDf.get_value(0, 'diastolic_pressure')))
                        file.write("Presiunea diastolica este " + str(dataDf.get_value(0, 'diastolic_pressure')))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message(
                            "Presiunea diastolica este " + str(dataDf.get_value(0, 'diastolic_pressure')))
                        file.write("Presiunea diastolica este " + str(dataDf.get_value(0, 'diastolic_pressure')))
                        file.write("\n")
                    file.close()
                    return []
                elif "sistolică" in str(blood_pressure):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message(
                            "Presiunea sistolica este " + str(dataDf.get_value(0, 'systolic_pressure')))
                        file.write("Presiunea sistolica este " + str(dataDf.get_value(0, 'systolic_pressure')))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message(
                            "Presiunea sistolica este " + str(dataDf.get_value(0, 'systolic_pressure')))
                        file.write("Presiunea sistolica este " + str(dataDf.get_value(0, 'systolic_pressure')))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message(
                            "Presiunea sistolica este " + str(dataDf.get_value(0, 'systolic_pressure')))
                        file.write("Presiunea sistolica este " + str(dataDf.get_value(0, 'systolic_pressure')))
                        file.write("\n")
                    file.close()
                    return []
                else:
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message("Tensiunea este " + str(dataDf.get_value(0, 'blood_pressure')))
                        file.write("Tensiunea este " + str(dataDf.get_value(0, 'blood_pressure')))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message("Tensiunea este " + str(dataDf.get_value(0, 'blood_pressure')))
                        file.write("Tensiunea este " + str(dataDf.get_value(0, 'blood_pressure')))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message("Tensiunea este " + str(dataDf.get_value(0, 'blood_pressure')))
                        file.write("Tensiunea este " + str(dataDf.get_value(0, 'blood_pressure')))
                        file.write("\n")
                    file.close()
                    return []

            azi = None
        elif yesterday is not None:
            if blood_pressure is not None:
                if "diastolică" in str(blood_pressure):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message(
                            "Presiunea diastolica este " + str(dataDf.get_value(1, 'diastolic_pressure')))
                        file.write("Presiunea diastolica este " + str(dataDf.get_value(1, 'diastolic_pressure')))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message(
                            "Presiunea diastolica este " + str(dataDf.get_value(1, 'diastolic_pressure')))
                        file.write("Presiunea diastolica este " + str(dataDf.get_value(1, 'diastolic_pressure')))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message(
                            "Presiunea diastolica este " + str(dataDf.get_value(1, 'diastolic_pressure')))
                        file.write("Presiunea diastolica este " + str(dataDf.get_value(1, 'diastolic_pressure')))
                        file.write("\n")
                    file.close()
                    return []
                elif "sistolică" in str(blood_pressure):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message(
                            "Presiunea sistolica este " + str(dataDf.get_value(1, 'systolic_pressure')))
                        file.write("Presiunea sistolica este " + str(dataDf.get_value(1, 'systolic_pressure')))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message(
                            "Presiunea sistolica este " + str(dataDf.get_value(1, 'systolic_pressure')))
                        file.write("Presiunea sistolica este " + str(dataDf.get_value(1, 'systolic_pressure')))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message(
                            "Presiunea sistolica este " + str(dataDf.get_value(1, 'systolic_pressure')))
                        file.write("Presiunea sistolica este " + str(dataDf.get_value(1, 'systolic_pressure')))
                        file.write("\n")
                    file.close()
                    return []
                else:
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message("Tensiunea este " + str(dataDf.get_value(1, 'blood_pressure')))
                        file.write("Tensiunea este " + str(dataDf.get_value(1, 'blood_pressure')))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message("Tensiunea este " + str(dataDf.get_value(1, 'blood_pressure')))
                        file.write("Tensiunea este " + str(dataDf.get_value(1, 'blood_pressure')))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message("Tensiunea este " + str(dataDf.get_value(1, 'blood_pressure')))
                        file.write("Tensiunea este " + str(dataDf.get_value(1, 'blood_pressure')))
                        file.write("\n")
                    file.close()
                    return []

            azi = None
        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []


class ActionCalendar(Action):
    def name(self) -> Text:
        return "action_ask_about_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        calendar = next(tracker.get_latest_entity_values('calendar'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        tomorrow = next(tracker.get_latest_entity_values('tomorrow'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if calendar is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(0, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(0, 'calendar')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(0, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(0, 'calendar')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(0, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(0, 'calendar')))
                    file.write("\n")
                file.close()
                return []
            azi = None
        elif yesterday is not None:
            if calendar is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(1, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(1, 'calendar')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(1, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(1, 'calendar')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(1, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(1, 'calendar')))
                    file.write("\n")
                file.close()
                return []
        elif tomorrow is not None:
            if calendar is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(2, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(2, 'calendar')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(2, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(2, 'calendar')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Planurile sunt " + str(dataDf.get_value(2, 'calendar')))
                    file.write("Planurile sunt " + str(dataDf.get_value(2, 'calendar')))
                    file.write("\n")
                file.close()
                return []
        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []


class ActionWeight(Action):
    def name(self) -> Text:
        return "action_ask_about_weight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        weight = next(tracker.get_latest_entity_values('weight'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if weight is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Greutatea ta este " + str(dataDf.get_value(0, 'weight')))
                    file.write("Greutatea ta este " + str(dataDf.get_value(0, 'weight')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Greutatea ta este " + str(dataDf.get_value(0, 'weight')))
                    file.write("Greutatea ta este " + str(dataDf.get_value(0, 'weight')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Greutatea ta este " + str(dataDf.get_value(0, 'weight')))
                    file.write("Greutatea ta este " + str(dataDf.get_value(0, 'weight')))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []


class ActionSleep(Action):
    def name(self) -> Text:
        return "action_ask_about_sleep"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        sleep = next(tracker.get_latest_entity_values('sleep'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        if (today is None or today is not None) and yesterday is None:
            if sleep is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Numarul de ore de somn este " + str(dataDf.get_value(0, 'sleep')))
                    file.write("Numarul de ore de somn este " + str(dataDf.get_value(0, 'sleep')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Numarul de ore de somn este " + str(dataDf.get_value(0, 'sleep')))
                    file.write("Numarul de ore de somn este " + str(dataDf.get_value(0, 'sleep')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Numarul de ore de somn este " + str(dataDf.get_value(0, 'sleep')))
                    file.write("Numarul de ore de somn este " + str(dataDf.get_value(0, 'sleep')))
                    file.write("\n")
                file.close()
                return []
            azi = None
        elif yesterday is not None:
            if sleep is not None:
                if display is not None:
                    dispatcher.utter_message("Afisare")
                    dispatcher.utter_message("Numarul de ore de somn a fost " + str(dataDf.get_value(1, 'sleep')))
                    file.write("Numarul de ore de somn a fost " + str(dataDf.get_value(1, 'sleep')))
                    file.write("\n")
                elif say is not None:
                    dispatcher.utter_message("Exprimare")
                    dispatcher.utter_message("Numarul de ore de somn a fost " + str(dataDf.get_value(1, 'sleep')))
                    file.write("Numarul de ore de somn a fost " + str(dataDf.get_value(1, 'sleep')))
                    file.write("\n")
                else:
                    dispatcher.utter_message("Afisare + Exprimare")
                    dispatcher.utter_message("Numarul de ore de somn a fost " + str(dataDf.get_value(1, 'sleep')))
                    file.write("Numarul de ore de somn a fost " + str(dataDf.get_value(1, 'sleep')))
                    file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []


class ActionTime(Action):
    def name(self) -> Text:
        return "action_ask_about_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        time = next(tracker.get_latest_entity_values('time'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        yesterday = next(tracker.get_latest_entity_values('yesterday'), None)
        display = next(tracker.get_latest_entity_values('display_actions'), None)
        say = next(tracker.get_latest_entity_values('say_actions'), None)
        target = next(tracker.get_latest_entity_values('target'), None)

        if ("my" not in str(target) or "I" not in str(target)) and normalUser is True:
            dispatcher.utter_message(template="utter_incorrect_credentials")
            return []

        currentDT = datetime.datetime.now()
        if (today is None or today is not None) and yesterday is None:
            if time is not None:
                if "ceas" in str(time) or "ora" in str(time):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message("Este ora " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("Este ora " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message("Este ora " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("Este ora " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message("Este ora " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("Este ora " + str(currentDT.strftime("%H:%M:%S")))
                        file.write("\n")
                    file.close()
                    return []
                if "zi" in str(time):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message("Este ziua " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("Este ziua " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message("Este ziua " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("Este ziua " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message("Este ziua " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("Este ziua " + str(currentDT.strftime("%Y/%m/%d")))
                        file.write("\n")
                    file.close()
                    return []
                if "lună" in str(time):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message("Este luna %d" % currentDT.month)
                        file.write("Este luna %d" % currentDT.month)
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message("Este luna %d" % currentDT.month)
                        file.write("Este luna %d" % currentDT.month)
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message("Este luna %d" % currentDT.month)
                        file.write("Este luna %d" % currentDT.month)
                        file.write("\n")
                    file.close()
                    return []
                if "an" in str(time):
                    if display is not None:
                        dispatcher.utter_message("Afisare")
                        dispatcher.utter_message("Este anul %d" % currentDT.year)
                        file.write("Este anul %d" % currentDT.year)
                        file.write("\n")
                    elif say is not None:
                        dispatcher.utter_message("Exprimare")
                        dispatcher.utter_message("Este anul %d" % currentDT.year)
                        file.write("Este anul %d" % currentDT.year)
                        file.write("\n")
                    else:
                        dispatcher.utter_message("Afisare + Exprimare")
                        dispatcher.utter_message("Este anul %d" % currentDT.year)
                        file.write("Este anul %d" % currentDT.year)
                        file.write("\n")
                    file.close()
                    return []

        dispatcher.utter_message(template="utter_repeat")
        file.close()
        return []


class ActionWeather(Action):
    def name(self) -> Text:
        return "action_ask_about_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")
        data = pd.read_csv("date.csv", sep=',')
        dataDf = pd.DataFrame(data)

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        weather = next(tracker.get_latest_entity_values('weather'), None)
        today = next(tracker.get_latest_entity_values('today'), None)
        tomorrow = next(tracker.get_latest_entity_values('tomorrow'), None)

        if (today is None or today is not None) and tomorrow is None:
            if weather is not None:
                dispatcher.utter_message("Vremea este " + str(dataDf.get_value(0, 'weather')))
                file.write("Vremea este " + str(dataDf.get_value(0, 'weather')))
                file.write("\n")
                file.close()
                return []
        elif tomorrow is not None:
            if weather is not None:
                dispatcher.utter_message("Vremea va fi " + str(dataDf.get_value(2, 'weather')))
                file.write("Vremea va fi " + str(dataDf.get_value(2, 'weather')))
                file.write("\n")
                file.close()
                return []

        dispatcher.utter_message(template="utter_repeat")
        file.close()
        return []


class ActionPerson(Action):
    def name(self) -> Text:
        return "action_ask_about_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        dispatcher.utter_message(template="utter_person")
        file.write("Eu sunt bot-ul Rasa")
        file.write("\n")
        file.close()
        return []


class ActionPage(Action):
    def name(self) -> Text:
        return "action_ask_about_page_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        file = open("outputRomana.csv", "a")

        last_message = tracker.latest_message.get("text", "")
        file.write(str(last_message))
        file.write(",")

        page_type = next(tracker.get_latest_entity_values('page_type'), None)

        if page_type is not None:
            if "principală" in page_type:
                dispatcher.utter_message("Mergi la pagina principala")
                file.write("Mergi la pagina principala")
                file.write("\n")
            elif "anterioară" in page_type:
                dispatcher.utter_message("Mergi la pagina anterioara")
                file.write("Mergi la pagina anterioara")
                file.write("\n")
            else:
                dispatcher.utter_message("Mergi la pagina urmatoare")
                file.write("Mergi la pagina urmatoare")
                file.write("\n")
            file.close()
            return []

        dispatcher.utter_message(template="utter_repeat")

        file.close()
        return []
