import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

class Day1 {

    public Day1() {}
    public static void main(String[] args) {
        ArrayList<Integer> l1 = new ArrayList<>();
        ArrayList<Integer> l2 = new ArrayList<>();

        readToFile("C:\\Users\\J\\source\\repos\\aoc-2024\\Day1\\dayOneInput.txt", l1, l2);

        System.out.println(distance(l1,l2));

        System.out.println(similarity(l1, l2));
    }

    private static void readToFile(String filename, List<Integer> listOne, List<Integer> listTwo) {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] splited = line.split("\\s+");
                listOne.add(Integer.valueOf(splited[0]));
                listTwo.add(Integer.valueOf(splited[1]));
            }
        } catch (IOException exception) {
            System.err.println(exception);
        }
    }

    private static int distance(List<Integer> listOne, List<Integer> listTwo) {
        Collections.sort(listOne);
        Collections.sort(listTwo);

        int distance = 0;

        for (int i = 0; i < listOne.size(); i++) {
            distance += Math.abs(listOne.get(i) - listTwo.get(i));
        }

        return distance;
    }

    private static int similarity(List<Integer> listOne, List<Integer> listTwo) {
        int similarity = 0;

        HashMap<Integer, Integer> listOneCounts = new HashMap<>();

        for (Integer integer : listOne) {
            listOneCounts.put(integer, listOneCounts.getOrDefault(integer, 0));
        }

        System.out.println(listOneCounts.size());

        for (Integer integer : listTwo) {
            if (listOneCounts.containsKey(integer)) {
                listOneCounts.put(integer, listOneCounts.getOrDefault(integer, 0) + 1);
            }
        }

        // System.out.println(listOneCounts);

        for (Integer key : listOneCounts.keySet()) {
            similarity += listOneCounts.getOrDefault(key, 0) * key;
        }

        return similarity;
    }
}