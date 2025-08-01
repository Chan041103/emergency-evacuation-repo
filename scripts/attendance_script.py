import json
import requests
import psycopg2

# Database connection settings
DB_HOST = 'your_database_host'
DB_NAME = 'your_database_name'
DB_USER = 'your_database_user'
DB_PASSWORD = 'your_database_password'

# GitHub API key
GITHUB_API_KEY = 'your_github_api_key'

def process_attendees(data):
    # Process the attendees data
    attendees_data = json.loads(data)
    attendees = attendees_data['attendees']

    # Connect to the database
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()

    # Insert attendees data into the database
    for attendee in attendees:
        cur.execute("INSERT INTO attendance (id, time, place) VALUES (%s, %s, %s)", (attendee['id'], attendee['time'], attendee['place']))
    conn.commit()

    # Close the database connection
    cur.close()
    conn.close()

    # Return a success message
    return 'Attendees data sent to database successfully!'

def main():
    # Receive attendees data from Postman
    data = request.get_json()
    if data:
        process_attendees(data)
    else:
        return 'No attendees data received.'

if __name__ == '__main__':
    main()
