import time
import datetime
from playsound import playsound
def set_alarm(alarm_time, tone, snooze_duration):
    print(f"Alarm set for {alarm_time} with tone '{tone}'")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm ringing!")
            playsound(tone)
            snooze = input("Press 's' to snooze for {} minutes or any other key to stop: ".format(snooze_duration))
            if snooze.lower() == 's':
                print("Snoozing for {} minutes...".format(snooze_duration))
                time.sleep(snooze_duration * 60)  # Snooze for the specified duration
                print("Snooze over! Alarm will ring again.")
            else:
                print("Alarm stopped.")
                break
        time.sleep(1)
def main():
    alarm_time = input("Enter alarm time (HH:MM format, 24-hour): ")
    # Using the provided audio file path directly
    tone = r"C:\Users\harin\Downloads\bomb-countdown-beeps-6868.mp3"
    snooze_duration = int(input("Enter snooze duration in minutes: "))
    set_alarm(alarm_time, tone, snooze_duration)
if __name__ == "__main__":
    main()


