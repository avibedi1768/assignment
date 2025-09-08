package amdocs;

public class Shape {
	int l, b;
	int r;
	int a;
	double pi;
	
	Shape(){
		
	}
	
	Shape(int l, int b){
		this.l = l;
		this.b = b;
	}
	
	Shape(int a){
		this.a = a;
	}
	
	Shape(int r, double pi){
		this.r = r;
		this.pi = pi;
	}
	
	public static void area_rect(Shape rect) {
		System.out.println("rect: " + (rect.l * rect.b));
	}
	
	public static void area_square(Shape square) {
		System.out.println("square: " + square.a * square.a);
	}
	
	public static void area_circle(Shape circle) {
		System.out.println("circle: " + (circle.pi * circle.r * circle.r));
	}
	
	public static void main(String args[]) {
		Shape s1 = new Shape();
		Shape rect = new Shape(4, 5);
		Shape square = new Shape(5);
		Shape circle = new Shape(5, 3.14);

		area_rect(rect);
		area_square(square);
		area_circle(circle);
		
		double triangle = find_area(3, 4, 5);
		double rhombus = find_area(4, 5);
		

		System.out.println("triangle: " + triangle);
		System.out.println("rhombus: " + rhombus);
	}
	
	public static double find_area(int a, int b, int c) {
		double s = (a + b + c) / 2.0;
		return Math.sqrt(s * (s - a) * (s - b) * (s - c));
	}
	
	public static double find_area(int a, int b){
		return a * b;
	}
}
