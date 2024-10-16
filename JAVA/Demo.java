// Source code is decompiled from a .class file using FernFlower decompiler.
public class Demo {
   public Demo() {
   }

   public static void main(String[] var0) {
      int[] var1 = new int[]{6, 8, 9, 7, 90};
      int var2 = 0;
      int var3 = 0;
      int[] var4 = var1;
      int var5 = var1.length;

      for(int var6 = 0; var6 < var5; ++var6) {
         int var7 = var4[var6];
         if (var7 > var2) {
            var3 = var2;
            var2 = var7;
         } else if (var7 > var3 && var7 < var2) {
            var3 = var7;
         }
      }

      System.out.println("Max: " + var2);
      System.out.println("Second Max: " + var3);
   }
}
