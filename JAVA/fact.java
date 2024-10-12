// Source code is decompiled from a .class file using FernFlower decompiler.
public class fact {
   public fact() {
   }

   public static void main(String[] var0) {
      if (var0.length > 0) {
         String[] var1 = var0;
         int var2 = var0.length;

         for(int var3 = 0; var3 < var2; ++var3) {
            String var4 = var1[var3];
            int var5 = Integer.parseInt(var4);
            System.out.println("Factorial of " + var5 + " is: " + factorial(var5));
         }
      } else {
         System.out.println("Please provide numbers as command-line arguments.");
      }

   }

   public static int factorial(int var0) {
      int var1 = 1;

      for(int var2 = 1; var2 <= var0; ++var2) {
         var1 *= var2;
      }

      return var1;
   }
}
