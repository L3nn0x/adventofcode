class Node {
  final String name;
  int? cachedSize;
  List<Node> children = [];
  late Node parent;
  final bool isFolder;

  int get size {
    if (cachedSize == null) {
      int size = 0;
      for (var child in children) {
        size += child.size;
      }
      cachedSize = size;
    }
    return cachedSize!;
  }

  Node.root()
      : name = "/",
        isFolder = true {
    parent = this;
  }

  Node(this.parent, this.name, this.isFolder);

  static Node makeDir(Node parent, String name) {
    var node = Node(parent, name, true);
    parent.children.add(node);
    return node;
  }

  static Node makeFile(Node parent, String name, int size) {
    var node = Node(parent, name, false);
    node.cachedSize = size;
    parent.children.add(node);
    return node;
  }

  Node getNodeFromPath(String path) {
    Node current = this;
    final splitted = path.split("/");
    if (path[0] == '/') {
      while (current != current.parent) {
        current = current.parent;
      }
    }

    for (final name in splitted) {
      if (name == "..") {
        current = current.parent;
      } else {
        for (final child in current.children) {
          if (child.name == name) {
            current = child;
            break;
          }
        }
      }
    }

    return current;
  }

  void display({int indent = 0}) {
    final indentString = " " * indent;
    if (children.isNotEmpty) {
      print("$indentString$name: ($size)");
    } else {
      print("$indentString$name ($size)");
    }
    for (final entry in children) {
      entry.display(indent: indent + 2);
    }
  }

  T fold<T>(T init, T Function(T, Node) function) {
    init = function(init, this);
    for (final child in children) {
      init = child.fold(init, function);
    }
    return init;
  }
}
