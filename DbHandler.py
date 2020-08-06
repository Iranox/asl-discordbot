import mariadb
from dotenv import load_dotenv
import os
import logging
from datetime import datetime, timedelta

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")
HOST = os.getenv("DB_HOST")
PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")


class DbHandler:

    def __init__(self):
        try:
            connection = mariadb.connect(user=DB_USER, password=DB_PWD, host=HOST, port=PORT, database=DB_NAME)
        except mariadb.Error as e:
            logging.error("DbConnection error: " + str(e))
            self.cursor = None
            return
        self.cursor = connection.cursor()

    def add_quote(self, text, author, date, comment, recorded_by):
        statement = "INSERT INTO quotations (text,author"
        values = "VALUES (%(text)s,%(author)s"
        value_dict = {"text": text, "author": author}
        if date is not None:
            statement = statement + ",date"
            values = values + ",%(date)s"
            value_dict["date"] = date
        if comment is not None:
            statement = statement + ",comment"
            values = values + ",%(comment)s"
            value_dict["comment"] = comment
        if recorded_by is not None:
            statement = statement + ",recorded_by"
            values = values + ",%(recorded_by)s"
            value_dict["recorded_by"] = recorded_by
        statement = statement + ") " + values + ");"
        try:
            logging.info("Adding quote: " + statement + " with Values: " + str(value_dict))
            self.cursor.execute(statement, value_dict)
        except mariadb.Error as e:
            logging.error("Insertion failed: " + str(e))
            return False
        return True

    def get_quotes(self, from_time, until_time):
        value_dict = {}
        statement = "SELECT * FROM quotations"
        if from_time or until_time:
            statement = statement + " WHERE "
            if from_time:
                statement = statement + "date >= %(from_time)s"
                value_dict["from_time"] = from_time
                if until_time:
                    statement = statement + " AND date <= $(until_time)s"
                    value_dict["until_time"] = until_time
            else:
                statement = statement + "date <= %(until_time)s"
                value_dict["until_time"] = until_time
        statement = statement + ";"
        try:
            logging.info("Reading quotes: " + statement + " with Values: " + str(value_dict))
            self.cursor.execute(statement, value_dict)
            quotes = ""
            for (pk_id, date, text, author, comment, recorded_by) in self.cursor:
                logging.info("Read quote: " + str(pk_id) + " " + str(date) + " " + str(text) + " " + str(author) + " " + str(comment) + " " + str(recorded_by))
                quotes = quotes + "\nZitat: " + str(text) + "\nUrheber: " + str(author) + "\nZeitpunkt: " + str(date) + "\nKommentar: " + str(comment) + "\nEingereicht von: " + str(recorded_by) + "\n"
            logging.info("Read quotes: " + str(quotes))
            if quotes == "":
                quotes = "Keine Zitate (für den angegebenen Zeitraum?)"
            return quotes
        except mariadb.Error as e:
            logging.error("Reading failed: " + str(e))
            return False

    def insert_events(self, events):
        self.cursor.execute("DELETE FROM events;")
        for event in events:
            statement = "INSERT INTO events (date, object, details) VALUES (%(time)s, %(object)s, %(details)s);"
            try:
                logging.info("Inserting event: " + statement + " with values: " + str(event))
                self.cursor.execute(statement, event)
            except mariadb.Error as e:
                logging.error("Insertion failed: " + str(e))
        return True

    def get_events(self):
        try:
            self.cursor.execute("SELECT date, object, details FROM events;")
            events = []
            for (date, event_obj, details) in self.cursor:
                event_dict = {
                    "time": date,
                    "object": event_obj,
                    "details": details
                }
                events.append(event_dict)
            return events
        except mariadb.Error as e:
            logging.error("Reading events failed: " + str(e))
            return False

    def set_program(self, date, author, program):
        try:
            values = {
                "date": date,
                "author": author,
                "program": program
            }
            self.cursor.execute("DELETE FROM programs;")
            statement = "INSERT INTO programs (date, author, program) VALUES (%(date)s, %(author)s, %(program)s);"
            logging.info("Statement: " + statement)
            self.cursor.execute(statement, values)
            return True
        except mariadb.Error as e:
            logging.error("Inserting program failed: " + str(e))
            return False

    def get_program(self):
        try:
            self.cursor.execute("SELECT program FROM programs;")
            programs = []
            for p in self.cursor:
                programs.append(p)
            if len(programs) != 1:
                return "Es ist noch kein Programm gesetzt :("
            program = programs[0][0]
            program = program.replace("; ", "\n")
            return program
        except mariadb.Error as e:
            logging.error("Getting of program failed: " + str(e))
            return "Oops, da ist was schief gelaufen. Näheres in den Logs."
        except Exception as e:
            logging.error("Getting of program failed: " + str(e))
            return "Oops, da ist was schief gelaufen. Näheres in den Logs."

    def insert_munkel(self, text):
        try:
            self.cursor.execute("INSERT INTO munkel (text) VALUES (%(text)s);", {"text": text})
            return True
        except Exception as e:
            logging.error("Adding of munkel failed: " + str(e))
            return False

    def read_munkel(self, time_from=None, time_until=None):
        statement = "SELECT text FROM munkel"
        if not time_from:
            time_from = datetime.now() - timedelta(days=1)
        param_dict = {"time_from": time_from}
        statement += " WHERE timestamp>=%(time_from)s"
        if time_until:
            " AND timestamp<=%(time_until)s"
            param_dict["time_until"] = time_until
        statement += ";"
        try:
            self.cursor.execute(statement, param_dict)
            munkels = ""
            for munkel in self.cursor:
                munkels += munkel + "\n"
            return munkels
        except Exception as e:
            logging.error("Getting of munkel failed: " + str(e))
            return "Oops, da ist was schief gelaufen. Näheres in den Logs."
