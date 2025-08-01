import json
import requests
import psycopg2

# Database connection settings
DB_HOST = 'SINTSA1049.infineon.com'
DB_NAME = 'ESH_Evacuation_DEV'
DB_USER = 'esh_evac_j01c'
DB_PASSWORD = 'QXxM400E&TE-OPS8-'

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
        cur.execute("UPDATE dbo.Employees SET time = %s, place = %s WHERE id = %s", (attendee['time'], attendee['place'], attendee['id']))
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
