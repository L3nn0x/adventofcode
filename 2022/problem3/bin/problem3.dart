import 'dart:io';

int priority(String c) {
  int code = c[0].codeUnitAt(0);
  if (code >= 'a'.codeUnitAt(0) && code <= 'z'.codeUnitAt(0)) {
    return 1 + code - 'a'.codeUnitAt(0);
  } else {
    return 27 + code - 'A'.codeUnitAt(0);
  }
}

void main(List<String> arguments) async {
  var file = File("data.txt");

  var score = 0;
  List<Set<String>> data = [Set(), Set(), Set()];
  var index = 0;

  for (var line in await file.readAsLines()) {
    data[index] = Set.from(line.split(''));
    ++index;
    if (index == 3) {
      index = 0;
      var three = data[0].intersection(data[1].intersection(data[2]));
      score += three.fold(
          0, ((previousValue, element) => previousValue + priority(element)));
    }
  }
  print(score);
}
