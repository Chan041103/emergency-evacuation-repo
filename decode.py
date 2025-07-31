import base64
import json

# Let's assume you already have the API response stored in 'response'
# and have extracted the base64_content from response.json()['content']

# Example base64 content from GitHub API (shortened for illustration)
base64_content = "ewogICJkYXRlIjogIjIwMjUtMDctMzEiLAogICJ0aW1lc3RhbXAiOiAiMjAyNS0wNy0zMSAwNzowNzoxOCIsCiAgInJlY29yZGVyIjogIkNoYW4wNDExMDMiLAogICJhdHRlbmRlZXMiOiBbCiAgICB7Im5hbWUiOiAiU3R1ZGVudDEiLCAic3RhdHVzIjogInByZXNlbnQifSwKICAgIHsibmFtZSI6ICJTdHVkZW50MiIsICJzdGF0dXMiOiAiYWJzZW50In0KICBdCn0="

# Step 1: Decode Base64 to bytes
decoded_bytes = base64.b64decode(base64_content)

# Step 2: Convert bytes to string
decoded_content = decoded_bytes.decode('utf-8')

# Step 3: Parse JSON (if the content is JSON)
attendance_data = json.loads(decoded_content)

# Print the decoded content
print("Decoded content:")
print(decoded_content)

# Print the parsed JSON
print("\nParsed JSON:")
print(f"Date: {attendance_data['date']}")
print(f"Timestamp: {attendance_data['timestamp']}")
print(f"Recorder: {attendance_data['recorder']}")
print(f"Number of attendees: {len(attendance_data['attendees'])}")
