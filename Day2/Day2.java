import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class Day2 {
    private static void partOne(String filename) {
        int validSequences = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            boolean result;
            while ((line = br.readLine()) != null) {
                result = validateSequence(line);
                validSequences += result ? 1 : 0;
            }
        } catch (IOException exception) {
            System.err.println(exception);
        }
        System.out.println(validSequences);
    }

    // validate method
    private static boolean validateSequence(String sequence) {
        String[] splitValues = sequence.split("\\s+");

        int difference = Integer.parseInt(splitValues[0]) - Integer.parseInt(splitValues[1]);

        if (difference < 0) {
            return isValidSequence(splitValues, true, false) ||
                    isValidSequence(dampen(splitValues, 0), true, true)||
                    isValidSequence(dampen(splitValues, 0), false, true);
        } else {
            return isValidSequence(splitValues, false, false) ||
                    isValidSequence(dampen(splitValues, 0), false, true)||
                    isValidSequence(dampen(splitValues, 0), true, true);
        }
    }

    private static boolean isValidSequence(String[] numbers, boolean increasing, boolean isNumbersModified) {
        int difference;
        for (int i = 0; i < numbers.length - 1; i++) {
            difference = Integer.parseInt(numbers[i]) - Integer.parseInt(numbers[i+1]);

            if (increasing && (difference >= -3 && difference < 0)) continue;

            else if (!increasing && (difference <= 3 && difference > 0)) continue;

            if (!isNumbersModified) {
                return isValidDampenedSequence(numbers, increasing, i);
            }

            return false;
        }

        return true;
    }

    private static boolean isValidDampenedSequence(String[] numbers, boolean increasing, int index) {
        return isValidSequence(dampen(numbers, 0), true, true) ||
        isValidSequence(dampen(numbers, index), true, true) ||
        isValidSequence(dampen(numbers, index+1), true, true) ||
        isValidSequence(dampen(numbers, 0), false, true) ||
        isValidSequence(dampen(numbers, index), false, true) ||
        isValidSequence(dampen(numbers, index+1), false, true);
    }

    private static String[] dampen(String[] numbers, int index) {
        List<String> output = new ArrayList<>();
        for (int i = 0; i < numbers.length; i++) {
            if (i != index) {
                output.add(numbers[i]);
            }
        }
        return output.toArray(new String[0]);
    }

    public static void main(String[] args) {
        partOne("C:\\Users\\J\\source\\repos\\aoc-2024\\Day2\\dayTwoInput.txt");
    }
}