import 'package:problem7/node.dart';
import 'package:test/test.dart';

void main() {
  test("Calculate Size", () {
    var dir = Node.root();
    var subdir = Node.makeDir(dir, "a");
    var file1 = Node.makeFile(dir, "b", 41);
    var file2 = Node.makeFile(subdir, "c", 1);

    expect(42, dir.size);
  });

  test("Get Path", () {
    var dir = Node.root();
    var subdir = Node.makeDir(dir, "a");
    var file1 = Node.makeFile(dir, "b", 41);
    var file2 = Node.makeFile(subdir, "c", 1);

    expect(file2, dir.getNodeFromPath("a/c"));
    expect(file2, subdir.getNodeFromPath("../a/c"));
    expect(file2, subdir.getNodeFromPath("/a/c"));
  });

  test("Is Dir", () {
    expect(true, Node.root().isFolder);
    expect(true, Node.makeDir(Node.root(), "a").isFolder);
    expect(false, Node.makeFile(Node.root(), "a", 1).isFolder);
  });
}
