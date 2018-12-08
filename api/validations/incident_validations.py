# Import neccessary depencies
# Using re's pattern to match and find other strings or sets of strings
from api.models.user_models import User
from flask import Flask, jsonify, request, json
import re

class Validate:
    def validate_input(self):
        pass