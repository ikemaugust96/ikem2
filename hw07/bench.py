class Bench:
    """A class representing a sidelines bench"""

    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.bench = []

    def send_to_bench(self, player_name):
        # TODO: Put the player "onto the bench"
        if player_name not in self.bench:
            self.bench.append(player_name)
            print(f"{player_name} has been sent to the bench.")
        else:
            print(f"{player_name} is already on the bench.")

    def get_from_bench(self):
        # TODO: Return the name of the player who has
        # been on the bench longest.
        if self.bench:
            player_name = self.bench.pop(0)
            print(f"Got {player_name} from the bench.")
            return player_name
        else:
            print("The bench is empty.")
            return None

    # TODO: Write the function that will display the
    # current list of players on the bench
    def show_bench(self):
        if self.bench:
            print("The bench currently includes:")
            for player in self.bench:
                print(player)
        else:
            print("The bench is empty.")

    # TODO: Write any other methods that might be used
    # by the methods above.
