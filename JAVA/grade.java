// 2. Accept 5 subject marks through command line arguments, find the average and total, and display the grade.
public class JavaLab {
    public static void main(String[] args) {
        if (args.length != 5) {
            System.out.println("Please provide exactly 5 subject marks.");
            return;
        }

        int total = 0;
        for (String arg : args) {
            total += Integer.parseInt(arg);
        }
        double average = total / 5.0;

        System.out.println("Total: " + total);
        System.out.println("Average: " + average);

        if (average > 80) {
            System.out.println("Grade: Outstanding");
        } else if (average > 60) {
            System.out.println("Grade: First Class");
        } else if (average > 50) {
            System.out.println("Grade: Second Class");
        } else if (average > 40) {
            System.out.println("Grade: Third Class");
        } else {
            System.out.println("Grade: Fail");
        }
    }
}
