"""
components.py

This file defines components of our ML pipeline and their respective
metadata.
"""

from mltrace import Component
from tests import *


class Cleaning(Component):
    def __init__(self, beforeTests=[], afterTests=[]):

        super().__init__(
            name="cleaning",
            owner="plumber",
            description="Cleans raw NYC taxicab data",
            tags=["nyc-taxicab"],
            beforeTests=beforeTests,
            afterTests=afterTests,
        )


class Featuregen(Component):
    def __init__(self, beforeTests=[], afterTests=[]):

        super().__init__(
            name="featuregen",
            owner="spark-gymnast",
            description="Generates features for high tip prediction problem",
            tags=["nyc-taxicab"],
            beforeTests=beforeTests,
            afterTests=afterTests,
        )


class TrainTestSplit(Component):
    def __init__(self, beforeTests=[], afterTests=[]):

        super().__init__(
            name="splitting",
            owner="fission",
            description="Splits data into training and test sets",
            tags=["nyc-taxicab"],
            beforeTests=beforeTests,
            afterTests=afterTests,
        )


class Training(Component):
    def __init__(self, beforeTests=[], afterTests=[]):

        super().__init__(
            name="training",
            owner="personal-trainer",
            description="Trains model for high tip prediction problem",
            tags=["nyc-taxicab"],
            beforeTests=beforeTests,
            afterTests=afterTests,
        )


class Inference(Component):
    def __init__(self, beforeTests=[], afterTests=[]):

        super().__init__(
            name="inference",
            owner="sherlock-holmes",
            description="Predicts high tip probability",
            tags=["nyc-taxicab"],
            beforeTests=beforeTests,
            afterTests=afterTests,
        )
