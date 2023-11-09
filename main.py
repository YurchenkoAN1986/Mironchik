import logging
import sys
import app_logger
import xml.etree.ElementTree


if __name__ == "__main__":
    logger:logging.Logger = app_logger.getLogger(__name__)


    try:
        pass
        logger.debug('Nachalo raboty')
        logger.info('-----Nachalo raboty')
        if 1 == 1:
            raise Exception('Test oshibok')
    except Exception as e:
        logger.error(f'Oshibka v rabote prilozhenia:{e}')
        sys.exit(-1)
    finally:
        logger.info('------Okonchanie raboty')
    #print(2+2)

    #
    # logger:logging.Logger=app_logger.get_Logger(__name__)
    # logger.debug("Osnovnoi potok")
    # logger.info("Osnovnoi potok")
    # logger.error("Osnovnoi potok")
