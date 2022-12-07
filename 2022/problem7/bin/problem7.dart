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

  const int totalSize = 70000000;
  const int requiredSize = 30000000;

  final int usedSpace = fs.size;
  final int spaceToFree = requiredSize - (totalSize - usedSpace);

  var directories = [];
  fs.march((node) {
    if (node.isFolder) {
      directories.add(node);
    }
  });

  directories.sort((a, b) => a.size.compareTo(b.size));

  for (final dir in directories) {
    if (dir.size >= spaceToFree) {
      print(dir.size);
      break;
    }
  }
}
