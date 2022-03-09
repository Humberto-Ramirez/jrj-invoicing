import logging

from jrj_invoicing.db.session import SessionLocal
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),  # stop at 5 minutes of execution
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),  # add handler before info
    after=after_log(logger, logging.WARN)  # add handler when warn log ocurrs
)
def init() -> None:
    """
    Await for postgres server & app db are ready
    """
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
