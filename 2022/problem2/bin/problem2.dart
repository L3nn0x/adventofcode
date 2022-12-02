import 'dart:io';
import "package:problem2/problem2.dart";

Game? parseEntry(String input) {
  if (input == "A") {
    return Game.rock;
  } else if (input == "B") {
    return Game.paper;
  } else if (input == "C") {
    return Game.scissors;
  }
  return null;
}

Game? chooseYou(Game other, String input) {
  if (input == "X") {
    return Game.getLoose(other);
  } else if (input == "Y") {
    return other;
  } else if (input == "Z") {
    return Game.getWin(other);
  }
  return null;
}

void main(List<String> arguments) async {
  var file = File("data.txt");

  int score = 0;

  for (var line in await file.readAsLines()) {
    final splitted = line.split(" ");
    final opponent = parseEntry(splitted[0]);
    final you = chooseYou(opponent!, splitted[1]);

    switch (you?.compareTo(opponent)) {
      case 1:
        score += 6;
        break;
      case -1:
        score += 0;
        break;
      case 0:
        score += 3;
        break;
    }
    score += you!.points;
  }

  print(score);
}
