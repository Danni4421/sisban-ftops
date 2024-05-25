from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class FuzzyMember(ABC):
    tipe: str

    def __init__(self, tipe):
        self.tipe = tipe

    @abstractmethod
    def fuzzify(self, x):
        pass


class MemberReward(ABC):
    @abstractmethod
    def get_reward(self, alpha):
        pass


class LinearDown(FuzzyMember, MemberReward):
    min: int
    max: int

    def __init__(self, config):
        super().__init__(tipe="linear_down")
        self.min = config.get('min')
        self.max = config.get('max')

    def fuzzify(self, x):
        if x <= self.min:
            return 1
        elif self.min <= x <= self.max:
            return (self.max - x) / (self.max - self.min)
        elif x >= self.max:
            return 0

    def get_reward(self, alpha):
        return self.max - (alpha * (self.max - self.min))


class LinearUp(FuzzyMember, MemberReward):
    min: int
    max: int

    def __init__(self, config):
        super().__init__(tipe="linear_up")
        self.min = config.get('min')
        self.max = config.get('max')

    def fuzzify(self, x):
        if x <= self.min:
            return 0
        elif self.min <= x <= self.max:
            return (x - self.min) / (self.max - self.min)
        elif x >= self.max:
            return 1

    def get_reward(self, alpha):
        return self.min + (alpha * (self.max - self.min))


class Triangle(FuzzyMember):
    min: int
    middle: int
    max: int

    def __init__(self, config):
        super().__init__(tipe="triangle")
        self.min = config.get('min')
        self.middle = config.get('middle')
        self.max = config.get('max')

    def fuzzify(self, x):
        if x <= self.min or x >= self.max:
            return 0
        elif self.min <= x <= self.middle:
            return (x - self.min) / (self.middle - self.min)
        elif self.middle <= x <= self.max:
            return (self.max - x) / (self.max - self.middle)


class Trapezium(FuzzyMember):
    min: int
    middle_one: int
    middle_two: int
    max: int

    def __init__(self, config):
        super().__init__(tipe="trapezium")
        self.min = config.get('min')
        self.middle_one = config.get('middle_one')
        self.middle_two = config.get('middle_two')
        self.max = config.get('max')

    def fuzzify(self, x):
        if x <= self.min or x >= self.max:
            return 0
        elif self.min <= x <= self.middle_one:
            return (x - self.min) / (self.middle_one - self.min)
        elif self.middle_one <= x <= self.middle_two:
            return 1
        elif self.middle_two <= x <= self.max:
            return (self.max - x) / (self.max - self.middle_two)