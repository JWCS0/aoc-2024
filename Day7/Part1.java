package Day7;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Stream;

public class Part1 {

    public String FILENAME = "C:\\Users\\J\\source\\repos\\aoc-2024\\Day7\\daySevenInput.txt";
    HashMap<Long, List<Long>> map = new HashMap<>();

    public Part1() {
        try (BufferedReader br = new BufferedReader(new FileReader(FILENAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                Long res = Long.parseLong(line.split(":")[0].strip());
                List<Long> ints = Stream.of(line.split(":")[1].strip().split(" ")).map(x -> Long.parseLong(x)).toList();
                map.put(res, ints);
            }
        } catch (IOException exception) {
            System.err.println(exception);
        }
    }

    public void method(List<Long> values, Long runningTotal, List<Long> results, int index) {
        if (index == values.size() - 1) {
            results.add(runningTotal + values.get(index));
            results.add(runningTotal == 0 ? values.get(index) : runningTotal * values.get(index));
            return;
        } 

        method(values,
            runningTotal + values.get(index),
            results,
            index + 1);
        method(values,
            runningTotal == 0 ? values.get(index) : runningTotal * values.get(index),
            results,
            index + 1);
    }

    public static void main(String[] args) {
        Part1 p1 = new Part1();

        List<Long> result = new ArrayList<>();

        Long total = 0L;
        for (Long value: p1.map.keySet()) {
            p1.method(p1.map.get(value), 0L, result, 0);
            if (result.contains(value)) {
                total += value;
            }
        }

        System.out.println(total);
    }
}
