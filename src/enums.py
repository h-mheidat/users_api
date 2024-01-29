from enum import Enum, unique


@unique  # This is used to ensure no integers are given to more than one item.
class Color(Enum):
    Black = 1
    White = 2
    Purple = 3
    Red = 4
    Green = 5
    Blue = 6

    @classmethod
    def return_color(cls, clr_num: int):
        colors = set(item.value for item in cls)

        if clr_num not in colors:
            return "I don't have a favourite."

        return cls(clr_num).name


@unique
class State(Enum):  # Check USA States API if this is not needed
    Alabama = 1
    Alaska = 2
    Arizona = 3
    Arkansas = 4
    California = 5
    Colorado = 6
    Connecticut = 7
    Delaware = 8
    Florida = 9
    Georgia = 10
    Hawaii = 11
    Idaho = 12
    Illinois = 13
    Indiana = 14
    Iowa = 15
    Kansas = 16
    Kentucky = 17
    Louisiana = 18
    Maine = 19
    Maryland = 20
    Massachusetts = 21
    Michigan = 22
    Minnesota = 23
    Mississippi = 24
    Missouri = 25
    Montana = 26
    Nebraska = 27
    Nevada = 28
    New_Hampshire = 29
    New_Jersey = 30
    New_Mexico = 31
    New_York = 32
    North_Carolina = 33
    North_Dakota = 34
    Ohio = 35
    Oklahoma = 36
    Oregon = 37
    Pennsylvania = 38
    Rhode_Island = 39
    South_Carolina = 40
    South_Dakota = 41
    Tennessee = 42
    Texas = 43
    Utah = 44
    Vermont = 45
    Virginia = 46
    Washington = 47
    West_Virginia = 48
    Wisconsin = 49
    Wyoming = 50

    @classmethod
    def return_state(cls, state_num: int):
        states = set(item.value for item in cls)

        if state_num not in states:
            return "No State."

        return cls(state_num).name
