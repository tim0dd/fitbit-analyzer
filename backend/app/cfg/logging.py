import logging


class ColorLogFormatter(logging.Formatter):
    COLORS = {
        'WARNING': '\033[93m',   # Yellow
        'INFO': '\033[92m',      # Green
        'DEBUG': '\033[96m',     # Light Cyan
        'CRITICAL': '\033[31m',  # Dark Red
        'ERROR': '\033[91m',     # Red
        'NAME': '\033[95m',      # Purpleish
        'RESET': '\033[0m'       # Reset
    }

    def format(self, record):
        record.levelname = self.COLORS.get(record.levelname, self.COLORS['INFO']) + record.levelname + self.COLORS['RESET']
        record.name = self.COLORS['NAME'] + record.name + self.COLORS['RESET']
        return logging.Formatter.format(self, record)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "colored": {
            "()": ColorLogFormatter,
            "format": "%(levelname)s: %(name)s: %(message)s",
        },
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "colored"}},
    "loggers": {
        "": {"handlers": ["console"], "level": "INFO"},
        "uvicorn.error": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
        "uvicorn.access": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}
