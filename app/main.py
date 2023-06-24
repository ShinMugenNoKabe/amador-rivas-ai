from schedule_twit_every_hour import schedule_twit_every_hour
import schedule
import time
import logging
import threading


def start_thread(func):
    job = threading.Thread(target=func)
    job.start()


def main():
    logging.info(f"Bot is on")
    
    schedule.every().minute.at(":30").do(start_thread, schedule_twit_every_hour)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()