import datetime
import os

def load_sensitive_keywords():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(BASE_DIR, "utils", "keywords_list.txt")

    if not os.path.exists(filename):
        print(f"❌ Keyword file not found at {filename}")
        exit(1)

    with open(filename, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

def is_malicious_input(user_input, keywords):
    user_input_lower = user_input.lower()
    return any(keyword in user_input_lower for keyword in keywords)

def log_query(user_input, is_malicious):
    with open("query_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} | {'MALICIOUS' if is_malicious else 'SAFE'} | {user_input}\n")


keywords = load_sensitive_keywords()

print("🔐 HR Assistant Input Filter")
print("Type your query below. Type 'bye' to exit.\n")

while True:
    user_input = input("Enter a test query: ")

    if user_input.strip().lower() == "bye":
        print("👋 Goodbye!")
        break

    malicious = is_malicious_input(user_input, keywords)

    log_query(user_input, malicious)  

    if malicious:
        print("⚠️ Malicious query detected!\n")
    else:
        print("✅ Query looks safe.\n")

