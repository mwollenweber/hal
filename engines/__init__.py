from test import TestEngine


def get_engine(name):
    if not name:
        return None
    if name.lower() == 'test':
        return TestEngine

