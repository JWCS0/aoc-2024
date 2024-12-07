package Day6;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Stack;
import java.util.stream.Collectors;

class DaySixPartTwo {
    public List<List<Character>> originalGrid;
    public String FILENAME = "C:\\Users\\J\\source\\repos\\aoc-2024\\Day6\\daySixInput.txt";
    
    public int originX;
    public int originY;

    public LinkedHashMap<Character, DirectionClass> directionModifiers = new LinkedHashMap<Character, DirectionClass>();
    public LinkedHashMap<Character, Character> symbolMap = new LinkedHashMap<>();

    public DaySixPartTwo() {
        this.originalGrid = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(FILENAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                originalGrid.add(line.chars().mapToObj(c -> (char) c).collect(Collectors.toList()));
                if (line.contains("^")) {
                    this.originX = line.indexOf("^");
                    this.originY = originalGrid.size() - 1;
                }
            }
        } catch (IOException exception) {
            System.err.println(exception);
        }

        directionModifiers.put('N', new DirectionClass(0, -1));
        directionModifiers.put('E', new DirectionClass(1, 0));
        directionModifiers.put('S', new DirectionClass(0, 1));
        directionModifiers.put('W', new DirectionClass(-1, 0));

        symbolMap.put('N', '^');
        symbolMap.put('E', '>');
        symbolMap.put('S', 'v');
        symbolMap.put('W', '<');
    }

    private class Guard {
        int x;
        int y;
        Character direction;
        Character symbol;

        public Guard() {
            this.x = originX;
            this.y = originY;
            this.direction = 'N';
            this.symbol = '^';
        }

        public void rotate() {
            int currentDirectionIndex = new ArrayList<>(directionModifiers.keySet()).indexOf(this.direction);
            this.direction = new ArrayList<>(directionModifiers.keySet()).get((currentDirectionIndex + 1)%4);
            this.symbol = symbolMap.get(this.direction);
        }

        public boolean isInBounds() {
            return DaySixPartTwo.this.isInBounds(originX, originY);
        }
    }

    private class DirectionClass {
        int xDelta;
        int yDelta;

        public DirectionClass(int x, int y) {
            this.xDelta = x;
            this.yDelta = y;
        }
    }

    private class LocationClass {
        int x;
        int y;

        public LocationClass(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public String toString() {
            return "Location " + x + " " + y;
        }
    }

    public boolean isInBounds(int x, int y) {
        return x >= 0 &&
            x < originalGrid.get(0).size() &&
            y >= 0 &&
            y < originalGrid.size();
    }

    public boolean isInBounds(LocationClass loc) {
        return loc.x >= 0 &&
            loc.x < originalGrid.get(0).size() &&
            loc.y >= 0 &&
            loc.y < originalGrid.size();
    }

    public Character[][] copyGrid() {
        Character[][] stringArray = originalGrid.stream().map(u -> u.toArray(Character[]::new)).toArray(Character[][]::new);

        return stringArray;
    }

    public static void main(String[] args) {
        DaySixPartTwo obj = new DaySixPartTwo();
        Character[][] grid = obj.copyGrid();
        Guard guard = obj.new Guard();
        Stack<String> path = new Stack<>();

        while(guard.isInBounds()) {
            LocationClass newLocation = obj.new LocationClass(
                guard.x + obj.directionModifiers.get(guard.direction).xDelta,
                guard.y + obj.directionModifiers.get(guard.direction).yDelta);

            if (!obj.isInBounds(newLocation)) {
                break;
            }

            if (grid[newLocation.y][newLocation.x] == '#') {
                guard.rotate();
                continue;
            }

            if (grid[newLocation.y][newLocation.x] == '.') {
                path.push(Integer.toString(newLocation.x) +
                    ',' + 
                    Integer.toString(newLocation.y));
                grid[guard.y][guard.x] = ' ';
            }

            grid[newLocation.y][newLocation.x] = guard.symbol;
            guard.x = newLocation.x;
            guard.y = newLocation.y;
        }

        int count = 0;

        while(!path.isEmpty()) {
            String s = path.pop();
            String[] locationString = s.split(",");
            LocationClass blockLocation = obj.new LocationClass(Integer.parseInt(locationString[0]), Integer.parseInt(locationString[1]));
            Character[][] newGrid = obj.copyGrid();
            newGrid[blockLocation.y][blockLocation.x] = '#';
            Guard ephemeralGuard = obj.new Guard();
            HashSet<String> seenPositions = new HashSet<>();

            while(ephemeralGuard.isInBounds()) {
                LocationClass newLocation = obj.new LocationClass(
                    ephemeralGuard.x + obj.directionModifiers.get(ephemeralGuard.direction).xDelta,
                    ephemeralGuard.y + obj.directionModifiers.get(ephemeralGuard.direction).yDelta);

                String locationAndDirection = Integer.toString(newLocation.x) +
                                                "|" +
                                                Integer.toString(newLocation.y) +
                                                "|" +
                                                ephemeralGuard.direction;

                if (seenPositions.contains(locationAndDirection)) {
                    count++;
                    break;
                }
    
                if (!obj.isInBounds(newLocation)) {
                    break;
                }
    
                if (newGrid[newLocation.y][newLocation.x] == '#') {
                    ephemeralGuard.rotate();
                    continue;
                }
    
                if (newGrid[newLocation.y][newLocation.x] == '.') {
                    newGrid[ephemeralGuard.y][ephemeralGuard.x] = '.';
                }
                
                seenPositions.add(locationAndDirection);
                newGrid[newLocation.y][newLocation.x] = ephemeralGuard.symbol;
                ephemeralGuard.x = newLocation.x;
                ephemeralGuard.y = newLocation.y;
            }
        }

        System.out.println(count);
    }
}