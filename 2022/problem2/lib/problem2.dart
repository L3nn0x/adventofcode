enum Game implements Comparable<Game> {
  rock(points: 1),
  paper(points: 2),
  scissors(points: 3);

  const Game({required this.points});

  final int points;

  @override
  int compareTo(Game other) {
    if ((this == rock && other == scissors) ||
        (this == scissors && other == paper) ||
        (this == paper && other == rock)) {
      return 1;
    } else if (this == other) {
      return 0;
    } else {
      return -other.compareTo(this);
    }
  }

  static Game getWin(Game other) {
    for (var entry in Game.values) {
      if (entry.compareTo(other) == 1) {
        return entry;
      }
    }
    throw Exception("unreachable");
  }

  static Game getLoose(Game other) {
    for (var entry in Game.values) {
      if (entry.compareTo(other) == -1) {
        return entry;
      }
    }
    throw Exception("Unreachable");
  }
}
