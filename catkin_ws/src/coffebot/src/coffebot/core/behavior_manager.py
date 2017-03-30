#!/usr/bin/env python3

class Behavior:

    def __init__(self):
        self.behavior_name = None

    def get_behavior() -> str or None:
        return self.behavior_name

    def _run_behavior(pattern: dict):
        pass

    def set_behavior_pattern(pattern: dict):
        self.behavior_name = pattern['name']
        self._run_behavior(pattern)
