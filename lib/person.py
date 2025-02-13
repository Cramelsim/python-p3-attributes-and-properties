#!/usr/bin/env python3
class Person:

    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


    
    def __init__(self, name="John Doe", job="Admin"):
        self.name = name  # Calls the setter
        self.job = job  # Calls the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case before saving
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.__class__.APPROVED_JOBS:  # Ensure class attribute is accessed
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

