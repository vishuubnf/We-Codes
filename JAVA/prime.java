public class prime {
    public static void main(String[] args) {
        if (args.length > 0) {
            int n = Integer.parseInt(args[0]);
            System.out.println("Prime numbers up to " + n + ":");

            for (int i = 2; i <= n; i++) {
                if (isPrime(i)) {
                    System.out.print(i + " ");
                }
            }
        } else {
            System.out.println("Please provide a number as a command-line argument.");
        }
    }

    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

