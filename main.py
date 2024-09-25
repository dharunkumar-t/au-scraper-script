from scraper import get_announcements
from email_service import send_email

def main():
    announcements = get_announcements()
    if announcements:
        for announcement in announcements:
            send_email(announcement)
            print(f"Sent Email: {announcement}")
    else:
        print("No new announcements found.")

if __name__ == "__main__":
    main()
