import 'dart:io';
import 'package:problem7/node.dart';

Node parseInput(File file) {
  Node root = Node.root();
  Node current = root;

  for (final line in file.readAsLinesSync()) {
    final splitted = line.split(' ');
    if (splitted[0] == '\$') {
      if (splitted[1] == "cd") {
        current = current.getNodeFromPath(splitted[2]);
      }
    } else {
      if (splitted[0] == "dir") {
        Node.makeDir(current, splitted[1]);
      } else {
        Node.makeFile(current, splitted[1], int.parse(splitted[0]));
      }
    }
  }
  return root;
}

void main(List<String> arguments) {
  var fs = parseInput(File("data.txt"));

  int size = fs.fold(0, (init, node) {
    if (node.isFolder && node.size < 100000) {
      return init + node.size;
    }
    return init;
  });

  print(size);
}
