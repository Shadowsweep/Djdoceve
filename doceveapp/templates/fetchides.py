from flask import Flask, jsonify

from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from doceveapp.serializers import StudentSerializer
from doceveapp.models import Student
from doceveapp.tuple_to_dict import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt




app = Flask(__name__)

@app.route('/get_ids', methods=['POST'])
def get_ids(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        # Execute the query to fetch all the IDs
        cursor.execute("SELECT enrollmentid FROM doceveapp_student")

        # Fetch all the IDs
        ids = [row[0] for row in cursor.fetchall()]
        # Print the array of IDs
        print(ids)

    # Return a response (optional)
    return jsonify(message='IDs fetched successfully')

if __name__ == '__main__':
    app.run()
