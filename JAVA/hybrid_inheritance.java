public class Child implements Mother, Father {
   public Child() {
   }

   public void show() {
      System.out.println("Mother and Father are parents ");
   }

   public void displayParents() {
      System.out.println("Two Parents");
   }

   public void displayChild() {
      System.out.println("Mother and Father have one child");
   }

   public static void main(String[] var0) {
      Child var1 = new Child();
      System.out.println("Implementation of Hybrid Inheritance in Java");
      var1.show();
      var1.displayParents();
      var1.displayChild();
   }
}
