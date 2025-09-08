package amdocs;

public class Student {
	String name;
	int age;
	char section, gender;
	int subj1, subj2, subj3;
	
	public Student(String name, int age, char section, char gender, int subj1, int subj2, int subj3) {
		this.name = name;
		this.age = age;
		this.section = section;
		this.gender = gender;
		this.subj1 = subj1;
		this.subj2 = subj2;
		this.subj3 = subj3;
	}
	
	public static void display(Student s) {
		int total = s.subj1 + s.subj2 + s.subj3;
		double percent = total / 3.0;
		
		System.out.println(s.name + " " + s.age +" " + s.section + " " + s.gender);
		System.out.println(total + " " + percent);
	}
	
	public static void main(String args[]) {
		Student s1 = new Student("abc", 16, 'A', 'M', 89, 94, 67);
		Student s2 = new Student("def", 15, 'A', 'F', 0, 90, 77);
		Student s3 = new Student("ghi", 16, 'B', 'M', 0, 97, 60);
		Student s4 = new Student("jkl", 17, 'B', 'F', 79, 98, 97);

		display(s1);
		display(s2);
		display(s3);
		display(s4);
	}
}
