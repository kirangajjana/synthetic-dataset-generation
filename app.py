import pandas as pd
from faker import Faker
import random

fake = Faker()

# Dictionary to map categories to potential error descriptions
error_descriptions = {
    'Network': ['Connection lost intermittently', 'Slow internet speed', 'Unable to access shared drive', 'VPN connection issues'],
    'Software': ['Application crash', 'Unexpected error message', 'Feature not working as expected', 'License activation error'],
    'Hardware': ['Printer malfunction', 'Blue screen of death', 'Computer not booting', 'Monitor display issues'],
    'Account': ['Password reset required', 'Unable to log in', 'Two-factor authentication error', 'Account locked out']
}

def generate_ticket_data(num_tickets):
    data = []
    for _ in range(num_tickets):
        category = random.choice(list(error_descriptions.keys()))  # Choose category first
        ticket = {
            'Ticket_ID': str(random.randint(10000, 99999)),  # 5-digit ticket ID
            'Application_User_Name': fake.user_name(),
            'User_Email': fake.email(),
            'Error_Type': random.choice(['Connection Error', 'Timeout', 'Data Mismatch', 'Authorization Failure']),
            'Description': random.choice(error_descriptions[category]),  # Description matches category
            'Category': category,
            'Severity': random.choice(['Low', 'Medium', 'High']),
            'Time_Created': fake.date_time_this_decade().strftime('%H:%M:%S'),  # Format as HH:MM:SS
            'Error_Status': random.choice(['Open', 'In Progress', 'Pending', 'Closed']),
            'Error_Priority': random.choice(['Low', 'Medium', 'High']),
            'Support_Level': random.choices(['L1', 'L2', 'L3'], weights=[0.6, 0.3, 0.1])[0],
        }
        data.append(ticket)
    return pd.DataFrame(data)

# Generate 1000 tickets
num_tickets = 1000
df_tickets = generate_ticket_data(num_tickets)

# Save to CSV
csv_file_path = "ticket_data2.csv"
df_tickets.to_csv(csv_file_path, index=False)

print(f"Synthetic ticket data saved to {csv_file_path}")
