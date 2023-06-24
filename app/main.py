from schedule_twit_every_hour import schedule_twit_every_hour
import schedule
import time
import logging


def main():
    logging.info(f"Bot is on")
    
    schedule.every(20).seconds.do(schedule_twit_every_hour)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()