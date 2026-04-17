    class P{
        int a = 10;
        public void func1(){System.out.println("A" + a);}
        public void func2(){System.out.println("B" + a);}
    }
    class C extends P{
        int a = 20;
        public void func1(){System.out.println("C" + a);}
        public void func3(){System.out.println("D" + a);}
    }
public class test4 {
    public static void main(String[] args) {
        P p = new C();
        p.func1();
        p.func2();
        ((C) p).func3();
}
}
