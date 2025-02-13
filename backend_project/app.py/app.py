import os
import sys
from flask import Flask, jsonify, request

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Use absolute imports for project modules
from http.HttpHandler import HttpHandler
from database.DBConnection import DBConnection
from security.JWTManger import JWTManger
from security.FormatCheck import FormatCheck

# ... rest of the existing code ...