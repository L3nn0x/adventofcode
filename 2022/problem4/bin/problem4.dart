import 'dart:io';

void main(List<String> arguments) async {
  var file = File("data.txt");

  var score = 0;

  for (final line in await file.readAsLines()) {
    final splitted = line.split(",");
    final left = splitted[0].split("-");
    final right = splitted[1].split("-");
    final leftStart = int.parse(left[0]);
    final leftEnd = int.parse(left[1]);
    final rightStart = int.parse(right[0]);
    final rightEnd = int.parse(right[1]);

    if (leftEnd >= rightStart && leftStart <= rightEnd) {
      ++score;
    }
  }

  print(score);
}
