import 'dart:io';
import 'dart:collection';

const int LENGTH = 14;

void main(List<String> arguments) {
  var file = File("data.txt");

  final line = file.readAsStringSync();
  if (line.length < 4) {
    return;
  }
  var window = Queue();
  int index = 0;
  for (; index < line.length; ++index) {
    if (window.length == LENGTH) {
      window.removeFirst();
    }
    window.addLast(line[index]);
    final set = Set.from(window);
    if (set.length == LENGTH) {
      break;
    }
  }

  print(index + 1);
}
