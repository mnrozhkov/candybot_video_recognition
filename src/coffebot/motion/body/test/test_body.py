#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 FunRobots Lab

# Project: Candybot: Coffebot
# Summary: Test for motion_eyes_controller
# version: v1
# Test marks and interpretations
#     1) Серьезность (Severity) Наиболее распространена пятиуровневая система градации серьезности дефекта:
#         • S1 Блокирующий (Blocker)
#         • S2 Критический (Critical)
#         • S3 Значительный (Major)
#         • S4 Незначительный (Minor)
#         • S5 Тривиальный (Trivial)
#     2) Приоритет (Priority) Приоритет дефекта:
#         • P1 Высокий (High)
#         • P2 Средний (Medium)
#         • P3 Низкий (Low)

import os
import sys
from pathlib import Path
import random
import pytest

top = Path(__file__).resolve().parents[1]
sys.path.append(str(top))


