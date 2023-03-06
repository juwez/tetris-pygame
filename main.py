import random
pieceList = {
    "I": [{"x": 3, "y": 21}, {"x": 4, "y": 21}, {"x": 5, "y": 21}, {"x": 5, "y": 21}],
    "J": [{"x": 3, "y": 21}, {"x": 3, "y": 22}, {"x": 4, "y": 21}, {"x": 5, "y": 21}],
    "L": [[{"x": 3, "y": 21}, {"x": 4, "y": 21}, {"x": 5, "y": 21}, {"x": 5, "y": 22}]],
    "O": [[{"x": 3, "y": 21}, {"x": 3, "y": 22}, {"x": 4, "y": 21}, {"x": 4, "y": 22}]],
    "S": [{"x": 3, "y": 21}, {"x": 4, "y": 21}, {"x": 4, "y": 22}, {"x": 5, "y": 22}],
    "T": [{"x": 3, "y": 21}, {"x": 4, "y": 21}, {"x": 4, "y": 22}, {"x": 5, "y": 21}],
    "Z": [{"x": 3, "y": 22}, {"x": 4, "y": 21}, {"x": 4, "y": 22}, {"x": 5, "y": 21}]
}
colors = {
    "I": "#00f0f0",
    "J": "#0000f0",
    "L": "#f0a000",
    "O": "#f0f000",
    "S": "#00f000",
    "T": "#a000f0",
    "Z": "#f00000"
}


class Piece:

    def __init__(self):
        self.shape = random.choice(list(pieceList))
        self.coordinates = pieceList[self.shape]
        self.orientation = 0
        self.color = colors[self.shape]


