import Room


class Living(Room.Room):

    def __init__(self, name):
        self.name = name
        self.allocations = []

    def get_type(self):
        return 'living'
