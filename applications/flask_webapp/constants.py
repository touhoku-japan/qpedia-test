from flask import Flask, render_template, request, redirect, url_for, send_file, make_response, jsonify
import logging
from flask_cors import CORS
import sys
import os

app = Flask(__name__,
        static_url_path='', 
        static_folder='web/static',
        template_folder='web/templates'
        )
CORS(app)

app.secret_key = "somesecretkey"

## LOGGING configuration- change logging level for more output
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', 
                        stream=sys.stdout, 
                        level=logging.INFO, 
                        datefmt='%Y-%m-%d %H:%M:%S')