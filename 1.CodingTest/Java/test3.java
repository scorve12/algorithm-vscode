class A {
    int cost = 10;
    A() {
        System.out.print("A");
        outputCost();
    }
    void outputCost() {
        System.out.print(cost);
    }   
}

class B extends A {
    int cost = 20;
    B() {
        System.out.print("B");
        outputCost();
    }
    void outputCost() {
        System.out.print(cost);
    }   
}

public class test3 {
    public static void main(String[] args) {
        A a = new B();
        System.out.print(a.cost);
    }
}
