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
            
            while ((line = br.readLine()) != null) {
                validSequences += validateSequence(line) ? 1 : 0;
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
        if (Math.abs(difference) > 3 || difference == 0) return false;

        if (difference < 0) {
            return isValidIncreasingSequence(splitValues, true);
        } else {
            return isValidDecreasingSequence(splitValues, true);
        }
    }

    private static boolean isValidIncreasingSequence(String[] numbers, boolean firstTime) {
        int difference;
        for (int i = 0; i < numbers.length - 1; i++) {
            difference = Integer.parseInt(numbers[i]) - Integer.parseInt(numbers[i+1]);
            if (difference >= -3 && difference < 0) continue;

            if (firstTime) {
                return false;
                // return isValidIncreasingSequence(dampen(numbers, i), false) ||
                //         isValidIncreasingSequence(dampen(numbers, i+1), false);
            }

            return false;
        }

        return true;
    }

    private static boolean isValidDecreasingSequence(String[] numbers, boolean firstTime) {
        int difference;
        for (int i = 0; i < numbers.length - 1; i++) {
            difference = Integer.parseInt(numbers[i]) - Integer.parseInt(numbers[i+1]);

            if (difference <= 3 && difference > 0) continue;

            if (firstTime) {
                return false;
                // return isValidDecreasingSequence(dampen(numbers, i), false) ||
                //         isValidDecreasingSequence(dampen(numbers, i+1), false);
            }

            return false;
        }

        return true;
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
        partOne("/workspaces/aoc-2024/Day2/dayTwoInput.txt");
    }
}