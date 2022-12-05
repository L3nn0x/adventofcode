import "dart:io";

List<List<String>> parseInitialConfig(Iterator<String> lines) {
  var result = <List<String>>[];

  while (lines.moveNext()) {
    if (lines.current.isEmpty) {
      break;
    }
    int stackIndex = 0;
    int spaces = 0;
    for (var index = 0; index < lines.current.length; ++index) {
      String char = lines.current[index];
      if (char == ' ') {
        ++spaces;
      } else if (char == '[') {
        stackIndex += spaces ~/ 4 + spaces % 2;
        spaces = 0;
        if (result.length <= stackIndex) {
          final length = result.length;
          for (int i = 0; i <= stackIndex - length; ++i) {
            result.add([]);
          }
        }
        result[stackIndex].insert(0, lines.current[index + 1]);
      }
    }
  }

  return result;
}

// format for a command is [n, start, end]
List<List<int>> parseCommands(Iterator<String> lines) {
  var result = <List<int>>[];

  while (lines.moveNext()) {
    final splitted = lines.current.split(' ');
    result.add([
      int.parse(splitted[1]),
      int.parse(splitted[3]) - 1,
      int.parse(splitted[5]) - 1
    ]);
  }

  return result;
}

void main(List<String> arguments) {
  var file = File("data.txt");
  var lines = file.readAsLinesSync();

  var it = lines.iterator;
  final data = parseInitialConfig(it);
  print(data);
  final commands = parseCommands(it);
  print(commands);

  for (final command in commands) {
    final n = command[0];
    final start = command[1];
    final end = command[2];

    final startIndex = data[start].length - n;
    final endIndex = data[start].length;
    data[end].addAll(data[start].getRange(startIndex, endIndex));
    data[start].removeRange(startIndex, endIndex);
  }

  String result = data.fold("", (value, e) => value + e.last);

  print(result);
}
