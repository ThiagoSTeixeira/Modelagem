import java.lang.Math;

public class Ex3{
	
	public static void main(String[] args){
		double y0 = 0;
		double v0 = 0;
		double t = 0;
		double dt = Math.PI/8;
		double y = y0;
		double v = v0;

		for(double i = 0; i < 100; i++){
			y = y + Math.cos(t)*dt;
			t = t + dt;
		}
		System.out.println("Results (Euler):");
		System.out.println("Final time: " + t);
		System.out.println("y = " + y);

		double yAnalitic = Math.sin(t);
		System.out.println("Results (Analitic):");
		System.out.println("y = " + yAnalitic);
	}
}