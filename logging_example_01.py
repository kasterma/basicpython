import logging
import logging.config
import tempfile
import yaml


def main1():
    logging.info("Don't show this")
    logging.basicConfig(level=logging.INFO)  # b/c we have already logged this is ineffective
    logging.info("Don't show this")
    logging.error("Show this")


def main2():
    logging.basicConfig(level=logging.INFO)
    logging.info("Show this")
    logging.error("Show this")
    logging.debug("Don't show this")


def main3():
    with tempfile.NamedTemporaryFile() as tf:
        logging.basicConfig(filename=tf.name, level=logging.INFO)
        logging.info(f"using file ${tf.name}")
        logging.info("test")
        with open(tf.name) as f:
            print(f.readlines())


def main4():
    logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s - %(message)s", level=logging.INFO)
    logging.info("hello")


def main5():
    logger = logging.getLogger("main5")
    logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s - %(message)s", level=logging.INFO)
    logger.info("hello")


class ABC:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s - %(message)s", level=logging.INFO)   # (****)

    def logf(self):
        self.logger.info("logf called")


class BCD:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s - BBB %(message)s", level=logging.INFO)

    def logf(self):
        self.logger.info("logf called")


def main6():
    abc = ABC()
    abc.logf()
    bcd = BCD()
    bcd.logf()   # Note: still uses the basicConfig from the ABC call
    # rerunning with line (****) commented out, shows no log for abc.logf, but does show the log for bcd.logf and
    # uses the form of logging from BCD


def main7():
    bcd = BCD()
    abc = ABC()

    abc.logf()
    bcd.logf()


def main8():
    with open("logging_1.yaml") as log_conf_file:
        log_conf = yaml.load(log_conf_file)
    logging.config.dictConfig(log_conf)
    loga = logging.getLogger("loga")
    loga.info("yoyoyo")
    logb = logging.getLogger("logb")
    logb.info("tralalal")


def f(x, log=logging.getLogger("f_logger")):
    log.info(f"f called with {x}")


def main9(log_conf_filename="logging_1.yaml"):
    with open(log_conf_filename) as log_conf_file:
        log_conf = yaml.load(log_conf_file)
    logging.config.dictConfig(log_conf)

    loga = logging.getLogger("loga")
    loga.info("yoyoyo")
    f(2)
    f(3, loga)


def ff(x):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("hi", stack_info=True)
    return x


def main10():
    ff(3)


def main11():
    la = logging.getLogger("loggera")
    la.setLevel(logging.WARN)
    la.info("hi")
    la.setLevel(logging.INFO)
    la.info("hi")


if __name__ == '__main__':
    #main9("logging_2.yaml")
    #main10()
    main11()
    print("hi")

