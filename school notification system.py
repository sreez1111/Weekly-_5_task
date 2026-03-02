# Base class
class Notification:
    def send_message(self):
        print("Sending a generic notification...")

# Subclass 1
class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email 📧")

# Subclass 2
class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS 📱")

# Subclass 3
class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via Mobile App 🔔")

# Creating objects
email = EmailNotification()
sms = SMSNotification()
app = AppNotification()

# Polymorphism in action
notifications = [email, sms, app]

for notification in notifications:
    notification.send_message()