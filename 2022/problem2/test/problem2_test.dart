import 'package:problem2/problem2.dart';
import 'package:test/test.dart';

void main() {
  test("Game Values", () {
    expect(Game.rock.points, 1);
    expect(Game.paper.points, 2);
    expect(Game.scissors.points, 3);
  });

  test("Game Wins", () {
    expect(Game.rock.compareTo(Game.scissors), 1);
    expect(Game.scissors.compareTo(Game.paper), 1);
    expect(Game.paper.compareTo(Game.rock), 1);
  });

  test("Game Looses", () {
    expect(Game.scissors.compareTo(Game.rock), -1);
    expect(Game.paper.compareTo(Game.scissors), -1);
    expect(Game.rock.compareTo(Game.paper), -1);
  });

  test("Game Draws", () {
    expect(Game.rock.compareTo(Game.rock), 0);
    expect(Game.scissors.compareTo(Game.scissors), 0);
    expect(Game.paper.compareTo(Game.paper), 0);
  });

  test("Get Wins", () {
    expect(Game.getWin(Game.rock), Game.paper);
    expect(Game.getWin(Game.scissors), Game.rock);
    expect(Game.getWin(Game.paper), Game.scissors);
  });

  test("Get Looses", () {
    expect(Game.getLoose(Game.rock), Game.scissors);
    expect(Game.getLoose(Game.scissors), Game.paper);
    expect(Game.getLoose(Game.paper), Game.rock);
  });
}
