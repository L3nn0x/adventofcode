import 'dart:io';
import 'package:collection/collection.dart';

void main(List<String> arguments) async {
  var entry = File("data.txt");

  var calories = <int, int>{};

  int index = 0;
  int currentValue = 0;

  for (var line in await entry.readAsLines()) {
    if (line.isEmpty) {
      currentValue = index + 1;
    } else {
      calories.update(currentValue, (value) => value + int.parse(line),
          ifAbsent: () => int.parse(line));
    }
    ++index;
  }

  var values = calories.values.toList();
  values.sort((a, b) => b.compareTo(a));

  print(values.getRange(0, 3).sum);
}
